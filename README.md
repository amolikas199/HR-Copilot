# HR Copilot

An AI-powered HR assistant that answers policy questions, guides employee onboarding, and processes leave requests using retrieval-augmented generation (RAG) over company HR documents.

**[Live Demo](#deployment)** | **[GitHub](https://github.com/amolikas199/HR-Copilot)**

## Features

- **📚 Knowledge Assistant** — Ask questions about your HR policies. Answers are grounded in documents with source citations and confidence scores.
- **🧭 Onboarding Assistant** — Auto-generate onboarding checklists from company documents.
- **📝 Leave Request Intelligence** — Convert plain English to structured leave requests (JSON).

## Tech Stack

**Backend:** FastAPI, Python, LangChain, Groq LLM  
**Frontend:** React, Axios  
**Database:** ChromaDB (vector) + HuggingFace embeddings  
**Deployment:** Render (API) + Vercel (frontend)

## Architecture

```
┌─────────────────────────────────────────────┐
│         React Frontend (Vercel)             │
│  (Knowledge | Onboarding | Leave Request)   │
└────────────────┬────────────────────────────┘
                 │ HTTP/REST
┌────────────────▼────────────────────────────┐
│      FastAPI Backend (Render)               │
│  /ask  /checklist  /extract-leave           │
└────────────────┬────────────────────────────┘
                 │
    ┌────────────┼────────────┐
    ▼            ▼            ▼
ChromaDB    Groq API   HuggingFace
(Vector DB) (LLM)      (Embeddings)
```

## Project Modules

| Module | Status | Description |
|--------|--------|-------------|
| **Knowledge Assistant** | ✅ Done | RAG-based Q&A with semantic search |
| **Onboarding Checklist** | ✅ Done | Document-grounded checklist generation |
| **Leave Request Extractor** | ✅ Done | Natural language → structured JSON |
| **Policy Comparison Engine** | 🔄 In Progress | Detects changes between policy versions |

## Setup & Local Development

### Prerequisites
- Python 3.9+, Node 16+
- Groq API key (free at [groq.com](https://groq.com))

### Installation

```bash
git clone https://github.com/amolikas199/HR-Copilot.git
cd HR-Copilot

# Backend setup
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Add your GROQ_API_KEY to .env

# Build vector database (run once)
python ../ingest.py

# Start backend (from backend/ dir)
uvicorn main:app --reload

# Frontend setup (in new terminal)
cd frontend
npm install
npm start
```

Backend runs on `http://localhost:8000`, Frontend on `http://localhost:3000`

## Usage Examples

### Knowledge Assistant
**Q:** "How many casual leaves do I get per year?"  
**A:** [Answers from your handbook with page citations and confidence score]

### Onboarding Checklist
Generates a markdown checklist of all onboarding requirements from your documents.

### Leave Request
**Input:** "I need leave from 12th to 16th for medical reasons"  
**Output:**
```json
{
  "leave_type": "Sick Leave",
  "start_date": "2026-07-12",
  "end_date": "2026-07-16",
  "reason": "Medical",
  "total_days": 5
}
```

## Key Design Decisions

- **Local Embeddings:** Uses HuggingFace embeddings to keep data private (no external API calls)
- **Confidence Scoring:** Returns cosine similarity scores so users know how confident the system is
- **Source Attribution:** Every answer cites the specific document and page it came from
- **Structured Output:** Leave requests are extracted as JSON using LangChain's structured output

## Deployment

### Backend (Render)
1. Push to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Select GitHub repo → Choose `backend` folder
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port 8000`
5. Add env var: `GROQ_API_KEY=your_key`
6. Deploy

Get your backend URL (e.g., `https://hr-copilot-api.onrender.com`)

### Frontend (Vercel)
1. Go to [vercel.com](https://vercel.com) → Import Project
2. Select GitHub repo → Choose `frontend` folder
3. Add env var: `REACT_APP_API_URL=https://your-backend-url`
4. Deploy

Live: `https://hr-copilot.vercel.app`

## API Endpoints

- `POST /ask` — Answer HR question
- `POST /checklist` — Generate onboarding checklist
- `POST /extract-leave` — Extract structured leave request
- `GET /health` — Health check

## Future Enhancements

- Policy Comparison Engine
- Escalation System (route to HR)
- User feedback loop

## License

MIT

## Author

Amolika Singh | [GitHub](https://github.com/amolikas199) | [LinkedIn](https://linkedin.com/in/amolikas199)
