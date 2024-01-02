import re
import requests
from collections import Counter

url = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(url)
list = response.json()
print(list)