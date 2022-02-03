from operator import imod
from main import *
from .EMA import ema_smoothing
from .histo_data import *

class AccessDatabase(QObject):
    import_data_complete = Signal()
    
    def __init__(self, today):
        super().__init__()
        self.today = pd.to_datetime(today).strftime('%Y-%m-%d')
    
    def access_now(self):

        past = (pd.to_datetime(self.today) - timedelta(days=365)).strftime('%Y-%m-%d')

        db_btc = get_histo(past, self.today, 'BTC')
        db_eth = get_histo(past, self.today, 'ETH')
        db_doge = get_histo(past, self.today, 'DOGE')

        rt_btc = get_current('BTC')
        rt_eth = get_current('ETH')
        rt_doge = get_current('DOGE')

        try:
            p_btc = get_pred_table('BTC_predict')
            p_eth = get_pred_table('ETH_predict')
            p_doge = get_pred_table('DOGE_predict')

            lst = [db_btc, db_eth, db_doge, rt_btc, rt_eth, rt_doge, p_btc, p_eth, p_doge]
        except Exception:
            lst = [db_btc, db_eth, db_doge, rt_btc, rt_eth, rt_doge]
        
        fn = ['csv/db_btc.csv', 'csv/db_eth.csv', 'csv/db_doge.csv',
              'csv/rt_btc.csv', 'csv/rt_eth.csv', 'csv/rt_doge.csv',
              'csv/p_btc.csv', 'csv/p_eth.csv', 'csv/p_doge.csv']

        for i, df in enumerate(lst):
            if i > 5:
                df['Date'] = df.index
                df['Date'] = pd.to_datetime(df['Date']).dt.date
                df.reset_index(drop=True, inplace=True)
                df.columns = ['Price', 'Date']
                df['Price'] = df['Price'].round(4)
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
            'Twitter': 'Twitter_Data', 'Reddit': 'Reddit_Data', 'GoogleTrends': 'Google_Data'
        }
        
        for item in self.ds_source:
            # print(table_name[item])
            if item == 'Twitter':
                twitter = pd.DataFrame(get_data_table(table_name[item]))
                twitter = twitter[['date', table_name[crypto]]]
                twitter = ema_smoothing(twitter)    # EMA Smoothing                                    
                twitter['date'] = pd.to_datetime(twitter['date']).dt.date
                twitter = twitter.loc[(twitter['date'] >= self.from_) & (twitter['date'] <= self.until_)]
                twitter.columns=['Date', item]
                # df = pd.concat([df, twitter], ignore_index=True)
                df = pd.merge(df, twitter, how='outer', on='Date')
            
            elif item == 'Reddit':
                reddit = pd.DataFrame(get_data_table(table_name[item]))
                reddit = reddit[['date', table_name[crypto]]]
                reddit = ema_smoothing(reddit)    # EMA Smoothing 
                reddit['date'] = pd.to_datetime(reddit['date']).dt.date
                reddit = reddit.loc[(reddit['date'] >= self.from_) & (reddit['date'] <= self.until_)]
                reddit.columns=['Date', item]
                # df = pd.concat([df, reddit], ignore_index=True)
                df = pd.merge(df, reddit, how='outer', on='Date')
            
            elif item == 'GoogleTrends':
                google = pd.DataFrame(get_data_table(table_name[item]))
                google = google[['date', table_name[crypto]]]
                google = ema_smoothing(google)    # EMA Smoothing 
                google['date'] = pd.to_datetime(google['date']).dt.date
                google = google.loc[(google['date'] >= self.from_) & (google['date'] <= self.until_)]
                google.columns=['Date', item]
                # df = pd.concat([df, google], ignore_index=True)
                df = pd.merge(df, google, how='outer', on='Date')
            
            elif item == 'CoinDesk Historical Data':
                if table_name[crypto] == 'btc':
                    crypto_data = get_histo(self.from_.strftime('%Y-%m-%d'), self.until_.strftime('%Y-%m-%d'), 'BTC')
                if table_name[crypto] == 'eth':
                    crypto_data = get_histo(self.from_.strftime('%Y-%m-%d'), self.until_.strftime('%Y-%m-%d'), 'ETH')
                if table_name[crypto] == 'doge':
                    crypto_data = get_histo(self.from_.strftime('%Y-%m-%d'), self.until_.strftime('%Y-%m-%d'), 'DOGE')

                crypto_data['Date'] = pd.to_datetime(crypto_data['Date']).dt.date
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