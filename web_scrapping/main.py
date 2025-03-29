import requests, selectorlib
import time, streamlit as st
import plotly.express as px
import pandas as pd
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"

get_date = time.strftime("%Y-%m-%d %H:%M:%S")

# Create connection
connection = sqlite3.connect(r'C:\Users\elara\Documents\GitHub\python-study\web_scrapping\data.db')

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extractor(source):
    extract = selectorlib.Extractor.from_yaml_file(r"C:\Users\elara\Documents\GitHub\python-study\web_scrapping\file.yaml")
    value = extract.extract(source)["temperatures"]
    return value

def write_file(date, extract):
    row = ([date, extract])
    cursor = connection.cursor()
    cursor.execute("INSERT INTO average VALUES(?,?)", row)
    connection.commit()

def read_file():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM average")
    row = cursor.fetchall()
    print(row)
    return row

if __name__ == "__main__":
    scrapping = scrape(URL)
    extract_temp = extractor(scrapping)
    text = read_file()
    if extract_temp:
        file_text = write_file(get_date, extract_temp)
    # print(extract_temp)
    # print(get_date)

    # for line in text:
    #     new_text = [item for item in text]
    #     print(new_text)
    
    df = pd.DataFrame(text, columns=["datetime", "temperature"])
    df["datetime"] = pd.to_datetime(df["datetime"].str.strip())

    st.header("Temperatures")

    figure = px.line(df, x="datetime", y="temperature", labels={"datetime": "Date", "temperature": "Temperatures"})
    st.plotly_chart(figure)
    