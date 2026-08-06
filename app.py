import streamlit as st

st.set_page_config(page_title="HR Copilot", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    * { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    body { background: #f9fafb; }
    h1, h2, h3 { color: #111827; }

    [data-testid="stSidebar"] {
        background: white;
        padding-top: 20px;
        max-width: 100px;
    }

    [data-testid="stSidebarNav"] { display: none !important; }

    .sidebar-logo {
        text-align: center;
        margin-bottom: 40px;
        padding: 20px 0;
        border-bottom: 1px solid #e5e7eb;
    }

    .sidebar-logo-icon {
        font-size: 48px;
        margin-bottom: 8px;
    }

    .sidebar-logo-text {
        font-size: 14px;
        font-weight: 600;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-icon">🤖</div>
        <div class="sidebar-logo-text">HR Copilot</div>
    </div>
    """, unsafe_allow_html=True)

    pages_map = {
        "home": ("views/home.py", "🏠"),
        "knowledge": ("views/knowledge.py", "📚"),
        "onboarding": ("views/onboarding.py", "🧭"),
        "leave": ("views/leave.py", "📝"),
        "policy": ("views/policy_comparison.py", "📋"),
        "escalation": ("views/escalation.py", "🚨"),
        "feedback": ("views/feedback.py", "⭐"),
    }

    for key, (path, icon) in pages_map.items():
        if st.button(icon, key=f"nav_{key}", use_container_width=True):
            st.session_state.page = key
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
