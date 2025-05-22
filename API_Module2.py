
import pandas as pd
import requests
import json



url = "https://testbooru.donmai.us"

response = requests.get(url)

def anime_names(url):

    if response.status_code == 200:
        posts = response.json()
        print('success!')
    else:
        print('Error:', response.status_code)

anime_names_df = anime_names(url)
print(anime_names_df)
