import streamlit as st

with open("java.pdf", "rb") as file:
    btn = st.download_button(
        label="syllabus",
        data=file,
        file_name="java.pdf"
    )