import requests
import json

def searchx(query,s):
    url = f'https://stockx.com/api/browse?_search={query}'

    html = s.get(url = url)
    output = json.loads(html.text)
    return output['Products'][0]