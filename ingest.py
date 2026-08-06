"""
ingest.py  —  Module 1, Step 1: build the searchable knowledge base.

Run this ONCE (or again whenever the PDFs in data/ change):

    .venv/Scripts/python.exe ingest.py

It reads every PDF in data/, chunks the text, turns each chunk into a
vector with a local embedding model, and stores everything in Chroma
(a small database saved in the chroma_db/ folder).
"""

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os

# --- Settings we might want to tweak later, all in one place ---
DATA_DIR = "data"                       # where the PDFs live
DB_DIR = "chroma_db"                    # where the vector database gets saved
EMBED_MODEL = "BAAI/bge-small-en-v1.5"  # the local embedding model (mentor-mandated)
CHUNK_SIZE = 1000                       # ~how many characters per chunk
CHUNK_OVERLAP = 150                     # characters shared between neighbouring chunks


# ---------- STEP 1: LOAD ----------
def load_pdfs():
    """Read every PDF in data/ into a list of 'Document' objects (one per page)."""
    documents = []
    for filename in os.listdir(DATA_DIR):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(DATA_DIR, filename)
            loader = PyMuPDFLoader(path)
            pages = loader.load()          # one Document per page, with metadata
            documents.extend(pages)
            print(f"  loaded {filename}: {len(pages)} pages")
    return documents


# ---------- STEP 2: CHUNK ----------
def chunk_documents(documents):
    """Cut the page text into small overlapping pieces."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    chunks = splitter.split_documents(documents)
    return chunks


# ---------- STEPS 3 & 4: EMBED + STORE ----------
def build_vector_store(chunks):
    """Turn chunks into vectors and save them in Chroma."""
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBED_MODEL,
        encode_kwargs={"normalize_embeddings": True},  # recommended for bge models
    )
    # Chroma.from_documents does the embedding AND the saving in one call.
    # collection_metadata sets the distance metric to COSINE, which is the
    # standard choice for text embeddings and makes our confidence score
    # equal the true cosine similarity (1.0 = identical meaning).
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR,
        collection_metadata={"hnsw:space": "cosine"},
    )


def main():
    print("STEP 1 — loading PDFs...")
    documents = load_pdfs()
    print(f"  total pages loaded: {len(documents)}\n")

    print("STEP 2 — chunking...")
    chunks = chunk_documents(documents)
    print(f"  created {len(chunks)} chunks\n")

    print("STEP 3 & 4 — embedding + storing in Chroma (first run downloads the model)...")
    build_vector_store(chunks)
    print(f"\nDone! Vector database saved in '{DB_DIR}/'.")


if __name__ == "__main__":
    main()
