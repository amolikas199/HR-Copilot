"""
views/onboarding.py  —  Module 2 page: the Onboarding Assistant.

Two features:
  1. Q&A for new joiners  — reuses the same ask() engine as Module 1.
  2. Checklist generator   — one button that builds an onboarding checklist.
"""

import streamlit as st
from rag import ask
from checklist import generate_checklist
from ui_utils import show_answer

st.title("🧭 Onboarding Assistant")
st.caption("New here? Ask an onboarding question, or generate a ready-to-use checklist.")

# --- Feature 1: Onboarding Q&A ---
EXAMPLES = [
    "What documents do I need to submit?",
    "What trainings are required?",
]

picked = None
cols = st.columns(len(EXAMPLES))
for col, example in zip(cols, EXAMPLES):
    if col.button(example, key=f"onb_ex_{example}"):
        picked = example

with st.form("onb_form"):
    typed = st.text_input(
        "Ask an onboarding question:",
        placeholder="e.g. What documents do I need to submit on my first day?",
    )
    submitted = st.form_submit_button("Ask", type="primary")

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

# --- Feature 2: Checklist generator ---
st.subheader("📋 Generate an onboarding checklist")
st.caption("Builds a checklist of onboarding steps from the HR documents.")

if st.button("Generate checklist", type="primary"):
    try:
        with st.spinner("Building your checklist..."):
            # Store in session_state so it stays on screen after the download
            # button is clicked (a click re-runs the whole page).
            st.session_state["checklist"] = generate_checklist()
    except Exception:
        st.error("Couldn't generate the checklist right now. Please try again.")

if "checklist" in st.session_state:
    with st.container(border=True):
        st.markdown("#### Your onboarding checklist")
        st.markdown(st.session_state["checklist"])
        st.download_button(
            "⬇️ Download checklist",
            data=st.session_state["checklist"],
            file_name="onboarding_checklist.md",
        )
