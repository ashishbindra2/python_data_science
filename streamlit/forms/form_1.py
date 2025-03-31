import streamlit as st

st.title("Login form")

user_email = st.text_input("Enter your email")
user_pass = st.text_input("Enter your password")

btn = st.button("login")

if btn:
    st.write(user_email)
    st.write(user_pass)