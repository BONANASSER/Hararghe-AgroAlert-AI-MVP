# AgroAlert API

FastAPI serves the current-month regional summary, rule-based drought alerts,
and per-woreda metrics from the project's `data/chirps/` and `data/nasa/`
datasets. See the root README for setup instructions and the synthetic-data
limitations.

Run from this directory after installing `requirements.txt`:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
