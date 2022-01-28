import pandas_ta as ta
import yfinance as yf
import pandas as pd

def get_decision(crypto):

    #Get Data
    df = yf.Ticker(crypto+'-USD').history(period='1y')[['Close', 'Open', 'High', 'Volume', 'Low']]
    # MACD
    da = df
    da.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)

    #RSI
    dr = pd.DataFrame(columns=['price'])
    dr['price'] = df['Close']
    dr.ta.rsi(close='price', length=14, append=True)
    # View the result
    rsi = dr['RSI_14'].tail(1).squeeze()

    #STOCHASTIC
    do = pd.DataFrame()
    do = df
    do.drop('Volume', axis=1, inplace=True)
    do.ta.stoch(high='High', low='Low', k=14, d=3, append=True)

    dc = do[['MACD_12_26_9', 'MACDh_12_26_9', 'MACDs_12_26_9', 'STOCHk_14_3_3', 'STOCHd_14_3_3']].tail(1).squeeze()

    ## print(dc)

    macd = dc[0]
    macdh = dc[1]
    macds = dc[2]
    sok = dc[3]
    sod = dc[4]

    #RULES

    #RSI
    if(rsi<100):
        if(rsi<70):
            if(rsi<30):
                rsi_v = "BUY NOW!"
            else: rsi_v = "HOLD"
        else: rsi_v = "SELL NOW!"
    else: rsi_v = "WRONG VALUE"

    #MACD
    if(macd < macds):
        macd_v = "BUY NOW!"
    elif(macd == macds):
        macd_v = "HOLD"
    else:
        macd_v = "SELL NOW!"

    #SO   
    if(sok<100):
        if(sok<80):
            if(sok<20):
                if (sok > sod):
                    so_v = "BUY NOW!"
                else:
                    so_v = "PREPARE TO BUY"
            else: so_v = "HOLD"
        else:
            if (sok > sod):
                so_v = "PREPARE TO SELL"
            else:
                so_v = "SELL NOW!"
    else:
        so_v = "WRONG VALUE"

    #DECISION
    if (rsi_v == macd_v == so_v):
        des = so_v
    elif ((rsi == macd_v) != so_v ):
        if so_v == "PREPARE TO BUY" or so_v == "PREPARE TO SELL":
            des = so_v
        else:
            des = rsi_v
    elif ((so_v == macd_v) != rsi_v ):
        des = so_v
    elif ((rsi_v == so_v) != macd_v ):
        des = rsi_v
    else:
        des = so_v

    return des