import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv("pages/used_cars.csv")
st.title("Welcome To Usedcars Analysis Project")
st.text("Here is our Data features")
st.dataframe(df.head(10))
