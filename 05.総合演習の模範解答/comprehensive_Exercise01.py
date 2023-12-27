# 総合演習の模範解答
import time

from bs4 import BeautifulSoup
import requests

import zipfile
import os

url_top = 'https://www.aozora.gr.jp/'

url_base = 'https://www.aozora.gr.jp/index_pages/sakuhin_'
suffix = 'a i u e o'.split()

urls = [url_base + s + '1.html' for s in suffix]

person_list = []
book_name_list = []
book_url_list = []
zip_url_list = []
card_list = []
txt_filename_list = []

# 作品名と詳細URLをまとめて取得
authers = []
for url in urls:
    html = requests.get(url)
    html.encoding = 'utf-8'
    bsObj = BeautifulSoup(html.text, 'lxml')
    rows = bsObj.findAll('td')   

    cnt = 0
    for row in rows:
        rowa = row.findAll('a')
        if len(rowa) > 0:
            for item in rowa:
                _book_url = item.get('href')
                if 'cards' in _book_url:
                    card_list.append(_book_url.split('/')[2])
                    book_name_list.append(item.get_text())
                    book_url_list.append(_book_url.replace('../', url_top))
                    cnt += 1
        if cnt >= 5:
            break

    time.sleep(1)



# 詳細URLの中身から著者名&zipのURLを取得
for i, url in enumerate(book_url_list):
    html = requests.get(url)
    html.encoding = 'utf-8'
    bsObj = BeautifulSoup(html.text, 'lxml')
    rows = bsObj.findAll('a')
    zip_flag = False

    cnt = 0
    for row in rows:

        if 'zip' in str(row.get('href')):
            zip_url_list.append(row.get('href').replace('./', url_top+"cards/"+card_list[i]+"/"))
            zip_flag = True

        if 'person' in str(row.get('href')):
            cnt += 1
            if cnt == 2:
                person_list.append(row.get_text())

    if not zip_flag:
        zip_url_list.append(None)


#zipファイルをまとめてダウンロード&解凍&リネーム
for i, url in enumerate(zip_url_list):

    if url is None:
        txt_filename_list.append(None)
        continue

    zip_name = url.split('/')[-1]
    res = requests.get(url,stream=True)
    if res.status_code == 200:
        with open(zip_name, 'wb') as file:
                for chunk in res.iter_content(chunk_size=1024):
                    file.write(chunk)

    with zipfile.ZipFile(zip_name, 'r') as myzip:
        myzip.extractall()
        for info in myzip.infolist():
            new_filename = str(i+1).zfill(2)+"_"+book_name_list[i]+'_'+person_list[i]+'.txt'
            txt_filename_list.append(new_filename)
            if not os.path.exists(new_filename): #リネーム後のファイルがなければリネーム
                os.rename(info.filename, new_filename)
            else: #リネーム後のファイルがある場合は、リネーム前のファイルを削除(不要のため)
                os.remove(info.filename)

    os.remove(zip_name)

csv_data = []
csv_data.append("作品名,作家名,ファイル名\n")

for i, book_name in enumerate(book_name_list):
    if txt_filename_list[i] is None:
        txt_filename = "zipファイルなし"
    else:
        txt_filename = txt_filename_list[i]

    csv_data.append(book_name+','+person_list[i]+','+txt_filename+'\n')

# ファイル書き出し
with open('00_book-list.csv', 'w', encoding='shift_jis') as f:
    f.writelines(csv_data)

