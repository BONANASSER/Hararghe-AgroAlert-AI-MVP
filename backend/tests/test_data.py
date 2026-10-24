import unittest

from app.data import build_alerts, get_latest_snapshot


class DroughtDataTests(unittest.TestCase):
    def test_latest_snapshot_joins_precipitation_and_remote_sensing(self):
        date, snapshot = get_latest_snapshot()

        self.assertEqual(date, "2026-10-01")
        self.assertEqual(len(snapshot), 41)
        self.assertTrue(all(record["spi_3m"] is not None for record in snapshot))
        self.assertTrue(all(record["vci"] is not None for record in snapshot))

    def test_alerts_sort_by_severity_and_ignore_records_without_thresholds(self):
        snapshot = [
            {
                "woreda_id": "1",
                "woreda_name": "Mieso",
                "zone_name": "West Hararge",
                "spi_3m": -2.1,
                "vci": 40,
                "drought_hazard_category": "Extreme Drought",
            },
            {
                "woreda_id": "2",
                "woreda_name": "Chiro",
                "zone_name": "West Hararge",
                "spi_3m": -1.2,
                "vci": 45,
                "drought_hazard_category": "Moderate Drought",
            },
            {
                "woreda_id": "3",
                "woreda_name": "Kersa",
                "zone_name": "East Hararge",
                "spi_3m": 0.2,
                "vci": 60,
                "drought_hazard_category": "Near Normal",
            },
        ]

        alerts = build_alerts(snapshot)

        self.assertEqual([alert["severity"] for alert in alerts], ["critical", "medium"])
        self.assertEqual([alert["woreda_name"] for alert in alerts], ["Mieso", "Chiro"])


if __name__ == "__main__":
    unittest.main()
