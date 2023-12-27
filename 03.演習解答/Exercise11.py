# セルは必要に応じて増やしてよい。

import requests
import pandas as pd

url = 'http://www.aozora.gr.jp/index_pages/sakuhin_a1.html'
#html = requests.get(url)
#html.encoding='utf-8'
#tables = pd.read_html(html.text)

# Pandas で直接Webアクセス
tables = pd.read_html(url)
# 2番めのtable
table = tables[1]
# 1行目は削除
table = table[1:]
# 2,4桁目だけ取り出す
title_author_table = table[[1, 3]]

print(title_author_table)