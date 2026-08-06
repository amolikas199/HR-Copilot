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
    }

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

    .sidebar-nav {
        display: flex;
        flex-direction: column;
        gap: 16px;
        padding: 20px 0;
    }

    .sidebar-nav-item {
        text-align: center;
        font-size: 24px;
        cursor: pointer;
        opacity: 0.6;
        transition: all 0.2s ease;
        padding: 12px;
        border-radius: 8px;
    }

    .sidebar-nav-item:hover {
        opacity: 1;
        background: #f3f4f6;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-icon">🤖</div>
        <div class="sidebar-logo-text">HR Copilot</div>
    </div>
    """, unsafe_allow_html=True)

    modules = [
        ("📚", "views/knowledge.py"),
        ("🧭", "views/onboarding.py"),
        ("📝", "views/leave.py"),
        ("📋", "views/policy_comparison.py"),
        ("🚨", "views/escalation.py"),
        ("⭐", "views/feedback.py"),
    ]

    for icon, path in modules:
        if st.button(icon, key=f"nav_{path}", use_container_width=True):
            st.switch_page(path)

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
