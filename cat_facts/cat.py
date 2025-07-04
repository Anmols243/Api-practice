import requests
import json

api_url = "https://catfact.ninja/fact"
facts = set()
i = 0

try:
    while len(facts) < 5:
        response = requests.get(api_url)
        response.raise_for_status()
        fact = response.json()['fact']
        facts.add(fact)
    
    for i, fact in enumerate(facts, start=1):
        print(f"{i}. {fact}\n")
    
except Exception as e:
    print(e)
    


