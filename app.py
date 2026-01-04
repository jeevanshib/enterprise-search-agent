import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(
    page_title="Intelligent Enterprise Search",
    layout="centered"
)

st.title("🔍 Intelligent Enterprise Search")
st.write("Ask questions across enterprise knowledge with grounded answers and citations.")

query = st.text_input(
    "Enter your question",
    placeholder="e.g. What is the leave policy during probation?"
)

if st.button("Search"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching enterprise knowledge..."):
            response = requests.post(API_URL, json={"query": query})

        if response.status_code == 200:
            data = response.json()

            st.subheader("Answer")
            st.write(data["answer"])

            st.subheader("Sources")
            for src in data["sources"]:
                st.write(f"- {src}")
        else:
            st.error("Failed to fetch response from backend.")
