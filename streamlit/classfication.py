import streamlit as st
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


@st.cache
def load_data():
    iris = load_data
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_name = load_data()

model = RandomForestClassifier()

model.fit(df.iloc[:,:-1])