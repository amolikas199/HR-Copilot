import streamlit as st
import feedback

st.markdown("""
<style>
    .feedback-entry {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        padding: 16px;
        margin-bottom: 12px;
    }

    .feedback-helpful {
        border-left: 4px solid #10b981;
    }

    .feedback-unhelpful {
        border-left: 4px solid #ef4444;
    }

    .rating-badge {
        display: inline-block;
        font-size: 20px;
        margin-right: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.title("⭐ Feedback & Analytics")
st.write("Track user ratings and answer quality metrics.")

stats = feedback.get_feedback_stats()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total", stats["total"])
col2.metric("Helpful", stats["helpful"])
col3.metric("Unhelpful", stats["unhelpful"])
col4.metric("Success Rate", f"{stats.get('helpful_ratio', 0)}%")

if stats["total"] > 0:
    ratio = stats.get("helpful_ratio", 0)
    st.markdown(f"""
    <div style="background: #f3f4f6; height: 8px; border-radius: 4px; margin-top: 16px;">
        <div style="background: #10b981; height: 100%; width: {ratio}%; border-radius: 4px;"></div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

all_feedback = feedback.get_feedback_entries()

if not all_feedback:
    st.info("No feedback yet.")
else:
    st.subheader("Recent Feedback")
    for entry in all_feedback[:15]:
        card_class = "feedback-helpful" if entry["rating"] == "helpful" else "feedback-unhelpful"
        rating_icon = "👍" if entry["rating"] == "helpful" else "👎"

        st.markdown(f"""
        <div class="feedback-entry {card_class}">
            <span class="rating-badge">{rating_icon}</span>
            <strong>{entry['rating'].title()}</strong> · {entry['timestamp']}
            <p style="margin-top: 8px; font-size: 13px; color: #6b7280;">
                <strong>Q:</strong> {entry['question'][:60]}...
            </p>
        </div>
        """, unsafe_allow_html=True)
