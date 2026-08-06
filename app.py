import streamlit as st
import auth

st.set_page_config(
    page_title="HR Copilot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    * {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    body {
        background: #f9fafb;
    }

    [data-testid="stSidebar"] {
        background: white;
        border-right: 1px solid #e5e7eb;
    }

    [data-testid="stSidebarNav"] {
        padding: 0;
    }

    .stSidebar {
        background: white;
    }

    .sidebar-logo {
        text-align: center;
        padding: 24px 0;
        margin-bottom: 24px;
        border-bottom: 1px solid #e5e7eb;
    }

    .sidebar-logo-icon {
        font-size: 32px;
        margin-bottom: 8px;
    }

    .sidebar-logo-text {
        font-size: 18px;
        font-weight: 700;
        color: #111827;
    }

    [data-testid="stSidebarNavItems"] {
        padding: 0;
    }

    .stPageLink {
        padding: 12px 16px !important;
        margin: 4px 8px !important;
        border-radius: 6px !important;
        color: #6b7280 !important;
        background: transparent !important;
        transition: all 0.2s ease !important;
    }

    .stPageLink:hover {
        background: #f3f4f6 !important;
        color: #10b981 !important;
    }

    .stPageLink[aria-current="page"] {
        background: #ecfdf5 !important;
        color: #10b981 !important;
        font-weight: 600 !important;
    }

    .main-content {
        padding: 32px 40px;
        max-width: 1200px;
    }

    .header-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 24px;
        border-bottom: 1px solid #e5e7eb;
        margin-bottom: 32px;
    }

    .logout-btn {
        background: #f3f4f6;
        color: #374151;
        padding: 8px 16px;
        border-radius: 6px;
        border: 1px solid #d1d5db;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
        transition: all 0.2s ease;
    }

    .logout-btn:hover {
        background: #e5e7eb;
        color: #111827;
    }

    h1, h2, h3 {
        color: #111827;
    }

    p, span, div {
        color: #374151;
    }
</style>
""", unsafe_allow_html=True)

if not auth.check_login():
    auth.login_page()
    st.stop()

with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-icon">🤖</div>
        <div class="sidebar-logo-text">HR Copilot</div>
    </div>
    """, unsafe_allow_html=True)

    st.page_link("views/home.py", label="🏠 Home", icon="🏠")
    st.page_link("views/knowledge.py", label="📚 Knowledge", icon="📚")
    st.page_link("views/onboarding.py", label="🧭 Onboarding", icon="🧭")
    st.page_link("views/leave.py", label="📝 Leave", icon="📝")
    st.page_link("views/policy_comparison.py", label="📋 Policies", icon="📋")
    st.page_link("views/escalation.py", label="🚨 Escalations", icon="🚨")
    st.page_link("views/feedback.py", label="⭐ Feedback", icon="⭐")

    st.divider()

    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        if "logged_in" in st.query_params:
            del st.query_params["logged_in"]
        st.rerun()

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
