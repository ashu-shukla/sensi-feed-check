from datetime import datetime
import requests
import json
import nsefetch as ns

nse_status = 'https://www.nseindia.com/api/marketStatus'
today = datetime.today().strftime('%d-%b-%Y')  # DD-MMM-YYYY
discord = 'https://discord.com/api/webhooks/878985323009425468/1kUcjWjnB5UJTbMaUV_Pfmt_lSACqagVwq37GhwzJXJWMEFAIDWvjz5uWhzrkS-iCQBq'

f = open('recent.json')
data = json.load(f)
op = ns.nsefetch(nse_status)
capital_market = op['marketState'][0]
if capital_market['marketStatus'] == "Open":
    requests.post(discord, data={"content": "Capital Market is open today!"})
    data['was_market_open_today'] = "yes"
    with open('recent.json', 'w') as jf:
        json.dump(data, jf)
else:
    requests.post(discord, data={"content": "Capital Market is closed today!"})
    data['was_market_open_today'] = "no"
    with open('recent.json', 'w') as jf:
        json.dump(data, jf)
