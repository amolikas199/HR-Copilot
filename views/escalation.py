import streamlit as st
import escalation

st.title("🚨 Escalation Tickets")

st.write("View open HR escalation tickets from low-confidence queries.")

tickets = escalation.get_tickets()

if not tickets:
    st.info("No escalation tickets yet. All queries have been answered with sufficient confidence!")
else:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Tickets", len(tickets))
    col2.metric("Open", sum(1 for t in tickets if t["status"] == "OPEN"))
    col3.metric("Avg Confidence", round(sum(t["confidence"] for t in tickets) / len(tickets), 1))

    st.divider()

    for ticket in tickets:
        with st.expander(f"Ticket {ticket['_id']} - {ticket['question'][:50]}..."):
            st.write(f"**Status**: {ticket['status']}")
            st.write(f"**Confidence**: {ticket['confidence']}%")
            st.write(f"**Question**: {ticket['question']}")
            st.write(f"**Answer Provided**: {ticket['answer'][:200]}...")
            st.write(f"**Time**: {ticket['timestamp']}")
