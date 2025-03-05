import requests


image_request = requests.get(url="https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg")

print(f"Status: {image_request}")

with open("image.jpg", "wb") as image:
    image.write(image_request.content)