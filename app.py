import os
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

    * {
        color: #e2e8f0;
    }

    body {
        background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
    }

    .header-bar {
        background: linear-gradient(90deg, #1a1f2e 0%, #16212b 100%);
        border-bottom: 2px solid #2d3748;
        padding: 16px 24px;
        margin: -8px -8px 24px -8px;
        border-radius: 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .logo {
        font-size: 24px;
        font-weight: bold;
        background: linear-gradient(90deg, #60a5fa 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
    }

    .nav-tabs {
        display: flex;
        gap: 8px;
        justify-content: center;
        margin-bottom: 24px;
        flex-wrap: wrap;
    }

    .nav-tab {
        padding: 10px 16px;
        border-radius: 8px;
        background: #1a1f2e;
        border: 2px solid #2d3748;
        color: #94a3b8;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
    }

    .nav-tab:hover {
        background: #2d3748;
        border-color: #60a5fa;
        color: #60a5fa;
    }

    .nav-tab.active {
        background: linear-gradient(135deg, #60a5fa 0%, #818cf8 100%);
        border-color: #60a5fa;
        color: white;
    }

    .logout-btn {
        padding: 8px 12px;
        background: #7f1d1d;
        border: 1px solid #dc2626;
        border-radius: 6px;
        color: #fca5a5;
        cursor: pointer;
        font-size: 12px;
        transition: all 0.3s ease;
    }

    .logout-btn:hover {
        background: #991b1b;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

if not auth.check_login():
    auth.login_page()
    st.stop()

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

col1, col2 = st.columns([1, 10])
with col1:
    st.markdown('<div class="logo">🤖</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="logo" style="font-size: 20px; margin-top: 4px;">HR Copilot</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([8, 1, 1])
with col3:
    if st.button("🚪 Logout", key="logout_btn"):
        st.session_state.logged_in = False
        st.rerun()

pages = {
    "home": ("views/home.py", "🏠 Home"),
    "knowledge": ("views/knowledge.py", "📚 Knowledge"),
    "onboarding": ("views/onboarding.py", "🧭 Onboarding"),
    "leave": ("views/leave.py", "📝 Leave"),
    "policy": ("views/policy_comparison.py", "📋 Policies"),
    "escalation": ("views/escalation.py", "🚨 Escalations"),
    "feedback": ("views/feedback.py", "⭐ Feedback"),
}

cols = st.columns(len(pages))
for idx, (key, (path, label)) in enumerate(pages.items()):
    with cols[idx]:
        active = "active" if st.session_state.current_page == key else ""
        if st.button(label, use_container_width=True, key=f"nav_{key}"):
            st.session_state.current_page = key
            st.rerun()

st.divider()

page_path, _ = pages.get(st.session_state.current_page, pages["home"])
exec(open(page_path).read())
