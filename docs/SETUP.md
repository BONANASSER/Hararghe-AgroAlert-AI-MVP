# Setup Guide

## Prerequisites

- Python 3.11+
- Node.js 18+
- npm or yarn
- Docker (optional for PostgreSQL)
- Expo CLI (for mobile)

## Install backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Install web app

```bash
cd frontend-web
npm install
npm run dev
```

## Install mobile app

```bash
cd frontend-mobile
npm install
npx expo start
```

## Recommended next steps

- Add authentication
- Connect to PostgreSQL
- Build alert CRUD API
- Add dashboard charts
- Add farmer registration and profile module
