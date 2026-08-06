import streamlit as st

st.markdown("""
<style>
    .modules-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
        max-width: 400px;
        margin: 32px auto;
    }

    .module-card-clickable {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 32px 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 120px;
    }

    .module-card-clickable:hover {
        border-color: #10b981;
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.1);
        transform: translateY(-4px);
    }

    .module-icon-large {
        font-size: 48px;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.title("HR Copilot")
st.write("Get instant answers from your company's HR documents with AI-powered search and analysis.")

st.divider()

col1, col2, col3 = st.columns(3)
col1.metric("Modules", "6")
col2.metric("Grounded", "100%")
col3.metric("Live", "MongoDB")

st.subheader("Select a Module")

modules = [
    ("📚", "Knowledge", "knowledge"),
    ("🧭", "Onboarding", "onboarding"),
    ("📝", "Leave", "leave"),
    ("📋", "Policy", "policy"),
    ("🚨", "Escalation", "escalation"),
    ("⭐", "Feedback", "feedback"),
]

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for i, (icon, title, key) in enumerate(modules):
    with cols[i % 3]:
        if st.button(f"{icon}\n{title}", key=f"module_{key}", use_container_width=True, help=f"Open {title}"):
            if key == "knowledge":
                st.switch_page("views/knowledge.py")
            elif key == "onboarding":
                st.switch_page("views/onboarding.py")
            elif key == "leave":
                st.switch_page("views/leave.py")
            elif key == "policy":
                st.switch_page("views/policy_comparison.py")
            elif key == "escalation":
                st.switch_page("views/escalation.py")
            elif key == "feedback":
                st.switch_page("views/feedback.py")
