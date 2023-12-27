# セルは必要に応じて増やしてよい。
from bs4 import BeautifulSoup
import requests

url = 'http://www.data.jma.go.jp/developer/xml/feed/regular.xml'
html = requests.get(url)
html.encoding='utf-8'
bsObj = BeautifulSoup(html.text,'lxml')

entries = bsObj.findAll('entry')
for entry in entries:
    name = entry.findAll('name')[0]
    print(name.text)
    content = entry.findAll('content')[0]
    print(content.text)