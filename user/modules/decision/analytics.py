import pandas_ta as ta
import yfinance as yf
import pandas as pd

#Get Data
df = yf.Ticker('BTC-USD').history(period='1y')[['Close', 'Open', 'High', 'Volume', 'Low']]
# MACD
da = df
da.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)
# View result
pd.set_option("display.max_columns", None)  # show all columns
print(da)
dr = pd.DataFrame(columns=['price'])
dr['price'] = df['Close']
#RSI
dr.ta.rsi(close='price', length=14, append=True)
# View the result
print(dr)

