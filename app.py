import streamlit as st

st.set_page_config(page_title="HR Copilot", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    * { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    body { background: #f9fafb; }
    [data-testid="stSidebar"] { background: white; border-right: 1px solid #e5e7eb; }
    h1, h2, h3 { color: #111827; }
    p, span, div { color: #374151; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🤖 HR Copilot")
    st.page_link("views/home.py", label="🏠 Home")
    st.page_link("views/knowledge.py", label="📚 Knowledge")
    st.page_link("views/onboarding.py", label="🧭 Onboarding")
    st.page_link("views/leave.py", label="📝 Leave")
    st.page_link("views/policy_comparison.py", label="📋 Policies")
    st.page_link("views/escalation.py", label="🚨 Escalations")
    st.page_link("views/feedback.py", label="⭐ Feedback")

pages = [
    st.Page("views/home.py", title="Home", default=True),
    st.Page("views/knowledge.py", title="Knowledge"),
    st.Page("views/onboarding.py", title="Onboarding"),
    st.Page("views/leave.py", title="Leave"),
    st.Page("views/policy_comparison.py", title="Policies"),
    st.Page("views/escalation.py", title="Escalations"),
    st.Page("views/feedback.py", title="Feedback"),
]

st.navigation(pages).run()
