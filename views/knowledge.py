import streamlit as st
from rag import ask
from ui_utils import show_answer
import escalation
import feedback

st.markdown("""
<style>
    .example-pill {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        padding: 10px 16px;
        cursor: pointer;
        transition: all 0.2s ease;
        font-size: 13px;
        text-align: center;
    }

    .example-pill:hover {
        border-color: #10b981;
        background: #ecfdf5;
        color: #10b981;
    }

    .feedback-btn {
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

st.title("📚 Knowledge Assistant")
st.write("Ask questions about your company's HR policies and get instant answers with sources.")

st.divider()

EXAMPLES = [
    "How many vacation days do I get?",
    "What is the resignation notice period?",
]

st.markdown("**Quick examples:**")
picked = None
cols = st.columns(len(EXAMPLES))
for col, example in zip(cols, EXAMPLES):
    with col:
        st.markdown(f'<div class="example-pill">{example}</div>', unsafe_allow_html=True)
        if st.button("Ask", use_container_width=True, key=f"kb_ex_{example}"):
            picked = example

st.divider()

with st.form("kb_form"):
    typed = st.text_input("Your question", placeholder="e.g. What are the work-from-home policies?")
    submitted = st.form_submit_button("Search", use_container_width=True, type="primary")

question = picked or (typed if submitted else None)

if question:
    try:
        with st.spinner("Searching documents..."):
            result = ask(question)
    except Exception:
        st.error("Something went wrong. Please try again.")
        st.stop()
    show_answer(result)

    st.divider()
    st.subheader("Was this answer helpful?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Yes, helpful", use_container_width=True):
            feedback.save_feedback(question, result["answer"], result["chunks"], "helpful")
            st.success("Thank you for your feedback!")

    with col2:
        if st.button("👎 No, escalate", use_container_width=True):
            feedback.save_feedback(question, result["answer"], result["chunks"], "unhelpful")
            escalation.escalate_query(question, result["confidence"], result["answer"])
            st.info("This has been escalated to HR for review.")
