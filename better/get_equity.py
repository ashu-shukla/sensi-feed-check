from mongoDB import equity
from nsefetch import nsefetch
from datetime import datetime, timedelta
from update_master import ismarketOpen
from time import sleep

# today = datetime.today()-timedelta(days=1)
today = datetime.today()
today_str = today.strftime('%d-%b-%Y')  # DD-MMM-YYYY


if ismarketOpen():
    while True:
        main = {}
        dii_data = {}
        fii_data = {}
        url = 'https://www.nseindia.com/api/fiidiiTradeReact'
        js = nsefetch(url)
        # print(js[0]['date'], fii_stats_date_format)
        if js[0]['date'] == today_str:
            dii_data['buy'] = float(js[0]['buyValue'])
            dii_data['sell'] = float(js[0]['sellValue'])
            dii_data['net'] = float(js[0]['netValue'])
            fii_data['buy'] = float(js[1]['buyValue'])
            fii_data['sell'] = float(js[1]['sellValue'])
            fii_data['net'] = float(js[1]['netValue'])
            main['dii'] = dii_data
            main['fii'] = fii_data
            equity(main)
            break
        else:
            sleep(600)
