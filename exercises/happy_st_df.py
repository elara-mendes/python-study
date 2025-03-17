import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("happy.csv")

gdp = df["gdp"]
happiness = df["happiness"]
generosity = df["generosity"]

options = {
    "GDP": gdp,
    "Happiness": happiness,
    "Generosity": generosity
}

st.title("In Search for Happiness")
select_box_x = st.selectbox(
    label="Select the data for the X-axis", options=list(options.keys()))
select_box_y = st.selectbox(
    label="Select the data for the Y-axis", options=list(options.keys()))

st.subheader(f"{select_box_x} and {select_box_y}")

figure = px.scatter(data_frame=df, x=select_box_x.lower(), y=select_box_y.lower(), labels={select_box_x.lower(): select_box_x, select_box_y.lower(): select_box_y})

st.plotly_chart(figure)