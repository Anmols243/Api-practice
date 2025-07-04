import requests
import json

api_url = "https://catfact.ninja/fact"

try:
    response = requests.get(api_url)
    response.raise_for_status()
    fact = response.json()['fact']
    
except Exception as e:
    print(e)

else:
    print(fact)
