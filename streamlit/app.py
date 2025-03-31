import streamlit as st
import pandas as pd
import numpy as np


# Title of the application
st.title("hello title")

# Display a sample text
st.write("This is sample text!!")


## Create a simple Dataframe
df = pd.DataFrame({
    "first column": [1,2,3,4],
    "secound coulmn": [10,20,30,40]
})


## Display the Dataframe
st.write("Here is the dataframe")
st.write(df)


# Create a line chart

chart_data = pd.DataFrame(
    np.random.randn(10,3), columns = ['a','b','c']
)

st.line_chart(chart_data)