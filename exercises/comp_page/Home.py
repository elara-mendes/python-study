import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header("The Best Company")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc maximus turpis vulputate posuere aliquet. Curabitur eu blandit ex. Donec quis libero vel elit consequat vulputate. Morbi pulvinar mauris mattis tristique pharetra. Donec vitae diam sit amet metus mollis euismod. Donec semper quis lorem quis auctor. Etiam blandit vel diam vel suscipit. Nam fermentum nunc tortor, ut laoreet elit iaculis id.")

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        name = f"{row["first name"]} {row["last name"]}".title()
        st.subheader(name)
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        name = f"{row["first name"]} {row["last name"]}".title()
        st.subheader(name)
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        name = f"{row["first name"]} {row["last name"]}".title()
        st.subheader(name)
        st.write(row["role"])
        st.image("images/" + row["image"])