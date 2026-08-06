import streamlit as st
import escalation

st.markdown("""
<style>
    .ticket-card {
        background: white;
        border-left: 4px solid #ef4444;
        border: 1px solid #fee2e2;
        border-radius: 6px;
        padding: 16px;
        margin-bottom: 12px;
    }

    .ticket-status {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 600;
        background: #fee2e2;
        color: #dc2626;
    }

    .confidence-low {
        color: #dc2626;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚨 Escalation Tickets")
st.write("Monitor queries that need human HR review due to low AI confidence.")

tickets = escalation.get_tickets()

if not tickets:
    st.info("No escalations. All queries have been answered confidently.")
else:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total", len(tickets))
    col2.metric("Open", sum(1 for t in tickets if t["status"] == "OPEN"))
    avg_conf = round(sum(t["confidence"] for t in tickets) / len(tickets), 1)
    col3.metric("Avg Confidence", f"{avg_conf}%")

    st.divider()

    for idx, ticket in enumerate(tickets, 1):
        with st.expander(f"#{idx} • {ticket['question'][:50]}...", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Status:** {ticket['status']}")
                st.markdown(f"**Confidence:** <span class='confidence-low'>{ticket['confidence']}%</span>", unsafe_allow_html=True)
            with col2:
                st.caption(f"Created: {ticket['timestamp']}")

            st.divider()
            st.markdown(f"**Question**\n\n{ticket['question']}")
            st.markdown(f"**Response**\n\n{ticket['answer'][:300]}...")
