# セルは必要に応じて増やしてよい。
import requests
import os
import zipfile


def download_file(url):
    # url からファイル名切り出し
    s = url.split('/')
    filename = s[-1]
    
    # ファイルがないか確認
    if os.path.exists(filename):
        print(filename, 'exists')
        return filename
    
    res = requests.get(url,stream=True)
    if res.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in res.iter_content(chunk_size=1024):
                file.write(chunk)

    return filename

filename = download_file('http://www.aozora.gr.jp/cards/000148/files/789_ruby_5639.zip')

with zipfile.ZipFile(filename, 'r') as myzip:
    # zipファイルを開いて、中に格納されいるファイル名を表示
    for info in myzip.infolist():
        print(info.filename)
    # 解凍
    myzip.extractall()