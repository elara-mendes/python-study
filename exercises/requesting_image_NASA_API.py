import os
import requests
import streamlit as st

NASA_KEY = os.getenv("NASA_API")
# print(NASA_KEY)

url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_KEY}&count={1}"

request_content = requests.get(url)
request_dict = request_content.json()


title = st.title(request_dict[0]["title"])
image = st.image(request_dict[0]["url"])
text = st.text(request_dict[0]["explanation"])
print(type(request_content.json()))

# st.image()

print(request_content)