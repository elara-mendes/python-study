import glob, os
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
import streamlit as st

text_files = glob.glob("diary/*.txt")
file_name = [os.path.splitext(os.path.basename(text))[0] for text in text_files]
analyzer = SentimentIntensityAnalyzer()
# print(text_files)
# print(file_name)
pos = []
neg = []
for text in text_files:
    with open(text, "r") as file:
        text_file = file.read()
        text_analysis = analyzer.polarity_scores(text_file)
        pos.append(text_analysis["pos"])
        neg.append(text_analysis["neg"])
#         print(text_analysis)
# print(pos)
st.header("Sentiment Analysis")

st.subheader("Positive Sentiment")
figure = px.line(text_files, x=file_name, y=pos, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure, key="pos_sentiment")

st.subheader("Negative Sentiment")
figure_2 = px.line(text_files, x=file_name, y=neg, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure_2, key="neg_sentiment")


