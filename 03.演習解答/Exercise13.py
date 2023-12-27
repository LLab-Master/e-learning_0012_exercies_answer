# セルは必要に応じて増やしてよい。
from pprint import pprint
import time

from bs4 import BeautifulSoup
import requests

# 巡回するURL
url_base = 'https://www.aozora.gr.jp/index_pages/person_'
suffix = 'a ka sa ta na ha ma ya ra wa zz'.split()

urls = [url_base + s + '.html' for s in suffix]

# 巡回
authers = []
for url in urls:
    html = requests.get(url)
    html.encoding = 'utf-8'
    bsObj = BeautifulSoup(html.text, 'lxml')
    rows = bsObj.findAll('li')   
    for row in rows:
        auther = row.findAll('a')[0]
        authers.append(auther.text+"\n")
    time.sleep(1)

# ファイル書き出し
with open('authors-list.txt', 'w', encoding='utf-8') as f:
    f.writelines(authers)
