from pycoingecko import CoinGeckoAPI
from datetime import datetime, timedelta, date
import time as t
import calendar
import pandas as pd

from dbconnect import *
cg = CoinGeckoAPI()

# REALTIME
def get_cur():
    d_ = datetime.utcnow()
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
    btc = pd.DataFrame(columns=columns).append(pd.Series(btc_f, index=columns), ignore_index=True)
    eth = pd.DataFrame(columns=columns).append(pd.Series(eth_f, index=columns), ignore_index=True)
    doge = pd.DataFrame(columns=columns).append(pd.Series(doge_f, index=columns), ignore_index=True)

    print(btc, eth, doge)

    return btc, eth, doge, # btc_f, eth_f, doge_f

def update_realtime_data():
    
    btc, eth, doge = get_cur()
    print('update 15 mins')
    update_realtime('Realtime_BTC', btc)
    update_realtime('Realtime_ETH', eth)
    update_realtime('Realtime_DOGE', doge)

def new_realtime():
    
    btc, eth, doge = get_cur()
    insert_realtime_data('Realtime_BTC', btc)
    insert_realtime_data('Realtime_ETH', eth)
    insert_realtime_data('Realtime_DOGE', doge)

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


# TWITTER VOLUME DATA
import snscrape.modules.twitter as sntwitter

#Input is the Date Yesterday and current Date in YYYY-MM-DD string format
def scrape_daily_tweets():
    maxTweets = 10000000                            # ! Maxtweets to scrape ! #
    data = db.get_data_table('Twitter_Data')
    d = data['date'].iloc[-1]
    last_date = datetime.strptime(d, "%Y-%m-%d")
    d = last_date + timedelta(days=1)
    dateSince = datetime.strftime(d, "%Y-%m-%d")    # ! Last Date seen at the last row of the Database ! #
    dateUntil = date.today()                        # ! Current date ! #

    #dateSince = "2021-11-01" # ! ===TEST DATES=== ! #
    #dateUntil = "2021-11-03" # ! ===TEST DATES=== ! #

    if (dateSince==dateUntil):
        print("Please scrape tomorrow!")
    else:
        cryptoData = pd.DataFrame({'searchTerm':['#bitcoin OR #btc','#ethereum OR #eth','#dogecoin OR #doge'],'cryptoName':['bitcoin','ethereum','dogecoin']})
        # Initialize Total the Data dataframe
        total_data = pd.DataFrame({'Date':[dateSince],'bitcoin':[0],'ethereum':[0],'dogecoin':[0]})

        #Get Twitter Data
        for index, col in cryptoData.iterrows():
            #Set Snscrape parameters
            twitterScraperParams = str(str(col["searchTerm"]) + ' + since:' + str(dateSince) + ' until:' + str(dateUntil) +  ' -filter:links -filter:replies')
            #Create an empty dataframe
            columns = ['id','date','username','tweet']
            crypto_df = pd.DataFrame(columns=columns)

            #===Scrape needed Data===
            print ("[!] " + str(col["cryptoName"]) + " Scraping Start !!")
            for i,tweet in enumerate(sntwitter.TwitterSearchScraper(twitterScraperParams).get_items()):
                    if i > maxTweets:
                        break  
                    new_row = {'id':tweet.id, 'date':str(tweet.date), 'username':tweet.user.username, 'tweet':tweet.content}
                    crypto_df = crypto_df.append(new_row,ignore_index=True)

            #Print crypto dataframe
            print ("Raw data dimensions: " + str(crypto_df.shape))
            #print(crypto_df)

            #===Remove Duplicate Data===
            #Split date column
            crypto_df[['date', 'time']] = crypto_df["date"].str.split(" ", 1, expand=True)
            #New dataframe
            newdata_cols = ['date', 'time' , 'username', 'tweet']
            newdata = pd.DataFrame(crypto_df[['date', 'time', 'username', 'tweet']].values, columns = newdata_cols)
            #Reverse Data Order
            newdata = newdata[::-1].reset_index(drop = True)
            #Drop Duplicate Username on the same day
            newdata.drop_duplicates(subset=['date','username'], keep='first', inplace=True)
            newdata.reset_index(drop=True, inplace=True)

            #Print filtered crypto dataframe
            print ("Filtered data dimensions: " + str(newdata.shape))
            #print(newdata)

            #Total the given data
            i=0
            for dates in newdata["date"]:
                if (dates!=(total_data.loc[i,"Date"])):
                    i = i + 1
                    total_data.loc[i,"Date"]=dates
                    total_data.loc[i,str(col["cryptoName"])] = 0
                    total_data.loc[i,str(col["cryptoName"])]= total_data.loc[i,str(col["cryptoName"])] + 1
                else:
                    total_data.loc[i,str(col["cryptoName"])]= total_data.loc[i,str(col["cryptoName"])] + 1

            print("[!] Total Data !!!")
            print(total_data)

        update_trend('Twitter_Data',total_data)
        #Remove dataframes
        a, b, c = crypto_df, newdata, total_data
        lst = [a,b,c]
        del lst

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
#     #     scrape_daily_tweets()
#     #     scrape_google_data(today)

#     t.sleep(60*sleep)