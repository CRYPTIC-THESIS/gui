#import numpy as np
#import matplotlib.pyplot as plt
#import dbconnect
import pandas as pd

def ema_smoothing(trenddf,dates): # Parameter needed is a column of a table in the database (Ex. in Twitter_Data, the df['btc'] and df['date'] is needed). See the TEST INPUT/RUN
    def calculate_ema(prices, days, smoothing=2):
        ema = [sum(prices[:days]) / days]
        for price in prices[days:]:
            ema.append((price * (smoothing / (1 + days))) + ema[-1] * (1 - (smoothing / (1 + days))))
        return ema

    ema = calculate_ema(trenddf, 12)

    #For Plotting
    '''    
    price_X = np.arange(trenddf.shape[0]) # Creates array [0, 1, 2, 3, ..., df.shape[0]]
    ema_X = np.arange(12, trenddf.shape[0]+1) # Creates array [12, 13, 14, 15, ..., df.shape[0]+1]
                                        # We start at 10, because we use the first 10 values to calculate the SMA,
                                        # then we calculate EMA form the 11th value    
    plt.xlabel('Days')
    plt.ylabel('Trend Volume')
    plt.plot(price_X, trenddf, label='Trend Volume')
    plt.plot(ema_X, ema, label='EMA')
    plt.legend()
    plt.show()
    '''
    ema = pd.DataFrame(ema)

    for i in range(11):
        ema.loc[-1] = [0]  # adding a row
        ema.index = ema.index + 1  # shifting index
        ema.sort_index(inplace=True)

    final_ema = pd.concat([dates,ema],axis = 1)
    return final_ema

#=====TEST INPUT/RUN=====
#test = dbconnect.get_data_table('Google_Data')
#trend = test['btc']
#date = test['date']
#print(ema_smoothing(trend,date))

