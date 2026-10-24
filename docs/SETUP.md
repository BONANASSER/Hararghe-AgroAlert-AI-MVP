# Setup

See the root [README](../README.md) for the Windows run instructions,
API endpoints, frontend setup, and required synthetic-data disclaimer.

The API expects these project-relative input files:

- `data/chirps/hararghe_zones_chirps_monthly_1990_2026.csv`
- `data/nasa/hararghe_zones_remote_sensing_1990_2026.csv`

Set `AGROALERT_DATA_DIR` to override their common parent directory. Missing
datasets return HTTP 503 from data endpoints; the health endpoint reports
`data_status: unavailable`.
