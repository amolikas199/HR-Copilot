import streamlit as st
import escalation

st.markdown("""
<style>
    .ticket-card {
        background: linear-gradient(135deg, #1a1f2e 0%, #16212b 100%);
        border: 2px solid #dc2626;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        transition: all 0.3s ease;
    }

    .ticket-card:hover {
        border-color: #f87171;
        box-shadow: 0 4px 12px rgba(220, 38, 38, 0.2);
    }

    .ticket-status {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: bold;
        background: #7f1d1d;
        color: #fca5a5;
    }

    .confidence-low {
        color: #fca5a5;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚨 Escalation Tickets")
st.markdown("Monitor low-confidence queries that need human HR review.")

tickets = escalation.get_tickets()

if not tickets:
    st.info("✅ No escalations! All queries were answered with confidence.")
else:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Tickets", len(tickets), "📊")
    col2.metric("Open Status", sum(1 for t in tickets if t["status"] == "OPEN"), "🔴")
    avg_conf = round(sum(t["confidence"] for t in tickets) / len(tickets), 1)
    col3.metric("Avg Confidence", f"{avg_conf}%", "📈")

    st.divider()

    st.subheader("Recent Escalations")
    for idx, ticket in enumerate(tickets, 1):
        with st.expander(f"#{idx} • {ticket['question'][:50]}...", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Status**: <span class='ticket-status'>{ticket['status']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Confidence**: <span class='confidence-low'>{ticket['confidence']}%</span>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"**Created**: {ticket['timestamp']}")

            st.divider()
            st.markdown(f"**Question**\n{ticket['question']}")
            st.markdown(f"**AI Response**\n{ticket['answer'][:300]}...")
            st.caption("⚠️ This query needs human HR review due to low confidence score.")
