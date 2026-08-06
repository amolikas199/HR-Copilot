import streamlit as st

st.markdown("""
<style>
    .module-card {
        background: linear-gradient(135deg, #1a1f2e 0%, #16212b 100%);
        border: 2px solid #2d3748;
        border-radius: 12px;
        padding: 24px;
        transition: all 0.3s ease;
        height: 100%;
    }

    .module-card:hover {
        border-color: #60a5fa;
        box-shadow: 0 8px 16px rgba(96, 165, 250, 0.2);
        transform: translateY(-4px);
    }

    .module-icon {
        font-size: 40px;
        margin-bottom: 12px;
    }

    .module-title {
        font-size: 20px;
        font-weight: bold;
        color: #60a5fa;
        margin-bottom: 8px;
    }

    .module-desc {
        font-size: 14px;
        color: #cbd5e1;
        margin-bottom: 16px;
        line-height: 1.6;
    }

    .hero {
        background: linear-gradient(135deg, #1a1f2e 0%, #16212b 100%);
        border: 2px solid #2d3748;
        border-radius: 12px;
        padding: 32px;
        margin-bottom: 32px;
        text-align: center;
    }

    .hero-title {
        font-size: 32px;
        font-weight: bold;
        background: linear-gradient(90deg, #60a5fa 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 12px;
    }

    .hero-subtitle {
        font-size: 16px;
        color: #94a3b8;
        margin-bottom: 8px;
    }

    .stats {
        display: flex;
        gap: 16px;
        margin-top: 20px;
        justify-content: center;
    }

    .stat-item {
        text-align: center;
    }

    .stat-number {
        font-size: 24px;
        font-weight: bold;
        color: #60a5fa;
    }

    .stat-label {
        font-size: 12px;
        color: #94a3b8;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-title">🤖 HR Copilot</div>
    <div class="hero-subtitle">Your intelligent HR assistant powered by AI</div>
    <p style="color: #cbd5e1; margin-top: 16px;">
        Get instant, grounded answers from your company's HR documents.<br>
        Every answer includes sources and confidence scores.
    </p>
</div>
""", unsafe_allow_html=True)

st.subheader("📊 Quick Stats", divider=True)
col1, col2, col3 = st.columns(3)
col1.metric("Active Modules", "6", "Ready to use")
col2.metric("Features", "Full-stack AI", "Persistence enabled")
col3.metric("Data Source", "Real-time", "MongoDB Atlas")

st.subheader("🚀 Modules", divider=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">📚</div>
        <div class="module-title">Knowledge Assistant</div>
        <div class="module-desc">Ask HR questions and get answers from your company documents with source citations.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Knowledge Assistant", use_container_width=True, key="kb"):
        st.session_state.current_page = "knowledge"
        st.rerun()

with col2:
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">🧭</div>
        <div class="module-title">Onboarding Assistant</div>
        <div class="module-desc">Get onboarding help or generate a personalized checklist for new joiners.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Onboarding", use_container_width=True, key="ob"):
        st.session_state.current_page = "onboarding"
        st.rerun()

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">📝</div>
        <div class="module-title">Leave Request</div>
        <div class="module-desc">Convert plain English descriptions into structured leave requests instantly.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Leave Request", use_container_width=True, key="lr"):
        st.session_state.current_page = "leave"
        st.rerun()

with col2:
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">📋</div>
        <div class="module-title">Policy Comparison</div>
        <div class="module-desc">Compare old and new policy documents to see exactly what changed.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Policy Comparison", use_container_width=True, key="pc"):
        st.session_state.current_page = "policy"
        st.rerun()

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">🚨</div>
        <div class="module-title">Escalation Tickets</div>
        <div class="module-desc">Monitor low-confidence queries that need human review. Persists in MongoDB.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("View Escalations", use_container_width=True, key="esc"):
        st.session_state.current_page = "escalation"
        st.rerun()

with col2:
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">⭐</div>
        <div class="module-title">Feedback Analytics</div>
        <div class="module-desc">Track user feedback and sentiment on answer quality. Real-time metrics & persistence.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("View Analytics", use_container_width=True, key="fb"):
        st.session_state.current_page = "feedback"
        st.rerun()
