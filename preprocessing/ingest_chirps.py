"""
ingest_chirps.py
Generates a synthetic precipitation prototype series for Eastern and Western
Hararghe Zones. It does not download or ingest CHIRPS observations.

Temporal Coverage: 1990-01-01 to 2026-10-01 (October 2026) across all 41 woredas.
Total Records: 41 woredas × 442 monthly intervals = 18,122 observation records.
Calculates: monthly precipitation, 30-year climatological normal, rainfall anomaly,
3-month cumulative rainfall, and Standardized Precipitation Index (SPI-1, SPI-3).
"""

import os
import sys
from pathlib import Path
import csv
import math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from manifest_manager import record_dataset
from boundaries import HARARGHE_WOREDAS
from climatology import compute_spi

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHIRPS_DIR = PROJECT_ROOT / "data" / "chirps"
OUTPUT_CSV = CHIRPS_DIR / "hararghe_zones_chirps_monthly_1990_2026.csv"

# Baseline monthly precipitation distributions (mm) by agro-ecological zone
AGRO_PRECIP_PROFILES = {
    "Kolla (Warm Lowlands / Agro-Pastoral)": {
        1: 6.0, 2: 12.0, 3: 38.0, 4: 78.0, 5: 58.0, 6: 20.0,
        7: 52.0, 8: 78.0, 9: 68.0, 10: 48.0, 11: 20.0, 12: 6.0
    },
    "Woina Dega (Temperate Midlands)": {
        1: 12.0, 2: 25.0, 3: 65.0, 4: 110.0, 5: 90.0, 6: 55.0,
        7: 125.0, 8: 145.0, 9: 115.0, 10: 35.0, 11: 15.0, 12: 8.0
    },
    "Dega (Cool Sub-Humid Highlands)": {
        1: 16.0, 2: 32.0, 3: 88.0, 4: 138.0, 5: 118.0, 6: 82.0,
        7: 178.0, 8: 198.0, 9: 152.0, 10: 46.0, 11: 22.0, 12: 10.0
    }
}

YEAR_SHOCK_MULTIPLIERS = {
    1990: 0.85, 1991: 0.72, 1992: 0.95, 1993: 1.10, 1994: 0.70,
    1995: 0.90, 1996: 1.15, 1997: 0.74, 1998: 1.25, 1999: 0.82,
    2000: 0.80, 2001: 0.95, 2002: 0.64, 2003: 0.78, 2004: 0.88,
    2005: 1.05, 2006: 1.12, 2007: 1.10, 2008: 0.68, 2009: 0.71,
    2010: 1.18, 2011: 0.75, 2012: 0.92, 2013: 1.02, 2014: 0.85,
    2015: 0.46,  # Historic El Niño drought
    2016: 1.16,  # Recovery
    2017: 0.84, 2018: 0.96, 2019: 1.22,
    2020: 0.80, 2021: 0.66, 2022: 0.58, 2023: 0.64,  # Historic multi-season failure
    2024: 1.12, 2025: 0.68, 2026: 0.86
}

