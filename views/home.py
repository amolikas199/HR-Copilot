import streamlit as st

st.title("HR Copilot")
st.write("Get instant answers from your company's HR documents with AI-powered search and analysis.")

st.divider()

col1, col2, col3 = st.columns(3)
col1.metric("Modules", "6")
col2.metric("Grounded", "100%")
col3.metric("Live", "MongoDB")

st.subheader("Available Modules")
st.write("👈 Use the sidebar to navigate between modules")
