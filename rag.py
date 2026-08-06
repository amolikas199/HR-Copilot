"""
rag.py  —  Module 1, Step 2: the core question-answering engine.

This loads the Chroma database we built with ingest.py, retrieves the most
relevant chunks for a question, and asks the Groq LLM to answer using ONLY
those chunks (so it can't make things up). It returns the answer, the
sources, and a rough confidence score.
"""

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()  # reads GROQ_API_KEY from the .env file

# --- Settings ---
DB_DIR = "chroma_db"
EMBED_MODEL = "BAAI/bge-small-en-v1.5"
LLM_MODEL = "llama-3.3-70b-versatile"   # a fast, capable model on Groq
TOP_K = 4                                # how many chunks to retrieve per question

# --- Load the pieces once, when this module is imported ---
embeddings = HuggingFaceEmbeddings(
    model_name=EMBED_MODEL,
    encode_kwargs={"normalize_embeddings": True},
)
db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
llm = ChatGroq(model=LLM_MODEL, temperature=0)   # temperature=0 = focused, consistent answers

# --- The prompt: the rules we give the LLM ---
PROMPT = ChatPromptTemplate.from_template(
    """You are a helpful HR assistant for employees.
Answer the question using ONLY the context below.
If the answer is not in the context, say: "I couldn't find this in the HR documents. Please contact HR."
Do not make up information. Keep the answer clear and concise.

Context:
{context}

Question: {question}

Answer:"""
)


def _format_context(docs):
    """Join the retrieved chunks into one text block, labelled with their source."""
    blocks = []
    for doc in docs:
        src = os.path.basename(doc.metadata.get("source", "unknown"))
        page = doc.metadata.get("page", "?")
        blocks.append(f"[Source: {src}, page {page}]\n{doc.page_content}")
    return "\n\n".join(blocks)


def _confidence_from_scores(scores):
    """Confidence (0-100) based on the best-matching chunk.
    With COSINE distance, Chroma returns (1 - cosine_similarity), so
    (1 - distance) gives back the true cosine similarity directly."""
    if not scores:
        return 0
    best = min(scores)                 # smallest distance = closest match
    confidence = max(0.0, 1.0 - best)  # = cosine similarity of the best chunk
    return round(confidence * 100)


def _confidence_label(confidence):
    """Turn the number into a human-friendly label."""
    if confidence >= 70:
        return "High"
    elif confidence >= 50:
        return "Medium"
    else:
        return "Low"


def ask(question):
    """Answer one question. Returns a dict: answer, sources, confidence."""
    # 1. retrieve
    results = db.similarity_search_with_score(question, k=TOP_K)
    docs = [doc for doc, score in results]
    scores = [score for doc, score in results]

    # 2. build the prompt and call the LLM
    context = _format_context(docs)
    message = PROMPT.format(context=context, question=question)
    response = llm.invoke(message)

    # 3. collect the retrieved chunks: their source (file + page) AND the text,
    #    so the UI can show the exact passage the answer is grounded in.
    chunks = []
    for doc in docs:
        chunks.append({
            "source": os.path.basename(doc.metadata.get("source", "unknown")),
            "page": doc.metadata.get("page", "?"),
            "text": doc.page_content,
        })

    confidence = _confidence_from_scores(scores)
    return {
        "answer": response.content,
        "chunks": chunks,
        "confidence": confidence,
        "confidence_label": _confidence_label(confidence),
    }


# Quick console test:  .venv/Scripts/python.exe rag.py
if __name__ == "__main__":
    result = ask("How many vacation days do employees get?")
    print("ANSWER:\n", result["answer"])
    print("\nCONFIDENCE:", result["confidence"], "% ->", result["confidence_label"])
    print("SOURCES:", [(c["source"], c["page"]) for c in result["chunks"]])
