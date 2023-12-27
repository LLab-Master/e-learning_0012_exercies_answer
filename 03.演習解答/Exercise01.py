#取得したWebページの保存
from urllib.request import urlopen

url = 'https://ja.wikipedia.org/wiki/Python'
html = urlopen(url)

encode = html.info().get_content_charset(failobj='utf-8')

text_byte = html.read()
text = text_byte.decode(encode)

with open('python.html','w',encoding=encode) as f:
    f.write(text)