import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import smtplib, ssl
# import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
# from tools.send_email import email_send

def email_send(message):
    host = "smtp.gmail.com"
    port = 465

    load_dotenv()
    app_password = os.getenv("GMAIL_PASSWORD")

    user_name = "elaradomingos@gmail.com"
    password = app_password
    receiver = "elaradomingos@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)


df = pd.read_csv("topics.csv")

st.header("Contact Us")

list_options = []
for index, row in df.iterrows():
    list_options.append(row["topic"])

with st.form(key="comp_form"):
    email = st.text_input("Your email address")
    options = st.selectbox(label="What do you want to discuss?", options=list_options)
    message = st.text_area("Your message")
    form_message = f"Subject: {options}\r\n\r\nMessage: {message}\r\nEmail: {email}"
    button = st.form_submit_button("Submit")
    if button:
        if email and message:
            email_send(form_message)
            st.success("Mail sent with success")
        else:
            st.error("Please, fill de form.")

