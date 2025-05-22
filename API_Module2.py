
import pandas as pd
import requests
import json



r = requests.get('hhttp://api.weatherstack.com/')
x = r.json()
df = pd.read_json(json.dumps(x))