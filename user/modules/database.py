from main import *

class AccessDatabase(QThread):
    update_progress = Signal(int)
    import_data_complete = Signal()
    
    def run(self):
        
        db_btc = get_data_table('Bitcoin_Data')
        db_eth = get_data_table('Ethereum_Data')
        db_doge = get_data_table('Dogecoin_Data')

        lst = [db_btc, db_eth, db_doge]
        fn = ['csv/db_btc.csv', 'csv/db_eth.csv', 'csv/db_doge.csv']

        today = datetime.today().strftime('%Y-%m-%d')
        today = pd.to_datetime(today)
        past = today - timedelta(days=365)

        for i, df in enumerate(lst):
            df['date'] = pd.to_datetime(df['date'])
            df = df.loc[(df['date'] >= past) & (df['date'] <= today)]
            df.to_csv(fn[i])

        # print(today)
        # print(past)

        self.import_data_complete.emit()

        for x in range(13, 101):
            time.sleep(0.07)
            self.update_progress.emit(x)