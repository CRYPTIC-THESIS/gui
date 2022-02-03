import pandas as pd

def ema_smoothing(trend_df):
    cols = list(trend_df.columns) 
    dates= trend_df ['date']
    crypto = trend_df [cols[1]]

    def calculate_ema(prices, days, smoothing=2):
        ema = [sum(prices[:days]) / days]
        for price in prices[days:]:
            ema.append((price * (smoothing / (1 + days))) + ema[-1] * (1 - (smoothing / (1 + days))))
        return ema

    ema = calculate_ema(crypto, 12)
    ema = pd.DataFrame(ema,columns=[cols[1]])
    
    for i in range(11):
        ema.loc[-1] = [trend_df[cols[1]].iloc[i]]  # adding a row
        ema.index = ema.index + 1  # shifting index
        ema.sort_index(inplace=True)

    final_ema = pd.concat([dates,ema],axis = 1)
    final_ema.rename(columns={'0':cols[1]},inplace=True)
    return final_ema

#=====TEST INPUT/RUN=====
#test = dbconnect.get_data_table('Google_Data')
#trend = test['btc']
#date = test['date']
#print(ema_smoothing(trend,date))

