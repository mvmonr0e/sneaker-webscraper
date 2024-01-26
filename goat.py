import requests
import json

def searchG(query,s):
    url = f'https://ac.cnstrc.com/search/{query.replace(" ", "%20")}?c=ciojs-client-2.29.11&key=key_XT7bjdbvjgECO5d8&i=3d08ddc3-8471-4c02-8574-1b450628144a&s=2&num_results_per_page=25&_dt=1663732655000'

    html = s.get(url = url)
    output = json.loads(html.text)

    return output['response']['results'][0]