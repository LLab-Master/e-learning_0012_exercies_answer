import requests

def download_file(url):
    s = url.split('/')
    filename = s[-1]
    
    res = requests.get(url,stream=True)
    if res.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in res.iter_content(chunk_size=1024):
                file.write(chunk)
download_file('https://upload.wikimedia.org/wikipedia/ja/5/5f/Mt_Fuji_at_Nihondaira.jpg')
download_file('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Tokyo_Tower_and_around_Skyscrapers.jpg/300px-Tokyo_Tower_and_around_Skyscrapers.jpg')