"""
views/knowledge.py  —  Module 1 page: the Knowledge Assistant.
"""

import streamlit as st
from rag import ask
from ui_utils import show_answer

st.title("📚 Knowledge Assistant")
st.caption("Ask a question about company HR policies. Answers come only from the HR documents.")

EXAMPLES = [
    "How many vacation days do I get?",
    "What is the resignation notice period?",
]

# Clickable example questions — clicking one runs it immediately.
picked = None
cols = st.columns(len(EXAMPLES))
for col, example in zip(cols, EXAMPLES):
    if col.button(example, key=f"kb_ex_{example}"):
        picked = example

with st.form("kb_form"):
    typed = st.text_input("Your question:", placeholder="e.g. How many vacation days do I get?")
    submitted = st.form_submit_button("Ask", type="primary")

# The active question is either a clicked example or the typed+submitted text.
question = picked or (typed if submitted else None)

if question:
    try:
        with st.spinner("Searching the HR documents..."):
            result = ask(question)
    except Exception:
        st.error("Something went wrong while answering. Please try again.")
        st.stop()
    show_answer(result)
