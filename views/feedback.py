import streamlit as st
import feedback

st.markdown("""
<style>
    .feedback-card {
        background: linear-gradient(135deg, #1a1f2e 0%, #16212b 100%);
        border: 2px solid #2d3748;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        transition: all 0.3s ease;
    }

    .feedback-card:hover {
        border-color: #60a5fa;
        box-shadow: 0 4px 12px rgba(96, 165, 250, 0.15);
    }

    .feedback-helpful {
        border-left: 4px solid #22c55e;
    }

    .feedback-unhelpful {
        border-left: 4px solid #ef4444;
    }

    .stats-container {
        background: linear-gradient(135deg, #1a1f2e 0%, #16212b 100%);
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 24px;
    }

    .progress-bar {
        background: linear-gradient(90deg, #22c55e 0%, #22c55e var(--ratio), #7f1d1d var(--ratio), #7f1d1d 100%);
        height: 24px;
        border-radius: 6px;
        margin-top: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 12px;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("⭐ Feedback Analytics")
st.markdown("Track user sentiment and answer quality metrics in real-time.")

stats = feedback.get_feedback_stats()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Feedback", stats["total"], "📊")
col2.metric("👍 Helpful", stats["helpful"], "✓")
col3.metric("👎 Unhelpful", stats["unhelpful"], "✗")
col4.metric("Success Rate", f"{stats.get('helpful_ratio', 0)}%", "📈")

if stats["total"] > 0:
    ratio = stats.get("helpful_ratio", 0)
    st.markdown(f"""
    <div class="progress-bar" style="--ratio: {ratio}%;">
        {ratio}% quality score
    </div>
    """, unsafe_allow_html=True)

st.divider()

all_feedback = feedback.get_feedback_entries()

if not all_feedback:
    st.info("📭 No feedback yet. User ratings will appear here once they rate answers.")
else:
    st.subheader("Recent Feedback Entries")
    for entry in all_feedback[:15]:
        rating_icon = "👍" if entry["rating"] == "helpful" else "👎"
        card_class = "feedback-helpful" if entry["rating"] == "helpful" else "feedback-unhelpful"

        st.markdown(f"""
        <div class="feedback-card {card_class}">
            <strong>Q:</strong> {entry['question'][:70]}...<br>
            <strong>A:</strong> {entry['answer'][:120]}...<br>
            <strong style="font-size: 20px;">{rating_icon}</strong> {entry['rating'].title()} · {entry['timestamp']}
        </div>
        """, unsafe_allow_html=True)
