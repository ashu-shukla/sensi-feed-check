import json
import requests
import feedparser

feed_url = 'https://feeds.feedburner.com/nseindia/FODailyReport'

# Send any message to discord.


def send_message(msg):
    discord = 'Discord url'
    requests.post(discord, data={"content": f"{msg}"})

#  Reset master.json


def master_reset():
    data = {
        "market_open_today": False,
        "candles": False,
        "equity": False,
        "oi": False,
        "fii_fut": False
    }
    with open('master.json', 'w') as jf:
        json.dump(data, jf)

# Check if all values in master.json are true or not.


def checkall():
    f = open('master.json')
    data = json.load(f)
    istrue = True
    for key in data:
        if not data[key]:
            istrue = False
            break
    if istrue:
        send_message('All Updated, resetting the master log.')
        master_reset()

# Update any value in master.json


def update_master(name, val):
    f = open('master.json')
    data = json.load(f)
    data[name] = val
    with open('master.json', 'w') as jf:
        json.dump(data, jf)
    checkall()

# Returns market open status from master.json


def ismarketOpen():
    f = open('master.json')
    data = json.load(f)
    return data['market_open_today']

# Checks if OI data is available in RSS feed or not.


def isOiDataAvailable():
    data = feedparser.parse(feed_url)
    isthere = False
    for entry in data.entries:
        if entry.title == 'Participant wise Open Interest':
            isthere = True
            break
        else:
            isthere = False
    return isthere

# Checks if FII statistics data is present in RSS feed or not.


def isFiiDeri():
    data = feedparser.parse(feed_url)
    isthere = False
    for entry in data.entries:
        if entry.title == 'FII derivatives statistics':
            isthere = True
            break
        else:
            isthere = False
    return isthere
