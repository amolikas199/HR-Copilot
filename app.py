"""
app.py  —  the entry point of the HR Copilot app.

Run it with:
    .venv/Scripts/streamlit.exe run app.py

This file only sets up the multi-page navigation. Each module lives in its
own file under views/. st.navigation shows a sidebar to switch between them.
"""

import os
import streamlit as st

st.set_page_config(page_title="HR Copilot", page_icon="💼")

# --- Sidebar branding (shows on every page) ---
with st.sidebar:
    st.markdown("## 💼 HR Copilot")
    st.caption("Grounded answers from your HR documents.")

    # Show which documents make up the knowledge base.
    try:
        pdfs = sorted(f for f in os.listdir("data") if f.lower().endswith(".pdf"))
    except FileNotFoundError:
        pdfs = []
    with st.expander(f"📁 Knowledge base ({len(pdfs)} docs)"):
        for name in pdfs:
            st.write(f"- {name}")

    with st.expander("ℹ️ About"):
        st.write(
            "An AI HR assistant that answers from company HR documents.\n\n"
            "- 📚 **Knowledge Assistant** — policy Q&A\n"
            "- 🧭 **Onboarding Assistant** — new-joiner help + checklist\n"
            "- 📝 **Leave Request** — plain English → structured request"
        )

    st.divider()

# Each st.Page points to a page file and gives it a title + icon for the sidebar.
pages = [
    st.Page("views/home.py", title="Home", icon="🏠", default=True),
    st.Page("views/knowledge.py", title="Knowledge Assistant", icon="📚"),
    st.Page("views/onboarding.py", title="Onboarding Assistant", icon="🧭"),
    st.Page("views/leave.py", title="Leave Request", icon="📝"),
    st.Page("views/policy_comparison.py", title="Policy Comparison", icon="📋"),
    st.Page("views/escalation.py", title="Escalation Tickets", icon="🚨"),
    st.Page("views/feedback.py", title="Feedback Analytics", icon="⭐"),
]

# Build the sidebar navigation and run whichever page is selected.
st.navigation(pages).run()
