import streamlit as st

st.title("sidebar")

# Sidebar
st.sidebar.header("About")
st.sidebar.title("This is our demo Project")

algorithms = st.sidebar.selectbox("Your Alogorithm",["Liner Regration","Logistic Regration", "dession tree"])