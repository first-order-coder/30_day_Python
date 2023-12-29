import json

a ='{ "name": "Afghanistan", "capital": "Kabul", "languages": ["Pashto", "Uzbek",  "Turkmen"], "population": 27657145, "flag": "https://restcountries.eu/data/afg.svg","currency": "Afghan afghani" }'

y = json.loads(a)
print("JSON string =", y)
print()