
import pandas as pd
import requests
import json

url = "https://api.weatherstack.com/current?access_key={8b97da969d50a46b212f5211c3700f6d}"

response = requests.get(url)

def anime_names(url):
    if response.status_code == 200:
        data = response.json()
        print('success!')
    else:
        print(f"Error: {response.status_code}")

    df = pd.DataFrame(data)
    print(df.head)
