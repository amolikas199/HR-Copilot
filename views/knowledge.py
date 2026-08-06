import streamlit as st
from rag import ask
from ui_utils import show_answer
import escalation
import feedback

st.markdown("""
<style>
    .question-input {
        border-radius: 8px;
        border: 2px solid #2d3748;
        background: #1a1f2e;
        padding: 12px;
    }

    .example-btn {
        background: linear-gradient(135deg, #2d3748 0%, #1a1f2e 100%);
        border: 2px solid #2d3748;
        border-radius: 8px;
        padding: 12px;
        color: #94a3b8;
        transition: all 0.3s ease;
    }

    .example-btn:hover {
        border-color: #60a5fa;
        color: #60a5fa;
    }
</style>
""", unsafe_allow_html=True)

st.title("📚 Knowledge Assistant")
st.markdown("Ask HR policy questions and get answers with source citations and confidence scores.")

EXAMPLES = [
    "How many vacation days do I get?",
    "What is the resignation notice period?",
]

st.markdown("**Quick Examples** — Click any to try:", unsafe_allow_html=True)
picked = None
cols = st.columns(len(EXAMPLES))
for col, example in zip(cols, EXAMPLES):
    if col.button(example, use_container_width=True, key=f"kb_ex_{example}"):
        picked = example

st.divider()

with st.form("kb_form"):
    typed = st.text_input("Your question:", placeholder="e.g. How many vacation days do I get?")
    col1, col2 = st.columns([8, 2])
    with col2:
        submitted = st.form_submit_button("🔍 Ask", use_container_width=True, type="primary")

question = picked or (typed if submitted else None)

if question:
    try:
        with st.spinner("🔎 Searching documents..."):
            result = ask(question)
    except Exception:
        st.error("Something went wrong. Please try again.")
        st.stop()
    show_answer(result)

    st.divider()
    st.subheader("📊 Was this helpful?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Yes, helpful", use_container_width=True):
            feedback.save_feedback(question, result["answer"], result["chunks"], "helpful")
            st.success("✓ Thank you for your feedback!")

    with col2:
        if st.button("👎 No, not helpful", use_container_width=True):
            feedback.save_feedback(question, result["answer"], result["chunks"], "unhelpful")
            escalation.escalate_query(question, result["confidence"], result["answer"])
            st.warning("⚠️ Escalated to HR team for review.")
