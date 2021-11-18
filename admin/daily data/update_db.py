from pycoingecko import CoinGeckoAPI
from datetime import datetime, timedelta
import time as t
import calendar
import pandas as pd

from dbconnect import *
cg = CoinGeckoAPI()

# REALTIME
def get_cur():
    d_ = datetime.strptime('2021-10-18 07:00:00', '%Y-%m-%d %H:%M:%S')
    t = d_ - timedelta(days = 1)
    u_d = calendar.timegm(d_.utctimetuple())
    u_t = calendar.timegm(t.utctimetuple())

    btc = list()
    eth = list()
    doge = list()

    b = cg.get_coin_market_chart_range_by_id(id='bitcoin',vs_currency='usd',from_timestamp=u_t,to_timestamp=u_d)
    btc_p = b.get('prices')

    e = cg.get_coin_market_chart_range_by_id(id='ethereum',vs_currency='usd',from_timestamp=u_t,to_timestamp=u_d)
    eth_p = e.get('prices')

    d = cg.get_coin_market_chart_range_by_id(id='dogecoin',vs_currency='usd',from_timestamp=u_t,to_timestamp=u_d)
    doge_p = d.get('prices')
    
    lst = [btc_p, eth_p, doge_p]
    for i, c in enumerate(lst):
        for val in c:
            date = datetime.fromtimestamp(val[0] / 1e3).strftime('%Y-%m-%d')
            if date == d_.strftime('%Y-%m-%d'):
                if i == 0: btc.append(val)
                if i == 1: eth.append(val)
                if i == 2: doge.append(val)
    

    btc = [val[1] for val in btc]
    btc_o = btc[0]
    btc_c = btc[-1]
    btc_h = max(btc)
    btc_l = min(btc)
    btc_f = [u_d, btc_o, btc_h, btc_l, btc_c]

    
    eth = [val[1] for val in eth]
    eth_o = eth[0]
    eth_c = eth[-1]
    eth_h = max(eth)
    eth_l = min(eth)
    eth_f = [u_d, eth_o, eth_h, eth_l, eth_c]

    
    doge = [val[1] for val in doge]
    doge_o = doge[0]
    doge_c = doge[-1]
    doge_h = max(doge)
    doge_l = min(doge)
    doge_f = [u_d, doge_o, doge_h, doge_l, doge_c]

    print(btc, eth, doge)

    columns = ['Timestamp', 'Open', 'High', 'Low', 'Closing']
    btc = pd.DataFrame(columns=columns).append(pd.Series(btc, index=columns), ignore_index=True)
    eth = pd.DataFrame(columns=columns).append(pd.Series(eth, index=columns), ignore_index=True)
    doge = pd.DataFrame(columns=columns).append(pd.Series(doge, index=columns), ignore_index=True)

    print(btc, eth, doge)

    return btc, eth, doge, btc_f, eth_f, doge_f

def update_realtime_data():
    
    btc, eth, doge = get_cur()
    print('update 15 mins')
    update_realtime('Realtime_BTC', btc)
    update_realtime('Realtime_ETH', eth)
    update_realtime('Realtime_DOGE', doge)

def new_realtime():
    
    btc, eth, doge = get_cur()
    # insert_realtime_data('Realtime_BTC', btc)
    # insert_realtime_data('Realtime_ETH', eth)
    # insert_realtime_data('Realtime_DOGE', doge)

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


# TWITTER
import snscrape.modules.twitter as sntwitter
import csv

