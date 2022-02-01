from main import *
from . analytics import *
from . histo_data import *

class AppFunctions(MainWindow):

    def display_prices(self):
        self.prices = GetPrices()
        self.prices.start()
        self.prices.import_complete.connect(self.display_this)

    def dash_histo(self):
        if self.selected_crypto == 'btn_home':
            lst = [self.selected_crypto, self.home_histo_price, self.home_histo_days, self.today]
        if self.selected_crypto == 'btn_btc':
            lst = [self.selected_crypto, self.btc_histo_price, self.btc_histo_days, self.today]
        if self.selected_crypto == 'btn_eth':
            lst = [self.selected_crypto, self.eth_histo_price, self.eth_histo_days, self.today]
        if self.selected_crypto == 'btn_doge':
            lst = [self.selected_crypto, self.doge_histo_price, self.doge_histo_days, self.today]

        self.h_thread = QThread()
        self.h_worker = GetHistoData(lst)
        self.h_worker.moveToThread(self.h_thread)
        self.h_worker.pass_histo_data.connect(self.catch_histo_data)
        self.h_thread.started.connect(self.h_worker.start_run)
        self.h_thread.start()

    def dash_pred(self):
        # print('prediction')
        self.pg_worker = GetPredData(self.selected_crypto,
                                self.selected_predicted_day,
                                self.today)
        self.pg_worker.start()
        self.pg_worker.pass_pred_data.connect(self.catch_pred_data)


class GetDecisionSupport(QThread):
    decision_complete = Signal()

    def run(self):
        dec_support = [ 'BTC: '+ get_decision('BTC'), 
                        'ETH: '+ get_decision('ETH'), 
                        'DOGE: '+ get_decision('DOGE')]

        pd.DataFrame([dec_support]).to_csv('csv/decsupport.csv')
        self.decision_complete.emit()

class GetPrices(QThread):
    import_complete = Signal(dict)

    def run(self):
        dfs = [pd.read_csv('csv/rt_btc.csv'), 
               pd.read_csv('csv/rt_eth.csv'), 
               pd.read_csv('csv/rt_doge.csv')]
        dct = {}
        n = ['btc', 'eth', 'doge']

        for i, df in enumerate(dfs):
            dct[n[i]] = [df['Close'].iat[-1].round(4),
                          df['Open'].iat[-1].round(4),
                          df['High'].iat[-1].round(4),
                          df['Low'].iat[-1].round(4)
                         ]
        
        # print(dct)
        self.import_complete.emit(dct)


class GetHistoData(QObject):
    pass_histo_data = Signal(list)

    def __init__(self, lst_):  # crypto, h_price, h_days, today
        super().__init__()
        self.crypto = lst_[0]
        self.h_price = lst_[1]
        self.h_days = lst_[2]
        self.today = lst_[3]

    def start_run(self):

        if self.h_days == '24h':
            self.df_btc = pd.read_csv('csv/rt_btc.csv')
            self.df_eth = pd.read_csv('csv/rt_eth.csv')
            self.df_doge = pd.read_csv('csv/rt_doge.csv')
        else:
            self.df_btc = pd.read_csv('csv/db_btc.csv')
            self.df_eth = pd.read_csv('csv/db_eth.csv')
            self.df_doge = pd.read_csv('csv/db_doge.csv')
        
        if self.crypto == 'btn_home':
            self.lst = [self.df_btc, self.df_eth, self.df_doge]
        if self.crypto == 'btn_btc':
            self.lst = [self.df_btc]
        if self.crypto == 'btn_eth':
            self.lst = [self.df_eth]
        if self.crypto == 'btn_doge':
            self.lst = [self.df_doge]
            
        self.pass_histo_data.emit(self.histo())

    def histo(self):

        numeric = ['Close', 'Open', 'High', 'Low']
        new_lst = list()
        
        for i, df in enumerate(self.lst):
            
            if self.h_days == '24h':
                date = pd.to_datetime(df['Datetime'])
            
            elif self.h_days == '1y':
                date = pd.to_datetime(df['Date'])
            
            else:
                df = df.tail(self.h_days).reset_index(drop=True)
                df['Date'] = pd.to_datetime(df['Date'])
                date = df['Date']

            df[numeric] = df[numeric].apply(pd.to_numeric, errors='coerce', axis=1)

            x = []
            y = df[self.h_price]

            for item in date:
                item = datetime.timestamp(item)
                x.append(item)

            new_lst.append([df, [x, y]])
        return new_lst


class GetPredData(QThread):
    pass_pred_data = Signal(list)

    def __init__(self, crypto, p_days, today):
        super().__init__()
        self.crypto = crypto
        # self.p_price = p_price
        self.p_days = p_days
        self.today = today

    def run(self):
        self.df_btc = pd.read_csv('csv/p_btc.csv')
        self.df_eth = pd.read_csv('csv/p_eth.csv')
        self.df_doge = pd.read_csv('csv/p_doge.csv')

        if self.crypto == 'btn_home':
            lst = [self.df_btc, self.df_eth, self.df_doge]
        if self.crypto == 'btn_btc':
            lst = [self.df_btc]
        if self.crypto == 'btn_eth':
            lst = [self.df_eth]
        if self.crypto == 'btn_doge':
            lst = [self.df_doge]

        # numeric = ['High', 'Low', 'Closing']
        new_lst = list()

        # future_d = self.today + timedelta(days=self.p_days)

        for df in lst:
            df2 = df.drop(df.columns[0], axis=1)
            df = df2
            df['Date'] = pd.to_datetime(df['Date'])
            df['Price'] = pd.to_numeric(df['Price'])
            df['Price'] = df['Price'].round(4)
            # print(df.head())

            df_date = []
            df_price = []

            # df_ = df.loc[(df['Date'] >= future_d) & (df['Date'] <= self.today)]
            df_date = df['Date']
            df_price = df['Price']
            df['Date'] = pd.to_datetime(df['Date']).dt.date

            x = []
            y = []

            for i in range(self.p_days):
                x.append(datetime.timestamp(df_date[i]))
                y.append(df_price[i])

            new_lst.append([df, [x, y]])
        self.pass_pred_data.emit(new_lst)