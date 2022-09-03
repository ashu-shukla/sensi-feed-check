from datetime import date, timedelta
import pymongo

from update_master import update_master
client = pymongo.MongoClient(
    "MongoURL")

# today = date.today()-timedelta(days=1)
today = date.today()
today_str = today.strftime('%Y-%m-%d')  # yyyy-mm-dd

db = client['sensibear']
master = db['master']

# print(db.list_collection_names())

# Add and create record with date, candle and close


def candles(data):
    master.insert_one(data)
    update_master('candles', True)

# Add Cash data to record


def equity(data):
    query = {'date': today_str}
    newval = {'$set': {'cash': data}}
    master.update_one(query, newval)
    update_master('equity', True)

#  Add OI data to record


def fao_oi(data):
    query = {'date': today_str}
    newval = {'$set': {'oi': data}}
    master.update_one(query, newval)
    update_master('oi', True)

#  Add FII stats to record


def fii_future(data):
    query = {'date': today_str}
    newval = {'$set': {'fii_future_crores': data}}
    master.update_one(query, newval)
    update_master('fii_fut', True)
