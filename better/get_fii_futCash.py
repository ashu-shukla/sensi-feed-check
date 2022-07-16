from time import sleep
import pandas as pd
import json
from datetime import datetime, timedelta
from mongoDB import fii_future
from update_master import isFiiDeri, ismarketOpen

# today = datetime.today()-timedelta(days=1)
today = datetime.today()
today_str = today.strftime('%d-%b-%Y')  # DD-MMM-YYYY

if ismarketOpen():
    while True:
        if isFiiDeri():
            fii_stats = f'https://www1.nseindia.com/content/fo/fii_stats_{today_str}.xls'
            df = pd.read_excel(fii_stats, nrows=6)
            df = df[2:]
            df.columns = ['Derivative Products', 'Contracts Bought', 'Buy in Crores',
                          'Contracts Sold', 'Sell in Crores', 'OI', 'OI in Crores']
            df['Buy in Crores'] = pd.to_numeric(df['Buy in Crores'])
            df['Sell in Crores'] = pd.to_numeric(df['Sell in Crores'])
            df['Net in Crores'] = df['Buy in Crores'] - df['Sell in Crores']
            fii_fut = df[0:1]
            fii_fut = fii_fut[['Buy in Crores',
                               'Sell in Crores', 'Net in Crores', 'OI']]
            fii_fut.columns = ['buy', 'sell', 'net', 'oi']
            fii_fut = fii_fut.apply(pd.to_numeric)
            js = json.loads(fii_fut.to_json(orient='records'))
            # print(df)
            fii_future(js[0])
            break
        else:
            sleep(300)
