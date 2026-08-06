"""
views/home.py  —  the landing page.

A short welcome plus one card per module, each with a link that jumps
straight to that page.
"""

import streamlit as st

st.title("💼 HR Copilot")
st.subheader("Your AI assistant for HR questions")
st.write(
    "Get instant, reliable answers drawn straight from your company's HR documents — "
    "every answer is grounded in the source text and cites where it came from."
)
st.write("")

# Three module cards, side by side.
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("### 📚 Knowledge Assistant")
        st.write("Ask any HR policy question and get an answer with sources and a confidence score.")
        st.page_link("views/knowledge.py", label="Open", icon="➡️")

with col2:
    with st.container(border=True):
        st.markdown("### 🧭 Onboarding Assistant")
        st.write("New-joiner help — ask onboarding questions or generate a ready-to-use checklist.")
        st.page_link("views/onboarding.py", label="Open", icon="➡️")

with col3:
    with st.container(border=True):
        st.markdown("### 📝 Leave Request")
        st.write("Describe your leave in plain English and get a clean, structured request.")
        st.page_link("views/leave.py", label="Open", icon="➡️")
