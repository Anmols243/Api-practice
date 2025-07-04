import requests
import json

try:
    response = requests.get('https://api.chucknorris.io/jokes/random')
    response.raise_for_status()
    joke = response.json()['value']

except Exception as e:
    print(e)
    
else:
    print(joke)
    
    