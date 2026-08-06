import streamlit as st
import policy_comparison

st.title("📋 Policy Comparison Engine")

st.write("Upload two policy PDFs to detect changes between versions.")

col1, col2 = st.columns(2)

with col1:
    old_file = st.file_uploader("Old Policy (PDF)", type="pdf")

with col2:
    new_file = st.file_uploader("New Policy (PDF)", type="pdf")

if old_file and new_file:
    if st.button("Compare Policies"):
        with st.spinner("Analyzing policies..."):
            old_path = f"/tmp/{old_file.name}"
            new_path = f"/tmp/{new_file.name}"

            with open(old_path, "wb") as f:
                f.write(old_file.getbuffer())
            with open(new_path, "wb") as f:
                f.write(new_file.getbuffer())

            result = policy_comparison.compare_policies(old_path, new_path)

        st.markdown("### Differences Found:")
        st.markdown(result)
