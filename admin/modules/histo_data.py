# import sys 
# sys.path.append('..')
import yfinance as yahooFinance
from datetime import datetime, timedelta

def get_histo(startdate,enddate,crypto):
    
    startDate = datetime.strptime(startdate, '%Y-%m-%d')
    startDate+=timedelta(1)
   
    endDate = datetime.strptime(enddate, '%Y-%m-%d')
    endDate+=timedelta(1)

    GetFacebookInformation = yahooFinance.Ticker(crypto+'-USD')
    
    # pass the parameters as the taken dates for start and end
    df = GetFacebookInformation.history(start=startDate, end=endDate)[['Close', 'Open', 'High', 'Low']]
    df.reset_index(inplace=True)

    return df
    
def get_current(crypto):
    
    GetFacebookInformation = yahooFinance.Ticker(crypto+'-USD')
    
    # pass the parameters as the taken dates for start and end
    df = GetFacebookInformation.history(period='24h', interval='15m')[['Close', 'Open', 'High', 'Low']]
    df.drop(df.tail(1).index,inplace=True)

    return df

def get_histo_dash(period, crypto):

    GetFacebookInformation = yahooFinance.Ticker(crypto+'-USD')
    
    # pass the parameters as the taken dates for start and end
    df = GetFacebookInformation.history(period=period)[['Close', 'Open', 'High', 'Low']]

    return df


#sample use
# data = get_histo('2020-01-01', '2020-01-31','DOGE')
# print(data)
# data.to_csv('csv/samp_apidata.csv')
