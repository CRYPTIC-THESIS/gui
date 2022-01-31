import yfinance as yahooFinance
from datetime import timedelta
import datetime

def get_histo(startdate,enddate,crypto):
    
    
    startDate = datetime.datetime.strptime(startdate, '%Y-%m-%d')
    startDate+=timedelta(1)
   
    endDate = datetime.datetime.strptime(enddate, '%Y-%m-%d')

    GetFacebookInformation = yahooFinance.Ticker(crypto+'-USD')
    
    # pass the parameters as the taken dates for start and end
    df = GetFacebookInformation.history(start=startDate, end=endDate)[['Close', 'Open', 'High', 'Low']]

    return df

#sample use
#data = get_histo("2020-1-1","2021-10-31",'DOGE')
