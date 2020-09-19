import json
import time

import requests


base_url = 'https://storage.googleapis.com/fiawec-prod/assets/live/WEC/__data.json'


def getMs() -> int:
    return int(round(time.time() * 1000))

def getUrl(url: str) -> str:
    return '{}?_t={}'.format(url, getMs())

filename = '{}'.format(getMs())

data = requests.get(getUrl(base_url))
if data.status_code == 200:
    with open('{}.json'.format(filename), 'w') as f:
        json.dump(data.json(), f)
