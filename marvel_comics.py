# To interact with APIs RESTs
from requests import request
import json
from pprint import pprint
from hashlib import md5
from datetime import datetime
from dotenv import load_dotenv
import os # To get the env. variables from the operating system.
load_dotenv() # We want to load the .env file.

ts = int(datetime.now().timestamp())

hash_code = md5(str.encode(f'{ts}' + os.environ['PUBLIC_KEY'] + os.environ['PRIVATE_KEY'], 'utf-8')).hexdigest()

p = {'ts': ts, 'apikey': os.environ['PRIVATE_KEY'], 'hash': hash_code, 'dateRange': '2013-01-01,2013-12-31', 'limit': 100} # URL Params.

r = request(method='GET',
url='https://gateway.marvel.com:443/v1/public/comics', # This is an endpoint.
params=p,
headers={"Content-Type": "application/json"},
timeout=10,
data={})

res = r.json()

for comic in res['data']['results']:
    print(comic['id'])

    print(comic['title'])

    for date in comic['dates']:
        if date['type'] == 'onsaleDate':
            print(date['date'])

    for creator in comic['creators']['items']:
        print(creator['name'])

    print('')