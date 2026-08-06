"""
views/leave.py  —  Module 3 page: Leave Request Intelligence.

Type a leave request in plain English; see the structured result both as
friendly fields and as raw JSON (the machine-readable output).
"""

import json
import streamlit as st
from leave import extract_leave

st.title("📝 Leave Request Intelligence")
st.caption("Describe your leave in plain English — I'll turn it into a structured request.")

EXAMPLES = [
    "I need leave from the 12th to the 16th for medical reasons",
    "Taking casual leave next Monday and Tuesday for a family function",
]

picked = None
cols = st.columns(len(EXAMPLES))
for col, example in zip(cols, EXAMPLES):
    if col.button(example, key=f"lv_ex_{example}"):
        picked = example

with st.form("leave_form"):
    typed = st.text_area(
        "Your leave request:",
        placeholder="e.g. I need leave from the 12th to the 16th for medical reasons",
    )
    submitted = st.form_submit_button("Extract", type="primary")

sentence = picked or (typed if submitted else None)

if sentence:
    try:
        with st.spinner("Extracting details..."):
            data = extract_leave(sentence)
    except Exception:
        st.error("Sorry, I couldn't understand that. Try rephrasing with clearer dates.")
        st.stop()

    # Friendly view inside a card
    with st.container(border=True):
        st.subheader("Extracted request")
        col1, col2 = st.columns(2)
        col1.metric("Leave type", data["leave_type"])
        col2.metric("Total days", data["total_days"] if data["total_days"] is not None else "—")
        col1.write(f"**Start date:** {data['start_date']}")
        col2.write(f"**End date:** {data['end_date']}")
        st.write(f"**Reason:** {data['reason']}")
        if data["total_days"] is not None and data["total_days"] < 1:
            st.warning("The end date looks earlier than the start date — please double-check.")

    # Machine-readable view: the raw JSON (this is the module's real deliverable)
    st.subheader("Structured JSON")
    st.json(data)

    st.download_button(
        "⬇️ Download JSON",
        data=json.dumps(data, indent=2),
        file_name="leave_request.json",
        mime="application/json",
    )
