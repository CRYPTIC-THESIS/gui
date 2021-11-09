import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv
import dbconnect

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

    dbconnect.update_trend('Twitter_Data',twitter_daily_total)
    #twitter_daily_total.to_csv('Daily-Twitter-Data/Daily_Twitter_Total.csv', mode='w', index=False, header=True) #if data is needed to be in a csv file
    #return twitter_daily_total #return final data frame if needed