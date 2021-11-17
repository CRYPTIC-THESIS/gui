from main import *

class AccessDatabase(QThread):
    update_progress = Signal(int)
    import_data_complete = Signal()
    
    def run(self):

        db_btc = get_data_table('Bitcoin_Data')
        db_eth = get_data_table('Ethereum_Data')
        db_doge = get_data_table('Dogecoin_Data')

        rt_btc = get_data_table('Realtime_BTC')
        rt_eth = get_data_table('Realtime_ETH')
        rt_doge = get_data_table('Realtime_DOGE')

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
        cn = ['csv/curr_btc.csv', 'csv/curr_eth.csv', 'csv/curr_doge.csv',]

        today = datetime.today().strftime('%Y-%m-%d')
        today = pd.to_datetime(today)
        past = today - timedelta(days=365)

        for i, df in enumerate(lst):
            if i <= 2:
                df['date'] = pd.to_datetime(df['date'])
                df = df.loc[(df['date'] >= past) & (df['date'] <= today)] 
            elif i >= 3 and i <= 5:
                # df2 = df.rename({'open': 'closing_', 'closing': 'open_'}, axis=1, inplace=True)
                # df = df2.rename({'closing_': 'closing', 'open_': 'open'}, axis=1, inplace=True)
                csv = df.iloc[[-1]]
                csv.to_csv(cn[i-3])
            else:
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

        for x in range(13, 101):
            time.sleep(0.07)
            self.update_progress.emit(x)