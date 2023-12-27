# セルは必要に応じて増やしてよい。
from bs4 import BeautifulSoup
import requests

url = 'http://www.aozora.gr.jp/index_pages/sakuhin_a1.html'
html = requests.get(url)
html.encoding='utf-8'
bsObj = BeautifulSoup(html.text,'lxml')

table = bsObj.findAll('table',{'class':'list'})[0]
#print(table)

rows = table.findAll('tr')
for row in rows[1:]:
    cells = row.findAll(['td'])
    title = cells[1].text
    auther = cells[3].text
    print(title, auther, sep=',', end='')
