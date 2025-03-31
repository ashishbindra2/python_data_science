# More intrative application

import streamlit as st
import pandas as pd

st.title("streamlit Text Input")


name = st.text_input("Enter you name")

if name:
    st.write(f"Hello, {name}")

age = st.slider("Select your age:", 0,100,25)

st.write(f"Your age is {age}.")


options = ["Python", "Java", "C++","js"]
choice = st.selectbox("choose your facorite language", options)
st.write(f"Your selected {choice}")

upload_file = st.file_uploader("choose a csv file", type="csv")


if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)