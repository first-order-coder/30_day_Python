# import re
# import requests
# from collections import Counter

# url = 'https://api.thecatapi.com/v1/breeds'

# response = requests.get(url)
# list = response.json()
# print(list)

''' Application Process Interface'''
''' If you dont want to show the actual data you can put it in a seperate file and call the method >> open('file_name', 'r').read() '{r}' means in reading mode'''

import requests
import datetime as dt

# base_url = "https://api.github.com"
# response = requests.get(base_url).json() --> testing the api
# print(response)

base_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
api_key = open(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\Day_20\api_key.txt', 'r').read()

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = base_url

#can use given paramters in API Docs that are available to plan and endpoint API
parameters = {
  'start':'1', #start from the first cryptocurrency
  'limit':'100', #limit to 5000 currencies
  'convert':'USD', #convert the values to USD on the way
  'price_min':'10000', #the parameters are given in the API documents
#   'slug':'ethereum', --> cannot use due to not included in basic plan
  'convert':'EUR',
  'sort':'price'
} 
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)

  data_2 = json.dumps(data, indent=4) #change json file in to a more readble way
#   info = json.loads(data_2) #converting data_2(str) --> dictionary type
  print(data_2)

  #to get the price history
#   coin_name = data['data'][0]['quote']['USD']
#   print(coin_name)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

