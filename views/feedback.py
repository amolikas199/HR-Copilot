import streamlit as st
import feedback

st.title("⭐ Feedback & Analytics")

st.write("View employee feedback on answer quality.")

stats = feedback.get_feedback_stats()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Feedback", stats["total"])
col2.metric("Helpful 👍", stats["helpful"])
col3.metric("Unhelpful 👎", stats["unhelpful"])
col4.metric("Helpful %", f"{stats.get('helpful_ratio', 0)}%")

st.divider()

all_feedback = feedback.get_feedback_entries()

if not all_feedback:
    st.info("No feedback yet. Answers will appear here once users rate them.")
else:
    st.subheader("Recent Feedback")
    for entry in all_feedback[:10]:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"**Q**: {entry['question'][:60]}...")
            st.write(f"*A*: {entry['answer'][:100]}...")
        with col2:
            if entry["rating"] == "helpful":
                st.success("👍")
            else:
                st.error("👎")
