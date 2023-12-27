# セルは必要に応じて増やしてよい。
import requests
import re

url  = 'https://www.lighthouselab.co.jp/p/data/sample.html'
html = requests.get(url)
text = html.text

pattern = re.compile('<td>(.*)</td>')
result = pattern.findall(text)

for i in range(0, len(result), 3):
    print(result[i], result[i+1], result[i+2], sep=',')