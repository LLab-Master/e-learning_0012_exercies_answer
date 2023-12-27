# セルは必要に応じて増やしてよい。
from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = 'https://www.python.org/blogs/'
html = requests.get(url)
bsObj = BeautifulSoup(html.text,'lxml')

latest_news = bsObj.findAll('ul',{'class':'list-recent-posts'})[0]

for news in latest_news.findAll('a'):
    print(news.text)