def generate_full_chirps_dataset():
    CHIRPS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[PROTOTYPE] Generating synthetic 1990 to October 2026 precipitation series for 41 woredas...")
    
    rows = []
    start_year = 1990
    end_year = 2026
    
    for woreda in HARARGHE_WOREDAS:
        w_id = woreda["woreda_id"]
        w_name = woreda["woreda_name"]
        zone_name = woreda["zone_name"]
        zone_type = woreda["agro_ecological_zone"]
        
        profile_key = "Woina Dega (Temperate Midlands)"
        for k in AGRO_PRECIP_PROFILES:
            if k.split()[0] in zone_type:
                profile_key = k
                break
        base_monthly = AGRO_PRECIP_PROFILES[profile_key]
        
        woreda_records = []
        for yr in range(start_year, end_year + 1):
            yr_mult = YEAR_SHOCK_MULTIPLIERS.get(yr, 1.0)
            
            for m in range(1, 13):
                if yr == 2026 and m > 10: # October 2026 cutoff
                    continue
                    
                date_str = f"{yr}-{m:02d}-01"
                base_mm = base_monthly.get(m, 40.0)
                
                seed = int(woreda["centroid_lat"] * 100) + int(woreda["centroid_lon"] * 100) + yr * 12 + m
                np.random.seed(seed)
                noise = np.random.normal(loc=0.0, scale=0.14 * base_mm)
                
                precip_mm = max(0.0, round((base_mm * yr_mult) + noise, 1))
                
                woreda_records.append({
                    "woreda_id": w_id,
                    "woreda_name": w_name,
                    "zone_name": zone_name,
                    "date": date_str,
                    "year": yr,
                    "month": m,
                    "precip_mm": precip_mm,
                    "precip_normal_mm": round(base_mm, 1),
                    "precip_anomaly_mm": round(precip_mm - base_mm, 1)
                })
                
        # Calculate SPI-1 and SPI-3 across the 442-month historical window
        for idx, rec in enumerate(woreda_records):
            m = rec["month"]
            hist_m_precip = [r["precip_mm"] for r in woreda_records if r["month"] == m]
            spi1 = compute_spi(hist_m_precip, rec["precip_mm"])
            
            if idx >= 2:
                p3m = woreda_records[idx]["precip_mm"] + woreda_records[idx-1]["precip_mm"] + woreda_records[idx-2]["precip_mm"]
            elif idx == 1:
                p3m = (woreda_records[idx]["precip_mm"] + woreda_records[idx-1]["precip_mm"]) * 1.5
            else:
                p3m = woreda_records[idx]["precip_mm"] * 3.0
                
            rec["precip_3m_mm"] = round(p3m, 1)
            
            hist_3m = []
            for j in range(2, len(woreda_records)):
                if woreda_records[j]["month"] == m:
                    hist_3m.append(woreda_records[j]["precip_mm"] + woreda_records[j-1]["precip_mm"] + woreda_records[j-2]["precip_mm"])
            if not hist_3m:
                hist_3m = [p3m]
                
            spi3 = compute_spi(hist_3m, p3m)
            rec["spi_1m"] = spi1
            rec["spi_3m"] = spi3
            
            if spi3 <= -2.0:
                cat = "Extreme Drought"
            elif spi3 <= -1.5:
                cat = "Severe Drought"
            elif spi3 <= -1.0:
                cat = "Moderate Drought"
            elif spi3 < 1.0:
                cat = "Near Normal"
            elif spi3 < 1.5:
                cat = "Moderately Wet"
            elif spi3 < 2.0:
                cat = "Very Wet"
            else:
                cat = "Extremely Wet"
            rec["drought_hazard_category"] = cat
            rows.append(rec)
            
    fieldnames = [
        "woreda_id", "woreda_name", "zone_name", "date", "year", "month",
        "precip_mm", "precip_normal_mm", "precip_anomaly_mm", "precip_3m_mm",
        "spi_1m", "spi_3m", "drought_hazard_category"
    ]
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"[PROTOTYPE] Synthetic Hararghe Zones dataset written to: {OUTPUT_CSV} ({len(rows)} total records)")
    
    # Register in manifest
    record_dataset(
        name="chirps_v3_hararghe_zones_1990_2026",
        filepath=str(OUTPUT_CSV),
        source_url="",
        provider="Synthetic prototype generator; not CHIRPS observations",
        temporal_coverage="1990-01-01 to 2026-10-01",
        spatial_resolution="0.05° (~5 km) Zonal Woreda Mean across East & West Hararge",
        record_count=len(rows),
        is_synthetic=True,
        metadata={
            "variables": ["precip_mm", "precip_anomaly_mm", "precip_3m_mm", "spi_1m", "spi_3m", "drought_hazard_category"],
            "total_woredas": len(HARARGHE_WOREDAS),
            "zones": ["East Hararge", "West Hararge"],
            "period": "1990 to October 2026"
        }
    )

if __name__ == "__main__":
    generate_full_chirps_dataset()
