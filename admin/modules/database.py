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

# def get_dataset_df(dataframe):

#     my_df = pd.DataFrame()
#     for df in dataframe:



