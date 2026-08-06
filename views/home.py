import streamlit as st

st.markdown("""
<style>
    .module-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 24px;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .module-card:hover {
        border-color: #10b981;
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.1);
        transform: translateY(-4px);
    }

    .module-icon {
        font-size: 40px;
        margin-bottom: 12px;
    }

    .module-title {
        font-size: 18px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 8px;
    }

    .module-desc {
        font-size: 14px;
        color: #6b7280;
        line-height: 1.6;
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

st.subheader("Available Modules")

col1, col2 = st.columns(2)

with col1:
    if st.button("📚 Knowledge Assistant", use_container_width=True, key="kb_main"):
        st.switch_page("views/knowledge.py")
    st.write("Ask HR policy questions and get answers grounded in your company documents.")

with col2:
    if st.button("🧭 Onboarding Assistant", use_container_width=True, key="ob_main"):
        st.switch_page("views/onboarding.py")
    st.write("Generate personalized onboarding checklists for new employees.")

col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Leave Request", use_container_width=True, key="lr_main"):
        st.switch_page("views/leave.py")
    st.write("Convert natural language into structured leave requests.")

with col2:
    if st.button("📋 Policy Comparison", use_container_width=True, key="pc_main"):
        st.switch_page("views/policy_comparison.py")
    st.write("Compare policy versions to detect changes and differences.")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚨 Escalations", use_container_width=True, key="esc_main"):
        st.switch_page("views/escalation.py")
    st.write("Monitor low-confidence queries sent for human review.")

with col2:
    if st.button("⭐ Feedback", use_container_width=True, key="fb_main"):
        st.switch_page("views/feedback.py")
    st.write("Track answer quality and user sentiment metrics.")
