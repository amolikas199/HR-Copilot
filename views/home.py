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
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">📚</div>
        <div class="module-title">Knowledge Assistant</div>
        <div class="module-desc">Ask HR policy questions and get answers grounded in your company documents.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">🧭</div>
        <div class="module-title">Onboarding Assistant</div>
        <div class="module-desc">Generate personalized onboarding checklists for new employees.</div>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">📝</div>
        <div class="module-title">Leave Request</div>
        <div class="module-desc">Convert natural language into structured leave requests.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">📋</div>
        <div class="module-title">Policy Comparison</div>
        <div class="module-desc">Compare policy versions to detect changes and differences.</div>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">🚨</div>
        <div class="module-title">Escalations</div>
        <div class="module-desc">Monitor low-confidence queries sent for human review.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-card">
        <div class="module-icon">⭐</div>
        <div class="module-title">Feedback</div>
        <div class="module-desc">Track answer quality and user sentiment metrics.</div>
    </div>
    """, unsafe_allow_html=True)

st.caption("👈 Click modules in the sidebar to open them")
