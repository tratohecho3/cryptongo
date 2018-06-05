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

def save_ticker(db_connection, ticker_data=None):
    if not ticker_data:
        return False
    if check_if_exists():
        return False
    
    ticker_data['rank'] = int(ticker_data['rank'])
    ticker_data['last_updated'] = int(ticker_data['last_updated'])
    db_connection.tickers.insert_one(ticker_data)
    return True

def check_if_exists(db_connection, ticker_data):
    if db_connection.tickers.find_one({'ticker_hash': 's'}):
        return True
    return False
