# セルは必要に応じて増やしてよい。
import requests

def get_json(url, param):
    '''access to WebAPI'''
    
    jsonData = requests.get(url,param)
    return jsonData.json()

def station_to_postal(station):
    '''駅名から郵便番号'''
    
    param = { 'method': 'getStations', 'name' : station}
    url = 'http://express.heartrails.com/api/json'
    data = get_json(url, param)
    postal = data['response']['station'][0]['postal']
    return postal
    
def postal_to_address(postal):
    '''郵便番号から住所'''
    param = { 'zipcode': postal}
    url = 'https://zipcloud.ibsnet.co.jp/api/search'
    data = get_json(url, param)
    address1 = data['results'][0]['address1']
    address2 = data['results'][0]['address2']
    address3 = data['results'][0]['address3']
    return ' '.join([address1, address2, address3])



station = '磯子'

postal = station_to_postal(station)
address = postal_to_address(postal)
print('駅名:', station)
print('郵便番号:', postal)
print('住所:', address)
