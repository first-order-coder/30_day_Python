import re
from bs4 import BeautifulSoup
import requests

search_item = input('What Are U Looking For?' )

url = f'https://www.newegg.com/p/pl?d={search_item}&N=4131'
results = requests.get(url).text
doc = BeautifulSoup(results, 'html.parser')

page_text = str(doc.find(class_="list-tool-pagination").strong)
print(page_text)
regex_pattern = r'\d+'
pages = int(re.findall(regex_pattern, page_text)[-1])

items_found = {}

for page in range(1, pages+1):
    url = f'https://www.newegg.com/p/pl?d={search_item}&N=4131&{page}'
    results = requests.get(url).text
    doc = BeautifulSoup(results, 'html.parser')
    
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text = re.compile(search_item))

    for item in items:
        parent = item.parent
        if parent.name != 'a':
            continue
        link = parent['href']
        next_parent = item.find_parent(class_='item-container')
        try:
            price = next_parent.find(class_='price-current').strong
            new_price = price.string
            items_found[item] = {'Price': int(new_price.replace(',', '')), 'Link': link}
        except:
            pass
    print(items_found)

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
	print(item[0])
	print(f"${item[1]['price']}")
	print(item[1]['link'])
	print("-------------------------------")




    # items = div.find(class_="item-info")
    # print(items.find(class_='item-title'))
    # print('-------------------')
