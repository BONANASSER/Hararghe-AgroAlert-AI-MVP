"""
boundaries.py
Official Administrative and Agro-Ecological Boundary Registry for
Eastern and Western Hararghe Zones, Oromia Regional State, Ethiopia.

Parsed directly from official ET_Admin3_2023 shapefiles.
Encompasses all 41 woredas across East Hararge (24) and West Hararge (17).
"""

import os
import csv
from pathlib import Path
from typing import List, Dict, Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BOUNDARIES_DIR = PROJECT_ROOT / "data" / "boundaries"
CATALOG_CSV = BOUNDARIES_DIR / "hararghe_zones_woredas.csv"
GEOJSON_PATH = BOUNDARIES_DIR / "hararghe_zones_woredas.geojson"


def load_hararghe_woredas() -> List[Dict[str, Any]]:
    """Loads all 41 woredas across East and West Hararge."""
    if not CATALOG_CSV.exists():
        raise FileNotFoundError(f"Boundary catalog missing: {CATALOG_CSV}. Run extract_official_boundaries.py first.")
    woredas = []
    with CATALOG_CSV.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["centroid_lat"] = float(row["centroid_lat"])
            row["centroid_lon"] = float(row["centroid_lon"])
            row["min_lat"] = float(row["min_lat"])
            row["max_lat"] = float(row["max_lat"])
            row["min_lon"] = float(row["min_lon"])
            row["max_lon"] = float(row["max_lon"])
            row["elevation_m"] = int(row["elevation_m"])
            woredas.append(row)
    return woredas

HARARGHE_WOREDAS = load_hararghe_woredas()
EAST_HARARGHE_WOREDAS = [w for w in HARARGHE_WOREDAS if "East" in w["zone_name"]]
WEST_HARARGHE_WOREDAS = [w for w in HARARGHE_WOREDAS if "West" in w["zone_name"]]

# Backwards compatibility alias
EASTERN_HARARGHE_WOREDAS = EAST_HARARGHE_WOREDAS
WESTERN_HARARGHE_WOREDAS = WEST_HARARGHE_WOREDAS

if __name__ == "__main__":
    print(f"[BOUNDARIES] Loaded {len(HARARGHE_WOREDAS)} total woredas.")
    print(f"  • East Hararge: {len(EAST_HARARGHE_WOREDAS)} woredas")
    print(f"  • West Hararge: {len(WEST_HARARGHE_WOREDAS)} woredas")
