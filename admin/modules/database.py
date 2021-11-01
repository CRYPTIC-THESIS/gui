import sys 
sys.path.append('..')

import dbconnect as db
import pandas as pd

def import_data(date):

    # date = date.date()
    print(date)

    df_btc = pd.DataFrame(db.get_data_table('Bitcoin_Data'))
    df_eth = pd.DataFrame(db.get_data_table('Ethereum_Data'))
    df_doge = pd.DataFrame(db.get_data_table('Dogecoin_Data'))

    df_btc.columns = ['Date', 'High', 'Low', 'Open', 'Closing']
    df_eth.columns = ['Date', 'High', 'Low', 'Open', 'Closing']
    df_doge.columns = ['Date', 'High', 'Low', 'Open', 'Closing']

    df_btc['Date'] = pd.to_datetime(df_btc['Date'])
    df_eth['Date'] = pd.to_datetime(df_eth['Date'])
    df_doge['Date'] = pd.to_datetime(df_doge['Date'])

    numeric = ['High', 'Low', 'Open', 'Closing']
    df_btc[numeric] = df_btc[numeric].apply(pd.to_numeric, errors='coerce', axis=1)
    df_eth[numeric] = df_eth[numeric].apply(pd.to_numeric, errors='coerce', axis=1)
    df_doge[numeric] = df_doge[numeric].apply(pd.to_numeric, errors='coerce', axis=1)


    df_btc = df_btc.loc[df_btc['Date'] <= date]
    print(df_btc)
    df_eth = df_eth.loc[df_eth['Date'] <= date]
    print(df_eth)
    df_doge = df_doge.loc[df_doge['Date'] <= date]
    print(df_doge)

    # print(df_btc, df_eth, df_doge)
    
    return df_btc, df_eth, df_doge

def get_dataset_df(from_, until_, dataset_crypto, dataset_source):
    
    my_df = pd.DataFrame()
    for crypto in dataset_crypto:
        print(crypto)
        my_df = pd.concat([my_df, select_data(from_, until_, crypto, dataset_source)], ignore_index=True)
    print(my_df.head())
    print(my_df.tail())

    return my_df

def select_data(from_, until_, dataset_crypto, dataset_source):
    print('Hello Select Data')

    df = pd.DataFrame(columns=['Date'])

    table_name = {
        'Bitcoin (BTC)': 'btc', 'Ethereum (ETH)': 'eth', 'Dogecoin (DOGE)': 'doge',
        'Twitter Volume': 'Twitter_Data', 'Reddit Volume': 'Reddit_Data', 'GoogleTrends': 'Google_Data'
    }
    
    for item in dataset_source:
        print(item)
        # print(table_name[item])
        if item == 'Twitter Volume':
            twitter = pd.DataFrame(db.get_data_table(table_name[item]))
            twitter = twitter[['date', table_name[dataset_crypto]]]
            twitter['date'] = pd.to_datetime(twitter['date']).dt.date
            twitter = twitter.loc[(twitter['date'] >= from_) & (twitter['date'] <= until_)]
            twitter.columns=['Date', item]
            # df = pd.concat([df, twitter], ignore_index=True)
            df = pd.merge(df, twitter, how='outer', on='Date')
        
        elif item == 'Reddit Volume':
            reddit = pd.DataFrame(db.get_data_table(table_name[item]))
            reddit = reddit[['date', table_name[dataset_crypto]]]
            reddit['date'] = pd.to_datetime(reddit['date']).dt.date
            reddit = reddit.loc[(reddit['date'] >= from_) & (reddit['date'] <= until_)]
            reddit.columns=['Date', item]
            # df = pd.concat([df, reddit], ignore_index=True)
            df = pd.merge(df, reddit, how='outer', on='Date')
        
        elif item == 'GoogleTrends':
            google = pd.DataFrame(db.get_data_table(table_name[item]))
            google = google[['date', table_name[dataset_crypto]]]
            google['date'] = pd.to_datetime(google['date']).dt.date
            google = google.loc[(google['date'] >= from_) & (google['date'] <= until_)]
            google.columns=['Date', item]
            # df = pd.concat([df, google], ignore_index=True)
            df = pd.merge(df, google, how='outer', on='Date')
        
        elif item == 'CoinDesk Historical Data':
            if table_name[dataset_crypto] == 'btc':
                historical = 'Bitcoin_Data'
            elif table_name[dataset_crypto] == 'eth':
                historical = 'Ethereum_Data'
            else:
                historical = 'Dogecoin_Data'
            crypto_data = pd.DataFrame(db.get_data_table(historical))
            crypto_data['date'] = pd.to_datetime(crypto_data['date']).dt.date
            crypto_data = crypto_data.loc[(crypto_data['date'] >= from_) & (crypto_data['date'] <= until_)]
            crypto_data.columns=['Date', 'High', 'Low', 'Open', 'Closing']
            # df = pd.concat([crypto_data, df], ignore_index=True)
            df = pd.merge(crypto_data, df, how='outer', on='Date')

    crypto_ = []
    for rows in range(len(df)):
        if table_name[dataset_crypto] == 'btc':
            crypto_.append('BTC')
        elif table_name[dataset_crypto] == 'eth':
            crypto_.append('ETH')
        else:
            crypto_.append('DOGE')

    df.insert(0, "Cryptocurrency", crypto_, True)

    # print('dataframe', df)
    return df


