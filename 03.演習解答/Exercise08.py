# セルは必要に応じて増やしてよい。
from bs4 import BeautifulSoup
import requests

url = 'https://www.kantei.go.jp/index-jnews.rdf'
html = requests.get(url)
bsObj = BeautifulSoup(html.text,'lxml')

items = bsObj.findAll('item')
for item in items:
    print(item.title.text)