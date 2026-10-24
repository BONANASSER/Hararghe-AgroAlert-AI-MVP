import csv
import os
from functools import lru_cache
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = Path(os.getenv("AGROALERT_DATA_DIR", PROJECT_ROOT / "data"))
PRECIPITATION_FILE = DATA_DIR / "chirps" / "hararghe_zones_chirps_monthly_1990_2026.csv"
REMOTE_SENSING_FILE = DATA_DIR / "nasa" / "hararghe_zones_remote_sensing_1990_2026.csv"


class DatasetUnavailableError(Exception):
    pass


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise DatasetUnavailableError(f"Required dataset is missing: {path}")

    with path.open(newline="", encoding="utf-8-sig") as csv_file:
        return list(csv.DictReader(csv_file))


def _number(record: dict[str, str], field: str) -> float | None:
    value = record.get(field, "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError as error:
        raise DatasetUnavailableError(
            f"Invalid numeric value in field '{field}': {value!r}"
        ) from error


@lru_cache(maxsize=1)
def get_latest_snapshot() -> tuple[str, list[dict[str, Any]]]:
    precipitation_rows = _read_csv(PRECIPITATION_FILE)
    if not precipitation_rows:
        raise DatasetUnavailableError(f"Dataset contains no records: {PRECIPITATION_FILE}")

    latest_date = max(row.get("date", "") for row in precipitation_rows)
    latest_precipitation = {
        row["woreda_id"]: row
        for row in precipitation_rows
        if row.get("date") == latest_date and row.get("woreda_id")
    }
    remote_sensing_rows = _read_csv(REMOTE_SENSING_FILE)
    remote_sensing_by_woreda = {
        row["woreda_id"]: row
        for row in remote_sensing_rows
        if row.get("date") == latest_date and row.get("woreda_id")
    }

    snapshot = []
    for woreda_id, precipitation in latest_precipitation.items():
        remote_sensing = remote_sensing_by_woreda.get(woreda_id, {})
        snapshot.append(
            {
                "woreda_id": woreda_id,
                "woreda_name": precipitation.get("woreda_name", ""),
                "zone_name": precipitation.get("zone_name", ""),
                "date": latest_date,
                "spi_3m": _number(precipitation, "spi_3m"),
                "precip_mm": _number(precipitation, "precip_mm"),
                "drought_hazard_category": precipitation.get(
                    "drought_hazard_category", ""
                ),
                "vci": _number(remote_sensing, "vci"),
                "soil_moisture": _number(remote_sensing, "smap_soil_moist"),
                "ipc_phase": _number(remote_sensing, "fews_ipc_phase"),
                "ipc_label": remote_sensing.get("fews_ipc_label", ""),
            }
        )

    if not snapshot:
        raise DatasetUnavailableError(
            f"No records for the latest date ({latest_date}) in {PRECIPITATION_FILE}"
        )
    return latest_date, snapshot


def build_alerts(snapshot: list[dict[str, Any]]) -> list[dict[str, Any]]:
    alerts = []
    for record in snapshot:
        spi_3m = record["spi_3m"]
        vci = record["vci"]

        if spi_3m is not None and spi_3m <= -2:
            severity = "critical"
        elif spi_3m is not None and spi_3m <= -1.5:
            severity = "high"
        elif spi_3m is not None and spi_3m <= -1:
            severity = "medium"
        elif vci is not None and vci <= 20:
            severity = "high"
        elif vci is not None and vci <= 35:
            severity = "medium"
        else:
            continue

        alerts.append(
            {
                **record,
                "id": record["woreda_id"],
                "type": "drought",
                "severity": severity,
                "message": (
                    f"{record['drought_hazard_category'] or 'Drought stress'} "
                    f"indicated for {record['woreda_name']}."
                ),
            }
        )
    return sorted(
        alerts,
        key=lambda alert: (
            {"critical": 0, "high": 1, "medium": 2}.get(alert["severity"], 3),
            alert["woreda_name"],
        ),
    )
