import nsefetch as ns
from update_master import send_message, update_master

nse_status = 'https://www.nseindia.com/api/marketStatus'
op = ns.nsefetch(nse_status)
capital_market = op['marketState'][0]

if capital_market['marketStatus'] == "Open":
    send_message("Capital Market is open today!")
    update_master('market_open_today', True)
else:
    send_message("Capital Market is closed today!")
    update_master('market_open_today', False)
