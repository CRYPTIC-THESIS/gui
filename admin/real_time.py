from pycoingecko import CoinGeckoAPI
from datetime import datetime, timedelta
import calendar
import pandas as pd

from dbconnect import *
cg = CoinGeckoAPI()

def get_cur():
    d = datetime.utcnow()
    t = datetime.utcnow() - timedelta(days = 1 )
    u_d = calendar.timegm(d.utctimetuple())
    u_t = calendar.timegm(t.utctimetuple())

    b = cg.get_coin_market_chart_range_by_id(id='bitcoin',vs_currency='usd',from_timestamp=u_t,to_timestamp=u_d)
    btc = b.get('prices')
    btc = [val[1] for val in btc]
    btc_o = btc[0]
    btc_c = btc[-1]
    btc_h = max(btc)
    btc_l = min(btc)
    btc = [u_d, btc_o, btc_h, btc_l, btc_c]

    e = cg.get_coin_market_chart_range_by_id(id='ethereum',vs_currency='usd',from_timestamp=u_t,to_timestamp=u_d)
    eth = e.get('prices')
    eth = [val[1] for val in eth]
    eth_o = eth[0]
    eth_c = eth[-1]
    eth_h = max(eth)
    eth_l = min(eth)
    eth = [u_d, eth_o, eth_h, eth_l, eth_c]

    d = cg.get_coin_market_chart_range_by_id(id='dogecoin',vs_currency='usd',from_timestamp=u_t,to_timestamp=u_d)
    dog = d.get('prices')
    dog = [val[1] for val in dog]
    dog_o = dog[0]
    dog_c = dog[-1]
    dog_h = max(dog)
    dog_l = min(dog)
    doge = [u_d, dog_o, dog_h, dog_l, dog_c]

    # print(btc, eth, doge)

    columns = ['Timestamp', 'Open', 'High', 'Low', 'Closing']
    btc = pd.DataFrame(columns=columns).append(pd.Series(btc, index=columns), ignore_index=True)
    eth = pd.DataFrame(columns=columns).append(pd.Series(eth, index=columns), ignore_index=True)
    doge = pd.DataFrame(columns=columns).append(pd.Series(doge, index=columns), ignore_index=True)

    # print(btc, eth, doge)

    return btc, eth, doge


def update_realtime_data():
    
    btc, eth, doge = get_cur()
    update_realtime('Realtime_BTC', btc)
    update_realtime('Realtime_ETH', eth)
    update_realtime('Realtime_DOGE', doge)


def update_crypto_data():
    # Convert timestamp
    def timestamp_to_date(df):
        date = []
        for i in range(len(df)):
            date.append(dt.fromtimestamp(int(float(df[i]))).strftime('%m/%d/%Y'))
        return date

    btc, eth, doge = get_cur()

    btc['Timestamp'] = timestamp_to_date(btc['Timestamp'])
    eth['Timestamp'] = timestamp_to_date(eth['Timestamp'])
    doge['Timestamp'] = timestamp_to_date(doge['Timestamp'])

    columns = ['Date', 'Open', 'High', 'Low', 'Price']
    btc.columns = columns
    eth.columns = columns
    doge.columns = columns

    # print(btc)
    # print(eth)
    # print(doge)

    update_crypto('Bitcoin_Data', btc)
    update_crypto('Ethereum_Data', eth)
    update_crypto('Dogecoin_Data', doge)