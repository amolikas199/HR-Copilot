import streamlit as st

st.set_page_config(page_title="HR Copilot", page_icon="🤖", layout="wide")

st.markdown("""
<style>
    * { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    body { background: #f9fafb; }
    h1, h2, h3 { color: #111827; }
</style>
""", unsafe_allow_html=True)

pages = [
    st.Page("views/home.py", title="🏠 Home", default=True),
    st.Page("views/knowledge.py", title="📚 Knowledge"),
    st.Page("views/onboarding.py", title="🧭 Onboarding"),
    st.Page("views/leave.py", title="📝 Leave"),
    st.Page("views/policy_comparison.py", title="📋 Policies"),
    st.Page("views/escalation.py", title="🚨 Escalations"),
    st.Page("views/feedback.py", title="⭐ Feedback"),
]

st.navigation(pages).run()
