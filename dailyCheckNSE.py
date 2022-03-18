from datetime import datetime
import requests
import feedparser
import json
from time import sleep
import nsefetch as ns

today = datetime.today().strftime('%d-%b-%Y')  # DD-MMM-YYYY

discord = 'https://discord.com/api/webhooks/878985323009425468/1kUcjWjnB5UJTbMaUV_Pfmt_lSACqagVwq37GhwzJXJWMEFAIDWvjz5uWhzrkS-iCQBq'
feed_url = 'https://feeds.feedburner.com/nseindia/FODailyReport'
fii_dii_url = 'https://www.nseindia.com/api/fiidiiTradeReact'

fao_flag = True
fii_dii_flag = True

# Check for daily participant wise fao data.
requests.post(discord, data={
              "content": 'Shell Script started, checking for OI data every 5mins...'})

f = open('recent.json')
recent_data = json.load(f)

if recent_data['was_market_open_today'] != 'no':
    while fao_flag:
        data = feedparser.parse(feed_url)
        for entry in data.entries:
            if entry.title == 'Participant wise Open Interest':
                if entry.link != recent_data['Participant wise Open Interest']:
                    recent_data['Participant wise Open Interest'] = entry.link
                    requests.post(discord, data={
                        "content": 'Participant wise open interest details is now available on NSE!'})
                    with open('recent.json', 'w') as jf:
                        json.dump(recent_data, jf)
                    fao_flag = False
                    break
        else:  # Executes only if break is not triggered in inner loop.
            sleep(298)
            continue
        break

    # Check for daily cash activity data on NSE website.
    requests.post(
        discord, data={"content": "Now Checking for cash data every 15mins..."})
    while fii_dii_flag:
        op = ns.nsefetch(fii_dii_url)
        if op[0]['date'] == today:
            requests.post(
                discord, data={"content": "Cash Data is now available on NSE!"})
            fii_dii_flag = False
            break
        sleep(900)
requests.post(discord, data={"content": "Closing Script"})
