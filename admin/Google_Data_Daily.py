from pytrends.request import TrendReq
import dbconnect as db
import pandas as pd
import datetime

def scrape_google_data(currDate): #currDate in YYYY-MM-DD format
    dfGoogle = db.get_data_table('Google_Data')
    lastDate = dfGoogle.loc[(len(dfGoogle)-1),'date']
    lastDate = datetime.datetime.strptime(lastDate,'%Y-%m-%d')
    NextDay_Date = lastDate + datetime.timedelta(days=8)
    endOfTheWeekDate = NextDay_Date.strftime ('%Y-%m-%d')

    #currDate = '2021-10-30' #for testing

    if (currDate==endOfTheWeekDate):
        print('[!] Google Trends Data Scraping Starts')

        dateToday = currDate
        dateRange = '2019-12-25 ' + dateToday

        pytrends = TrendReq(hl='en-Worldwide',tz=360)
        keyword = ['Bitcoin','btc']
        pytrends.build_payload(kw_list=keyword, cat=0, timeframe=dateRange, geo='',gprop='')
        btcTrends = pytrends.interest_over_time()

        pytrends = TrendReq(hl='en-Worldwide',tz=360)
        keyword = ['Ethereum','eth']
        pytrends.build_payload(kw_list=keyword, cat=0, timeframe=dateRange, geo='',gprop='')
        ethTrends = pytrends.interest_over_time()

        pytrends = TrendReq(hl='en-Worldwide',tz=360)
        keyword = ['Dogecoin','doge']
        pytrends.build_payload(kw_list=keyword, cat=0, timeframe=dateRange, geo='',gprop='')
        dogTrends = pytrends.interest_over_time()

        dfBtc = pd.DataFrame(btcTrends.drop(labels=['isPartial'],axis='columns'))
        dfEth = pd.DataFrame(ethTrends.drop(labels=['isPartial'],axis='columns'))
        dfDog = pd.DataFrame(dogTrends.drop(labels=['isPartial'],axis='columns'))

        dfBtc = pd.DataFrame(dfBtc.sum(axis=1),columns=['bitcoin'])
        dfBtc.reset_index(inplace=True)
        dfEth = pd.DataFrame(dfEth.sum(axis=1),columns=['ethereum'])
        dfEth.reset_index(inplace=True)
        dfDog = pd.DataFrame(dfDog.sum(axis=1),columns=['dogecoin'])
        dfDog.reset_index(inplace=True)

        btcEth = dfBtc.join(dfEth.set_index('date'), on="date")
        dogBtcEth = dfDog.join(btcEth.set_index('date'), on="date")

        total_data = pd.DataFrame({'Date':[''],'bitcoin':[0],'ethereum':[0],'dogecoin':[0]})

        i=0
        for index, row in dogBtcEth.iterrows():
            NextDay_Date_Formatted = row['date'].strftime('%Y-%m-%d')
            total_data.loc[i,'Date'] = NextDay_Date_Formatted
            total_data.loc[i,'bitcoin']  = row['bitcoin']
            total_data.loc[i,'ethereum'] = row['ethereum']
            total_data.loc[i,'dogecoin'] = row['dogecoin']
            for j in range (7):
                i = i + 1
                NextDay_Date = row['date'] + datetime.timedelta(days=j+1)
                NextDay_Date_Formatted = NextDay_Date.strftime ('%Y-%m-%d')
                total_data.loc[i,'Date'] = NextDay_Date_Formatted
                total_data.loc[i,'bitcoin']  = row['bitcoin']
                total_data.loc[i,'ethereum'] = row['ethereum']
                total_data.loc[i,'dogecoin'] = row['dogecoin']

        total_data = total_data.iloc[:-1 , :]
        total_data = total_data.tail(7)
        print(total_data)
        db.update_trend('Google_Data',total_data)
    else:
        print('Scrape Google trends data on ' + str(endOfTheWeekDate))
    
#scrape_google_data('2021-11-02') #sample run