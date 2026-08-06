import streamlit as st
import auth

st.set_page_config(
    page_title="HR Copilot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    [data-testid="stSidebar"] { display: none; }

    * { color: #e2e8f0; }
    body { background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%); }

    .logo {
        font-size: 20px;
        font-weight: bold;
        background: linear-gradient(90deg, #60a5fa 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
</style>
""", unsafe_allow_html=True)

if not auth.check_login():
    auth.login_page()
    st.stop()

col1, col2, col3 = st.columns([1, 9, 1])
with col1:
    st.markdown("🤖")
with col2:
    st.markdown('<div class="logo">HR Copilot</div>', unsafe_allow_html=True)
with col3:
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

st.divider()

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
