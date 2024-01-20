import streamlit as st

a = st.number_input("Enter num 1")
b = st.number_input("Enter num 2")
if st.button("Add"):
    st.title(a+b)

with open("main.py", "rb") as file:
    btn = st.download_button(
        label="Download Main file",
        data=file,
        file_name="main.py"
    )