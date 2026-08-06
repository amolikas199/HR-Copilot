"""
views/knowledge.py  —  Module 1 page: the Knowledge Assistant.
"""

import streamlit as st
from rag import ask
from ui_utils import show_answer
import escalation
import feedback

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

    st.divider()
    st.subheader("Was this answer helpful?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Yes, helpful"):
            feedback.save_feedback(question, result["answer"], result["chunks"], "helpful")
            st.success("Thank you for your feedback!")

    with col2:
        if st.button("👎 No, not helpful"):
            feedback.save_feedback(question, result["answer"], result["chunks"], "unhelpful")
            escalation.escalate_query(question, result["confidence"], result["answer"])
            st.warning("Your feedback has been escalated to HR. Thank you!")
