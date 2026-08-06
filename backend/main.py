from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import date
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

app = FastAPI(title="HR Copilot API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5", encode_kwargs={"normalize_embeddings": True})
db = Chroma(persist_directory="../chroma_db", embedding_function=embeddings)
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

class Question(BaseModel):
    question: str

class LeaveRequest(BaseModel):
    sentence: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(q: Question):
    results = db.similarity_search_with_score(q.question, k=4)
    docs = [doc for doc, _ in results]
    scores = [score for _, score in results]

    context = "\n\n".join([f"[{os.path.basename(doc.metadata.get('source', 'unknown'))}, page {doc.metadata.get('page', '?')}]\n{doc.page_content}" for doc in docs])
    prompt = ChatPromptTemplate.from_template("Answer using ONLY this context. If not found, say: 'I couldn't find this in HR documents.'\n\nContext:\n{context}\n\nQ: {question}\n\nA:")
    message = prompt.format(context=context, question=q.question)
    response = llm.invoke(message)

    confidence = round(max(0.0, 1.0 - min(scores)) * 100) if scores else 0
    return {"answer": response.content, "confidence": confidence, "sources": [(os.path.basename(d.metadata.get("source", "unknown")), d.metadata.get("page", "?")) for d in docs]}

@app.post("/checklist")
def checklist():
    query = "new employee onboarding: documents to submit, forms, ID proofs, trainings, orientation, accounts and equipment setup"
    docs = db.similarity_search(query, k=6)
    context = "\n\n".join(doc.page_content for doc in docs)
    prompt = ChatPromptTemplate.from_template("Create onboarding checklist from context. Output markdown checkboxes only.\n\nContext:\n{context}\n\nChecklist:")
    message = prompt.format(context=context)
    response = llm.invoke(message)
    return {"checklist": response.content}

@app.post("/extract-leave")
def extract_leave(req: LeaveRequest):
    from pydantic import BaseModel, Field

    class LeaveData(BaseModel):
        leave_type: str = Field(description="One of: Sick Leave, Casual Leave, Earned Leave, Maternity Leave, Paternity Leave, Unpaid Leave, Bereavement Leave, Work From Home")
        start_date: str = Field(description="YYYY-MM-DD")
        end_date: str = Field(description="YYYY-MM-DD")
        reason: str = Field(description="Short reason or 'Not specified'")

    extractor = llm.with_structured_output(LeaveData)
    today = date.today().isoformat()
    prompt = ChatPromptTemplate.from_template("Extract leave details. Today: {today}\n\nEmployee: {sentence}")
    message = prompt.format(today=today, sentence=req.sentence)
    result = extractor.invoke(message)
    data = result.model_dump()

    try:
        start = date.fromisoformat(data["start_date"])
        end = date.fromisoformat(data["end_date"])
        data["total_days"] = (end - start).days + 1
    except:
        data["total_days"] = None

    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
