# Deployment Guide

## Quick Deploy (10 mins)

### 1. Backend to Render

```bash
# Push to GitHub
git add .
git commit -m "Refactor to full-stack: FastAPI + React"
git push origin main
```

Go to **render.com**:
- New Web Service
- Connect GitHub repo
- Runtime: Python 3.9
- Build: `pip install -r backend/requirements.txt`
- Start: `cd backend && uvicorn main:app --host 0.0.0.0 --port 8000`
- Add env var: `GROQ_API_KEY=your_key`
- Deploy

**Note:** Copy your Render URL (e.g., `https://hr-copilot-api.onrender.com`)

### 2. Frontend to Vercel

Go to **vercel.com**:
- New Project → Import Git Repo
- Select `frontend` folder
- Add env: `REACT_APP_API_URL=https://your-render-url`
- Deploy

**Done!** Your app is live.

## Local Testing First

```bash
# Terminal 1: Backend
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Add your GROQ_API_KEY
uvicorn main:app --reload

# Terminal 2: Frontend
cd frontend
npm install
npm start
```

Open `http://localhost:3000` → Should work with local backend at `:8000`
