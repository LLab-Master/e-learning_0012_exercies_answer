# セルは必要に応じて増やしてよい。
import requests
import re

url  = 'https://www.lighthouselab.co.jp/p/data/sample.html'
html = requests.get(url)
text = html.text

pattern = re.compile('<li>(.*)</li>')
result = pattern.findall(text)

for d in result:
    print(d)