# セルは必要に応じて増やしてよい。
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.aozora.gr.jp/index_pages/person148.html#sakuhin_list_1'
html = requests.get(url)
html.encoding='utf-8'
bsObj = BeautifulSoup(html.text,'lxml')

table = bsObj.findAll('li')

list = []
for no, row in enumerate(table, start=1):
    #print(row.text)
    a = re.split(r'[\s、 ：（）]+', row.text)
    title, kana, id = a[0], a[1], a[3]
    list.append([no, title, kana, id])
    #print(a)
df = pd.DataFrame(list, columns=['No', 'タイトル', '仮名', '作品ID'])
print(df)