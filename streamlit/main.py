import streamlit as st

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["a", "b", "c"]
)
# print(np.random.randn(20,3))
# print(chart_data)

st.bar_chart(chart_data)
st.line_chart(chart_data)