#Input is the Date Yesterday and current Date in YYYY-MM-DD string format
def scrape_daily_tweets(dateYesterday,dateToday):
    maxTweets = 1000000

    print ("[!] Scraping Start !!!")

    cryptoData = pd.DataFrame({'searchTerm':['#bitcoin OR #btc','#ethereum OR #eth','#dogecoin OR #doge'],'dailyDataName':['gui/admin/modules/Trends/BTC_Daily.csv','gui/admin/modules/Trends/ETH_Daily.csv','gui/admin/modules/Trends/DOGE_Daily.csv'],'cryptoName':['bitcoin','ethereum','dogecoin']})
    dateSince = dateYesterday #Get Yesterday's Date
    dateUntil = dateToday #Get Today's Date

    #=====================================================================================================================
    #Get Twitter Data
    for index, col in cryptoData.iterrows():
        #Set Snscrape parameters
        twitterScraperParams = str(str(col["searchTerm"]) + ' + since:' + str(dateSince) + ' until:' + str(dateUntil) +  ' -filter:links -filter:replies')
        
        #Set FileName
        fileName = str(col["dailyDataName"])
        csvFile = open(fileName, 'w', newline='', encoding='utf8')

        #Use csv writer
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['id','Date','username','tweet']) 

        # DATAFRAME
        # columns = ['id','Date','username','tweet']
        # df_btc = pd.DataFrame(columns=columns)

        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(twitterScraperParams).get_items()):
                if i > maxTweets :
                    break  
                if (i%10000==0):
                    print(i) 
                csvWriter.writerow([tweet.id, tweet.date, tweet.user.username, tweet.content])
        csvFile.close()
        print ("[!] Scraping Done !!!")

    #=====================================================================================================================
    #Remove Duplicate Data
    for index, col in cryptoData.iterrows():
        #Set FileName
        fileName = str(col["dailyDataName"])

        #Open
        data = pd.read_csv(fileName)

        #Split Date column
        data[['Date', 'time']] = data["Date"].str.split(" ", 1, expand=True)

        #New dataframe
        newdata_cols = ['Date', 'time' , 'username', 'tweet']
        newdata = pd.DataFrame(data[['Date', 'time', 'username', 'tweet']].values, columns = newdata_cols)

        #Reverse Data Order
        newdata = newdata[::-1].reset_index(drop = True)

        #Print total Raw Data Rows
        rows  = newdata.count()[0]
        print ("\nNo. of Rows (Raw): " + str(rows) + "\n")
        print (newdata[['Date','time','username']].head(5))
        print (newdata[['Date','time','username']].tail(5))

        #Drop Duplicate Username on the same day
        newdata.drop_duplicates(subset=['Date','username'], keep='first', inplace=True)

        #Save filtered data
        newdata.to_csv(fileName, mode='w', index=False, header=True)

        #Print total Filtered Data Rows
        filtered_data = pd.read_csv(fileName)
        rows  = filtered_data.count()[0]
        print ("\nNo. of Rows (Filtered): " + str(rows) + "\n")
        print (filtered_data[['Date','time','username']].head(5))
        print (filtered_data[['Date','time','username']].tail(5))

    #=====================================================================================================================
    #Total the Data
    twitter_daily_total = pd.DataFrame({'Date':[dateSince],'bitcoin':[0],'ethereum':[0],'dogecoin':[0]})

    for index, col in cryptoData.iterrows():
        #Set FileName
        fileName = str(col["dailyDataName"])

        #Open 
        data = pd.read_csv(fileName)

        #New dataframe
        data_cols = ['Date']
        data = pd.DataFrame(data[['Date']], columns = data_cols)

        #Print total Rows
        rows  = data.count()[0]
        print ("\nNo. of Rows: " + str(rows) + "\n")

        i=0
        for index, row in data.iterrows():
            if (row["Date"]!=(twitter_daily_total.loc[i,"Date"])):
                i = i + 1
                twitter_daily_total.loc[i,"Date"]=row["Date"]
                twitter_daily_total.loc[i,str(col["cryptoName"])] = 0
                twitter_daily_total.loc[i,str(col["cryptoName"])]= twitter_daily_total.loc[i,str(col["cryptoName"])] + 1
            else:
                twitter_daily_total.loc[i,str(col["cryptoName"])]= twitter_daily_total.loc[i,str(col["cryptoName"])] + 1

    update_trend('Twitter_Data',twitter_daily_total)


# GOOGLE TRENDS
from pytrends.request import TrendReq

def scrape_google_data(currDate): #currDate in YYYY-MM-DD format
    dfGoogle = get_data_table('Google_Data')
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
        update_trend('Google_Data',total_data)
    else:
        print('Scrape Google trends data on ' + str(endOfTheWeekDate))
    
#scrape_google_data('2021-11-02') #sample run

new_realtime()

# RUN FOREVER
# while True:
#     sleep = 10
    
#     time = datetime.now().strftime("%H:%M")

#     today = datetime.now().strftime("%Y-%m-%d")
#     past = pd.to_datetime(today) - timedelta(days=1)
#     past = past.strftime("%Y-%m-%d")

#     forward = (datetime.strptime(time, "%H:%M") + timedelta(minutes=10)).strftime("%H:%M")
#     temp = datetime.strptime('23:55', "%H:%M") - datetime.strptime(time, "%H:%M")
#     temp = int(t.strftime("%M", t.gmtime(temp.total_seconds())))
    
#     try:
#         print(time)
#         if time >= '23:55':
#             update_crypto_data()
#             new_realtime()
#         else:
#             update_realtime_data()

#             if forward.startswith('00') and time.startswith('23') and temp < 15:
#                 sleep = temp
#     except Exception as e:
#         print(e)
#         sleep = 1
    
#     # if time >= '23:55':
#     #     scrape_daily_tweets(past, today)
#     #     scrape_google_data(today)

#     t.sleep(60*sleep)