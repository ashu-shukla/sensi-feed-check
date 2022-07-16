# SensiBear 🐻

## Introduction

The one stop place to wreck my boi Abid's software the useless-bull.\
It is as of now built to provide nothing!\
And is just for a parody unless i start seeing some sick profits out of this.

## The Backend

Unlike Postgres Version this is way independent of each other.\
If market is open only then all of this works.
Any data of that day gets updated at any time independent of each other.

## Scripts and their purpose in order

1. Check if market is open today and update master.

   - marketOpen.py
   - master.json

2. First get off candlesticks, close and date info and add to mongodb and create a new doc.

   - get_candlesticks.py

3. Then use loops to check for data availability of other info and update that days doc with the info.

   - get_equity.py
   - get_fao_oi.py
   - get_fut_fii.py

4. Difference between each day's data will be handled by frontend this time.

5. Keep track of all that is being pushed in a seperately and reset after complete push.

   - master.json
   - updation_master.py

## Process

1. 9:30am Market Open Runs and updates master.
2. 4:00pm Candles Run, create new doc in mongo and update master.
3. 6:45pm OI, Equity and Fut Run until data is fetched then, update in mongo and master.json
4. If all the data is added the master is reset for next day.
