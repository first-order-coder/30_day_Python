from bs4 import BeautifulSoup
import requests
import re

# search_item = input('What are You Looking For')

url = f'https://www.ss.lv/lv/electronics/computers/noutbooks/filter/'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')


page_text = doc.find('div', class_='td2')
lst = []
for page in page_text.contents[1:14]:
    regex = r'>[\d+]<'
    matches = re.findall(regex.strip('><'), str(page))
    lst.extend(matches)
    set1 = set(lst)
    lst1 = list(set1)
    lst1.sort()

num1 = int(lst1[-1])
for page1 in range(1, num1+1):
    url = f'https://www.ss.lv/lv/electronics/computers/noutbooks/filter/page{page1}.html'
    result = requests.get(url).text
    doc = BeautifulSoup(result, 'html.parser')

    div = doc.find('table', align="center", cellpadding="2", cellspacing="0", border="0", width="100%")
    items = div.contents[2:3]
    print(items)
    









































