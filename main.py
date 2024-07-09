import requests
import streamlit as st
from download_image import download_image
api_key = "Brc7oHWxGqGj6uMMHeOyACne8HtH8HQC6f3UPh7h"

url = ("https://api.nasa.gov/planetary/apod?"
       f"api_key={api_key}")

#get content
request = requests.get(url)
content = request.json()
# print(content)

# image_url = content['url']

#streamlit display content
st.title(content['title'])
#
# image = download_image(image_url)
# st.image(image)
#
# st.write(content["explanation"])

