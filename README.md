# HR Copilot

An AI-powered HR assistant with 6 modules for knowledge Q&A, onboarding, leave requests, policy comparison, escalation tracking, and feedback analytics. Uses RAG with LangChain, ChromaDB, and Groq LLM.

**[Live Demo on Streamlit Cloud](#deployment)** | **[GitHub](https://github.com/amolikas199/HR-Copilot)**

## 🎯 Features

- **📚 Knowledge Assistant** — Semantic search over HR documents with source citations and confidence scores
- **🧭 Onboarding Assistant** — Generate personalized onboarding checklists
- **📝 Leave Request** — Convert plain English to structured leave requests
- **📋 Policy Comparison** — Compare old and new policy versions to detect changes
- **🚨 Escalation Tickets** — Auto-escalate low-confidence queries for HR review (persists in MongoDB)
- **⭐ Feedback Analytics** — Track answer quality metrics with real-time persistence

## 🛠 Tech Stack

**Frontend:** Streamlit (dark mode UI + login auth)  
**LLM & RAG:** LangChain, Groq API, HuggingFace embeddings  
**Vector DB:** ChromaDB  
**Data Persistence:** MongoDB Atlas  
**Deployment:** Streamlit Cloud  

## 📊 Architecture

```
┌──────────────────────────────────────────────┐
│      Streamlit Cloud (All-in-One)            │
│  ┌─────────────────────────────────────────┐ │
│  │  Frontend (Dark Mode UI + Login)        │ │
│  │  6 Modules (Knowledge | Onboarding | ...) │
│  └──────────────────┬──────────────────────┘ │
│                     │                        │
│  ┌──────────────────▼──────────────────────┐ │
│  │  RAG Pipeline (LangChain)               │ │
│  │  ChromaDB + HuggingFace Embeddings      │ │
│  └──────────────────┬──────────────────────┘ │
│                     │                        │
│     ┌───────────────┼───────────────┐        │
│     ▼               ▼               ▼        │
│  Groq LLM     MongoDB Atlas   HuggingFace   │
│  (LLM)        (Persistence)   (Embeddings)  │
└──────────────────────────────────────────────┘
```

## 📋 Modules

| Module | Status | Description |
|--------|--------|-------------|
| **Knowledge Assistant** | ✅ | RAG Q&A with semantic search & source attribution |
| **Onboarding Assistant** | ✅ | Document-grounded checklist generation |
| **Leave Request** | ✅ | NLP extraction → structured JSON |
| **Policy Comparison** | ✅ | Detects added/removed/modified sections |
| **Escalation Engine** | ✅ | Routes low-confidence queries to HR (MongoDB persistence) |
| **Feedback Loop** | ✅ | Tracks helpful/unhelpful ratings with analytics (MongoDB persistence) |

## 🚀 Deployment (Streamlit Cloud)

1. **Create Streamlit Cloud account** at [streamlit.io](https://streamlit.io)
2. **Connect GitHub repo** → `amolikas199/HR-Copilot`
3. **Add secrets** (Settings → Secrets):
   ```
   GROQ_API_KEY = "your_groq_api_key"
   MONGO_URI = "mongodb+srv://username:password@cluster.mongodb.net/hr_copilot?retryWrites=true&w=majority"
   ```
4. **Deploy** — Live in seconds!

**Login credentials:** `hr_admin` / `demo123`

## 💻 Local Development

```bash
git clone https://github.com/amolikas199/HR-Copilot.git
cd "HR copilot"

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Add GROQ_API_KEY and MONGO_URI to .env

streamlit run app.py
```

Opens at `http://localhost:8501`

## 🔑 Key Features

✨ **Dark Mode UI** — Modern gradient theme with professional navigation  
🔐 **Login Auth** — Demo user authentication  
🧠 **Confidence Scoring** — Know when the AI is uncertain  
📚 **Source Attribution** — Every answer cites the source document  
💾 **Real-Time Persistence** — MongoDB integration for escalations & feedback  
📊 **Analytics Dashboard** — Track feedback & escalation metrics  

## 📝 Usage Examples

**Knowledge Assistant**
```
Q: How many vacation days do I get?
A: [Answer from handbook with confidence: 87% and source page]
```

**Escalation System**
```
- Low confidence answer (< 50%) → Auto-escalate to HR team
- Data persists in MongoDB Atlas
- View all escalations in real-time dashboard
```

**Feedback Analytics**
```
- Users rate answers (helpful/unhelpful)
- Tracks helpful ratio, total feedback, trends
- All data persists across app restarts
```

## 📦 Requirements

- Python 3.9+
- Groq API key (free tier: [groq.com](https://groq.com))
- MongoDB Atlas account (free tier available)
- GitHub repo for Streamlit Cloud deployment

## 🎓 Design Highlights

- **Privacy:** Uses local embeddings (HuggingFace) — no data sent to external APIs
- **Reliability:** Confidence thresholds prevent hallucinations
- **Persistence:** MongoDB Atlas ensures data survives app restarts
- **User Experience:** Dark mode, instant feedback, intuitive navigation

## 📄 License

MIT

## 👤 Author

Amolika Singh | [GitHub](https://github.com/amolikas199)
