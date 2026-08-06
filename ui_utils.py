"""
ui_utils.py  —  small display helpers shared by the pages.

Keeping these here means each page file stays short and they all render
answers the same way.
"""

import re
import streamlit as st

# Map the confidence label to a semantic badge colour.
_BADGE_COLOR = {"High": "green", "Medium": "orange", "Low": "red"}


def clean_snippet(text):
    """Tidy up raw PDF text so it reads cleanly in the UI:
    fix odd dash characters and collapse messy whitespace into single spaces."""
    text = text.replace("‐", "-").replace("’", "'").replace(" ", " ")
    text = re.sub(r"\s+", " ", text)   # runs of spaces/newlines/tabs -> one space
    return text.strip()


def show_answer(result):
    """Render an answer dict from rag.ask(): the answer, confidence, and sources."""
    # The answer sits in a bordered card.
    with st.container(border=True):
        st.markdown("#### 📌 Answer")
        st.write(result["answer"])

        label = result["confidence_label"]
        st.badge(
            f"Confidence: {label} · {result['confidence']}%",
            color=_BADGE_COLOR.get(label, "gray"),
        )
        if label == "Low":
            st.warning("This answer may not be reliable — please verify with HR.")

    # Sources below, each in its own collapsible card.
    st.markdown("##### 📄 Sources")
    for chunk in result["chunks"]:
        label = f"{chunk['source']}  ·  page {chunk['page']}"
        with st.expander(label):
            st.markdown(f"> {clean_snippet(chunk['text'])}")
