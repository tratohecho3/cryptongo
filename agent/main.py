import pymongo
import requests

API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

def get_db_connection(uri):
    client = pymongo.MongoClient(uri)
    return client.cryptongo

def get_cryptocurrencies_from_api():
    r = requests.get(API_URL)
    if r.status_code == 200:
        result = r.json()
        return result
    raise Exception('API Error')