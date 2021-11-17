from main import *

class AccessDatabase(QObject):
    import_data_complete = Signal()
    
    def __init__(self, today):
        super().__init__()
        self.today = today
    
    def access_now(self):

        rt_btc = get_data_table('Realtime_BTC')
        rt_eth = get_data_table('Realtime_ETH')
        rt_doge = get_data_table('Realtime_DOGE')
        lst = [rt_btc, rt_eth, rt_doge]
        fn = ['csv/curr_btc.csv', 'csv/curr_eth.csv', 'csv/curr_doge.csv',]

        for i, df in enumerate(lst):
            # df2 = df.rename({'open': 'closing_', 'closing': 'open_'}, axis=1, inplace=True)
            # df = df2.rename({'closing_': 'closing', 'open_': 'open'}, axis=1, inplace=True)
            df = df.iloc[[-1]]
            df.to_csv(fn[i])
        
        db_btc = get_data_table('Bitcoin_Data')
        db_eth = get_data_table('Ethereum_Data')
        db_doge = get_data_table('Dogecoin_Data')

        try:
            p_btc = get_pred_table('BTC_predict')
            p_eth = get_pred_table('ETH_predict')
            p_doge = get_pred_table('DOGE_predict')

            lst = [db_btc, db_eth, db_doge, p_btc, p_eth, p_doge] # 
        except Exception:
            lst = [db_btc, db_eth, db_doge]
        
        fn = ['csv/db_btc.csv', 'csv/db_eth.csv', 'csv/db_doge.csv',
              'csv/p_btc.csv', 'csv/p_eth.csv', 'csv/p_doge.csv',]
        past = self.today - timedelta(days=365)

        for i, df in enumerate(lst):
            if i <= 2:
                df['date'] = pd.to_datetime(df['date'])
                df = df.loc[(df['date'] >= past) & (df['date'] <= self.today)]
            else:
                df['Date'] = df.index
                df['Date'] = pd.to_datetime(df['Date']).dt.date
                df.reset_index(drop=True, inplace=True)
                df.columns = ['Price', 'Date']
                df = df.reindex(columns=['Date', 'Price'])
            df.to_csv(fn[i])
        # print(today)
        # print(past)

        self.import_data_complete.emit()

class ImportDataset(QThread):
    pass_dataset = Signal(pd.DataFrame)

    def __init__(self, from_, until_, ds_crypto, ds_source):
        super().__init__()
        self.from_ = from_
        self.until_ = until_
        self.ds_crypto = ds_crypto
        self.ds_source = ds_source

    def run(self):
        self.my_df = pd.DataFrame()
        for crypto in self.ds_crypto:
            print(crypto)
            self.my_df = pd.concat([self.my_df, self.select_data(crypto)], ignore_index=True)

        self.csv()
        # self.my_df.to_csv('csv/dataset.csv')
        
        self.pass_dataset.emit(self.my_df)

    def csv(self):
        csvf = self.my_df
        csvf.to_csv('csv/dataset.csv')

    def select_data(self, crypto):

        df = pd.DataFrame(columns=['Date'])

        table_name = {
            'Bitcoin (BTC)': 'btc', 'Ethereum (ETH)': 'eth', 'Dogecoin (DOGE)': 'doge',
            'Twitter': 'Twitter_Data_12Day_EMA', 'Reddit': 'Reddit_Data_12Day_EMA', 'GoogleTrends': 'Google_Data_12Day_EMA'
        }
        
        for item in self.ds_source:
            # print(table_name[item])
            if item == 'Twitter':
                twitter = pd.DataFrame(get_data_table(table_name[item]))
                twitter = twitter[['date', table_name[crypto]]]
                twitter['date'] = pd.to_datetime(twitter['date']).dt.date
                twitter = twitter.loc[(twitter['date'] >= self.from_) & (twitter['date'] <= self.until_)]
                twitter.columns=['Date', item]
                # df = pd.concat([df, twitter], ignore_index=True)
                df = pd.merge(df, twitter, how='outer', on='Date')
            
            elif item == 'Reddit':
                reddit = pd.DataFrame(get_data_table(table_name[item]))
                reddit = reddit[['date', table_name[crypto]]]
                reddit['date'] = pd.to_datetime(reddit['date']).dt.date
                reddit = reddit.loc[(reddit['date'] >= self.from_) & (reddit['date'] <= self.until_)]
                reddit.columns=['Date', item]
                # df = pd.concat([df, reddit], ignore_index=True)
                df = pd.merge(df, reddit, how='outer', on='Date')
            
            elif item == 'GoogleTrends':
                google = pd.DataFrame(get_data_table(table_name[item]))
                google = google[['date', table_name[crypto]]]
                google['date'] = pd.to_datetime(google['date']).dt.date
                google = google.loc[(google['date'] >= self.from_) & (google['date'] <= self.until_)]
                google.columns=['Date', item]
                # df = pd.concat([df, google], ignore_index=True)
                df = pd.merge(df, google, how='outer', on='Date')
            
            elif item == 'CoinDesk Historical Data':
                if table_name[crypto] == 'btc':
                    historical = 'Bitcoin_Data'
                if table_name[crypto] == 'eth':
                    historical = 'Ethereum_Data'
                if table_name[crypto] == 'doge':
                    historical = 'Dogecoin_Data'
                crypto_data = pd.DataFrame(get_data_table(historical))
                crypto_data['date'] = pd.to_datetime(crypto_data['date']).dt.date
                crypto_data = crypto_data.loc[(crypto_data['date'] >= self.from_) & (crypto_data['date'] <= self.until_)]
                crypto_data.columns=['Date', 'High', 'Low', 'Open', 'Closing']
                # df = pd.concat([crypto_data, df], ignore_index=True)
                df = pd.merge(crypto_data, df, how='outer', on='Date')

        crypto_ = []
        for rows in range(len(df)):
            if table_name[crypto] == 'btc':
                crypto_.append('BTC')
            elif table_name[crypto] == 'eth':
                crypto_.append('ETH')
            else:
                crypto_.append('DOGE')

        df.insert(0, "Cryptocurrency", crypto_, True)

        return df