# Hararghe AgroAlert + Multimodal Drought Research

This workspace combines the Hararghe AgroAlert web/mobile MVP with the local
multimodal drought research pipeline. The FastAPI backend reads the project's
monthly precipitation and remote-sensing CSVs and serves a current-in-dataset
summary, woreda-level records, and rule-based drought alerts to both apps.

## Important data limitation

The current full-Hararghe precipitation and remote-sensing CSVs are generated
by prototype scripts. They are **synthetic demonstration data**, not verified
CHIRPS, MODIS, SMAP, or FEWS NET observations, and are not live forecasts or
field advisories. The UI and API identify this limitation. Do not use the
alerts for operational or humanitarian decisions.

## Project structure

- `backend/`: FastAPI API, including the local CSV data adapter
- `frontend-web/`: React + Vite dashboard
- `frontend-mobile/`: Expo field-app prototype
- `preprocessing/`: drought and multimodal data pipeline
- `data/`: research datasets, boundaries, and provenance manifest
- `models/`, `notebooks/`, `results/`, `manuscripts/`: research artifacts

## Run locally (Windows PowerShell)

### 1. Start the API

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API uses the repository's `data/` directory by default. To use another
directory, set `AGROALERT_DATA_DIR` to a directory containing `chirps/` and
`nasa/` subdirectories.

### 2. Start the web dashboard

In another terminal:

```powershell
cd frontend-web
npm install
npm run dev
```

Open http://localhost:5173. Vite proxies `/api` requests to the backend on
port 8000.

### 3. Start the mobile app (optional)

```powershell
cd frontend-mobile
npm install
$env:EXPO_PUBLIC_API_URL = "http://YOUR_COMPUTER_LAN_IP:8000"
npx expo start
```

Set the API URL to your computer's LAN address when testing on a physical
phone. Android emulators can use `http://10.0.2.2:8000`; iOS simulators can
use `http://localhost:8000`.

## API

- `GET /api/health` — service and dataset availability
- `GET /api/dashboard` — latest-month regional metrics
- `GET /api/alerts` — rule-based drought threshold alerts
- `GET /api/woredas` — latest-month metrics by woreda

Alert thresholds are based on SPI-3 and VCI values in the supplied dataset.
They are demonstration rules, not a validated forecasting model.
