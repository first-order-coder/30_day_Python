import re
import requests
from bs4 import BeautifulSoup

url = f'https://yts.mx/browse-movies/0/all/all/8/latest/0/all'
result = requests.get(url).text
soup = BeautifulSoup(result, 'lxml')

courses = soup.find(class_="tsc_pagination tsc_paginationA tsc_paginationA06")
pg = courses.contents[2:10]

lst = []
for page in pg:
    num = page.find('a').string
    lst.append(num)
page_num = int(lst[-1])

for info in range(1, page_num+1):
    url = f'https://yts.mx/browse-movies/0/all/all/8/latest/0/all?page={info}'
    result = requests.get(url).text
    soup = BeautifulSoup(result, 'lxml')
    
    doc = soup.section.find(class_='row').contents
    print(doc)
        # rating_info_class = item.find('h4') #<--int object is iterable use list[]
        # print(rating_info_class)
        # for i in rating_info_class:
        #     lst1 = []
        #     lst1.append(i)
        #     print(lst1)
       
    