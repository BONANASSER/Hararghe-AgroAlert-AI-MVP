from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.data import DatasetUnavailableError, build_alerts, get_latest_snapshot

app = FastAPI(
    title="Hararghe AgroAlert AI API",
    version="0.1.0",
    description="Prototype drought monitoring API using the project research datasets.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    try:
        latest_date, _ = get_latest_snapshot()
        data_status = "available"
    except DatasetUnavailableError:
        latest_date = None
        data_status = "unavailable"
    return {
        "status": "ok",
        "service": "hararghe-agroalert-backend",
        "message": "Backend is running successfully.",
        "data_status": data_status,
        "data_as_of": latest_date,
        "data_is_synthetic": True,
    }


@app.get("/api/alerts")
def list_alerts():
    try:
        _, snapshot = get_latest_snapshot()
    except DatasetUnavailableError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error
    return {"alerts": build_alerts(snapshot), "data_is_synthetic": True}


@app.get("/api/dashboard")
def dashboard_summary():
    try:
        latest_date, snapshot = get_latest_snapshot()
    except DatasetUnavailableError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error

    alerts = build_alerts(snapshot)
    spi_values = [record["spi_3m"] for record in snapshot if record["spi_3m"] is not None]
    vci_values = [record["vci"] for record in snapshot if record["vci"] is not None]
    return {
        "region": "Hararghe",
        "woredas_monitored": len(snapshot),
        "active_alerts": len(alerts),
        "average_spi_3m": round(sum(spi_values) / len(spi_values), 2) if spi_values else None,
        "average_vci": round(sum(vci_values) / len(vci_values), 1) if vci_values else None,
        "data_as_of": latest_date,
        "data_is_synthetic": True,
    }


@app.get("/api/woredas")
def list_woredas():
    try:
        _, snapshot = get_latest_snapshot()
    except DatasetUnavailableError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error
    return {"woredas": snapshot, "data_is_synthetic": True}
