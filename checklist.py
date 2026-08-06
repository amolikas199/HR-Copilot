"""
checklist.py  —  Module 2 engine: generate an onboarding checklist.

It reuses the same database (db) and LLM (llm) from rag.py — no need to
load the embedding model or LLM again. It retrieves onboarding-related
chunks and asks the LLM to turn them into a clean, actionable checklist.
"""

from langchain_core.prompts import ChatPromptTemplate
from rag import db, llm   # reuse the already-loaded vector store and LLM

# A broad query to pull in the onboarding-relevant parts of the documents.
ONBOARDING_QUERY = (
    "new employee onboarding: documents to submit, forms, ID proofs, "
    "trainings, orientation, accounts and equipment setup, first-day tasks"
)

CHECKLIST_PROMPT = ChatPromptTemplate.from_template(
    """You are an HR onboarding assistant.
Using ONLY the context below, create an onboarding checklist for a new employee.

Rules:
- Output ONLY the checklist, with no introduction or closing remarks.
- Use markdown checkboxes, one item per line, like: "- [ ] Submit ID proof".
- Keep each item short and actionable.
- If the context has no onboarding details, reply exactly: "No onboarding details found in the documents."

Context:
{context}

Checklist:"""
)


def generate_checklist():
    """Retrieve onboarding chunks and produce a checklist grounded in the documents."""
    # Pull a few more chunks than usual, since a checklist spans several topics.
    docs = db.similarity_search(ONBOARDING_QUERY, k=6)
    context = "\n\n".join(doc.page_content for doc in docs)

    message = CHECKLIST_PROMPT.format(context=context)
    response = llm.invoke(message)
    return response.content
