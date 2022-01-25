# To interact with APIs RESTs
from urllib import response
from requests import request
import json
from pprint import pprint
from hashlib import md5
from datetime import datetime
from dotenv import load_dotenv
import os # To get the env. variables from the operating system.
import pandas as pd

load_dotenv() # We want to load the .env file.

ts = int(datetime.now().timestamp())

hash_code = md5(str.encode(f'{ts}' + os.environ['PUBLIC_KEY'] + os.environ['PRIVATE_KEY'], 'utf-8')).hexdigest()

p = {'ts': ts, 'apikey': os.environ['PRIVATE_KEY'], 'hash': hash_code, 'dateRange': '2013-01-01,2013-12-31', 'limit': 15} # URL Params.

r = request(method='GET',
url='https://gateway.marvel.com:443/v1/public/comics', # This is an endpoint.
params=p,
headers={"Content-Type": "application/json"},
timeout=10,
data={})

res = r.json()

response_list = []

for comic in res['data']['results']:
    response_list.append(comic)

# Ref.: https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#

df = pd.DataFrame.from_dict(response_list)
df_columns = df[['id', 'title', 'creators', 'dates', 'prices', 'stories', 'pageCount', 'events']]

pprint(df_columns)