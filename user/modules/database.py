from main import *
from . histo_data import *

class AccessDatabase(QThread):
    update_progress = Signal(int)
    import_data_complete = Signal()
    
    def run(self):

        db_btc = get_histo_dash('1y', 'BTC')
        db_eth = get_histo_dash('1y', 'ETH')
        db_doge = get_histo_dash('1y', 'DOGE')

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

        self.import_data_complete.emit()

        for x in range(13, 101):
            time.sleep(0.07)
            self.update_progress.emit(x)