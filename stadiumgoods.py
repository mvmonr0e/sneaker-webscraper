import requests
import json

def searchsg(query,s):
    url = f'https://www.stadiumgoods.com/api/commerce/v1/listing?pageindex=1&query={query.replace(" ", "%20")}'
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.7',
        'ff-country': 'US',
        'ff-currency': 'USD',
        'referer': 'https://www.stadiumgoods.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
    }

    html = s.get(url = url, headers = headers)
    output = json.loads(html.text)
    return output['products']['entries']['0']