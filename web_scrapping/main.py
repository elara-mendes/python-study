import requests, selectorlib
import time, streamlit as st
import plotly.express as px
import pandas as pd

URL = "https://programmer100.pythonanywhere.com/"

get_date = time.strftime("%Y-%m-%d %H:%M:%S")

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extractor(source):
    extract = selectorlib.Extractor.from_yaml_file(r"C:\Users\elara\Documents\GitHub\python-study\web_scrapping\file.yaml")
    value = extract.extract(source)["temperatures"]
    return value

def write_file(date, extract):
    with open(r"C:\Users\elara\Documents\GitHub\python-study\web_scrapping\file.txt", "a") as file:
        file.write(f"{date} / {extract}" + "\n")

def read_file():
    with open(r"C:\Users\elara\Documents\GitHub\python-study\web_scrapping\file.txt", "r") as file:
        return file.readlines()

if __name__ == "__main__":
    scrapping = scrape(URL)
    extract_temp = extractor(scrapping)
    text = read_file()
    if extract_temp:
        if extract_temp not in text:
            file_text = write_file(get_date, extract_temp)
    print(extract_temp)
    print(get_date)

    text_list = []
    for line in text:
        text_list.append(line.split("/"))
        print(text_list)
    
    df = pd.DataFrame(text_list, columns=["datetime", "temperature"])
    df["datetime"] = pd.to_datetime(df["datetime"].str.strip())
    df["temperature"] = df["temperature"].str.strip().astype(int)

    st.header("Temperatures")

    figure = px.line(df, x="datetime", y="temperature", labels={"datetime": "Date", "temperature": "Temperatures"})
    st.plotly_chart(figure)
    