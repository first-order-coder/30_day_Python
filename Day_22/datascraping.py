# import requests
# from bs4 import BeautifulSoup

# # url = 'https://www.bu.edu/president/boston-university-facts-stats/'

# # response = requests.get(url)
# # status = response.status_code
# # print(status)   

# # content = response.content
# # # print(content)

# # soup = BeautifulSoup(content, 'html.parser')
# # print(soup.title)
# # print(soup.title.get_text())
# # print(soup.body.get_text())

# # tables = soup.find_all('Table', {'cellpadding': '3'})
# # print(tables)

# url = 'https://archive.ics.uci.edu/ml/datasets.php'

import requests
from bs4 import BeautifulSoup
import re

# url = 'https://www.newegg.com/p/1FT-000Y-008D6?Description=rtx%204090&cm_re=rtx_4090-_-1FT-000Y-008D6-_-Product'
# result = requests.get(url)
# # print(doc.prettify())

# with open(r'C:\Users\ginuram\Desktop\test.txt', 'a') as f:
#     doc = BeautifulSoup(f, 'html.parser')


# pattern = r'(\$.*)'
# tag = doc.find_all(text=re.compile('\$.*'))
# print(tag)
# tag = doc.find_all(text= '$')
# parent = tag[1].parent
# strong = parent.find('strong')
# print(strong.string)
# print(tag)

# with open (r'C:\Users\ginuram\Desktop\C++\webscr.html', 'r') as f:
#     doc = BeautifulSoup(f, 'lxml')

# tag = doc.find_all(['option'], text= 'Undergraduate')
# tag = doc.find_all(class_= 'btn-item')
# tag = doc.find_all(text= re.compile('\$.*'))
# for tag_ in tag:
#     print(tag_.strip())
# tag['color'] = 'Blue'\
# print(tag.attrs)
# print(tag)

url = 'https://coinmarketcap.com/'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')


tbody = doc.tbody #or tag = doc.find('tbody') both are correct # print(tbody.prettify()) # or print(tag.prettify())
trs = tbody.contents

prices = {}

for tr in trs[:10]:
    name, price =  tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.span.string
    print(fixed_name)
    # print(fixed_price)
#     prices[fixed_name] = fixed_price
# print(prices)       


