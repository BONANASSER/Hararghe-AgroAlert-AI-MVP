from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Hararghe AgroAlert AI API",
    version="0.1.0",
    description="Backend API for agricultural monitoring and AI alerts.",
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
    return {
        "status": "ok",
        "service": "hararghe-agroalert-backend",
        "message": "Backend is running successfully.",
    }

@app.get("/api/alerts")
def list_alerts():
    return {
        "alerts": [
            {
                "id": 1,
                "type": "pest",
                "location": "Chercher",
                "severity": "high",
                "message": "Potential pest activity detected near irrigation zone.",
            },
            {
                "id": 2,
                "type": "drought",
                "location": "Mieso",
                "severity": "medium",
                "message": "Low soil moisture trend observed over the last 5 days.",
            },
        ]
    }

@app.get("/api/dashboard")
def dashboard_summary():
    return {
        "region": "Hararghe",
        "farmers_monitored": 1280,
        "active_alerts": 14,
        "weather_risk_index": 68,
        "ai_predictions": 9,
    }
