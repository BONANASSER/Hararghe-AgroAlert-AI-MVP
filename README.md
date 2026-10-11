# Hararghe AgroAlert AI MVP

A full-stack MVP for agricultural monitoring and alerting in Hararghe region.

## Architecture

- Backend: FastAPI API
- Web frontend: React + Vite + TypeScript
- Mobile app: Expo React Native
- Database: PostgreSQL
- Optional messaging/AI integration for crop disease detection and alerts

## Repository structure

```text
Hararghe-AgroAlert-AI-MVP/
├── backend/
│   ├── app/
│   ├── .env.example
│   ├── requirements.txt
│   └── README.md
├── frontend-web/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── .gitignore
├── frontend-mobile/
│   ├── App.tsx
│   ├── app.json
│   ├── package.json
│   ├── tsconfig.json
│   └── .gitignore
├── docker-compose.yml
├── .gitignore
├── README.md
└── docs/
    └── SETUP.md
```

## Quick start

### 1) Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API docs: http://localhost:8000/docs

### 2) Web frontend

```bash
cd frontend-web
npm install
npm run dev
```

### 3) Mobile app

```bash
cd frontend-mobile
npm install
npx expo start
```

### 4) Database with Docker

```bash
docker compose up -d postgres
```

## Default API

- GET /api/health
- GET /api/alerts
- GET /api/dashboard

## Notes

This repository is intentionally scaffolded to give you a working base for a production-ready MVP. You can extend it with:

- farmer profiles
- crop disease detection
- weather and soil alerts
- push notifications
- admin dashboard
- multilingual UI
- AI prediction pipeline

## License

This project is currently scaffolded for internal MVP development.
