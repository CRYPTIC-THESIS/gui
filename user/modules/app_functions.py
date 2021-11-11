from main import *

class AppFunctions(MainWindow):

    # def get_df(self):
    #     self.worker = GetData(self.selected_crypto, self.home_histo_price, self.home_histo_days, self.today)
    #     self.worker.start()
    #     self.worker.pass_histo_data.connect(self.catch_histo_data)

    def dash_histo(self):
        if self.selected_crypto == 'btn_home':
            lst = [self.selected_crypto, self.home_histo_price, self.home_histo_days, self.today]
        if self.selected_crypto == 'btn_btc':
            lst = [self.selected_crypto, self.btc_histo_price, self.btc_histo_days, self.today]
        if self.selected_crypto == 'btn_eth':
            lst = [self.selected_crypto, self.eth_histo_price, self.eth_histo_days, self.today]
        if self.selected_crypto == 'btn_doge':
            lst = [self.selected_crypto, self.doge_histo_price, self.doge_histo_days, self.today]

        self.h_worker = GetHistoData(lst)
        self.h_worker.start()
        self.h_worker.pass_histo_data.connect(self.catch_histo_data)

    def dash_pred(self):
        print('prediction')
        # self.p_worker = GetPredData(self.selected_crypto,
        #                         self.selected_predicted_price,
        #                         self.selected_predicted_day,
        #                         self.today)
        # self.p_worker.pass_pred_data.connect(self.catch_pred_data)


class GetHistoData(QThread):
    pass_histo_data = Signal(list)

    def __init__(self, lst_):  # crypto, h_price, h_days, today
        super().__init__()
        self.crypto = lst_[0]
        self.h_price = lst_[1]
        self.h_days = lst_[2]
        self.today = lst_[3]

        if self.h_days == 1:
            self.df_btc = pd.read_csv('csv/rt_btc.csv')
            self.df_eth = pd.read_csv('csv/rt_eth.csv')
            self.df_doge = pd.read_csv('csv/rt_doge.csv')
        else:
            self.df_btc = pd.read_csv('csv/db_btc.csv')
            self.df_eth = pd.read_csv('csv/db_eth.csv')
            self.df_doge = pd.read_csv('csv/db_doge.csv')

    def run(self):
        if self.crypto == 'btn_home':
            self.lst = [self.df_btc, self.df_eth, self.df_doge]
        if self.crypto == 'btn_btc':
            self.lst = [self.df_btc]
        if self.crypto == 'btn_eth':
            self.lst = [self.df_eth]
        if self.crypto == 'btn_doge':
            self.lst = [self.df_doge]

        if self.h_days == 1:
            new_lst = self.realtime()
        else:
            new_lst = self.histo()
            
        self.pass_histo_data.emit(new_lst)

    def histo(self):
        numeric = ['High', 'Low', 'Open', 'Closing']
        new_lst = list()

        today = pd.to_datetime(self.today)
        past_d = today - timedelta(days=self.h_days)
        
        for df in self.lst:
            df2 = df.drop(df.columns[0], axis=1)
            df = df2
            df.columns = ['Date', 'High', 'Low', 'Open', 'Closing']
            df['Date'] = pd.to_datetime(df['Date'])
            df[numeric] = df[numeric].apply(pd.to_numeric, errors='coerce', axis=1)
            # print(df.head())

            df_date = []
            df_price = []

            df_ = df.loc[(df['Date'] >= past_d) & (df['Date'] <= today)]
            df_date = df_['Date']
            df_price = df_[self.h_price]

            x = []
            y = []

            for item in df_date:
                item = datetime.timestamp(item)
                x.append(item)
            for item in df_price:
                y.append(item)

            new_lst.append([df, [x, y]])
        return new_lst

    def realtime(self):
        numeric = ['High', 'Low', 'Open', 'Closing']
        new_lst = list()

        for df in self.lst:
            df2 = df.drop(df.columns[0], axis=1)
            df = df2
            df.columns = ['Closing', 'High', 'Low', 'Open', 'Timestamp']
            df[numeric] = df[numeric].apply(pd.to_numeric, errors='coerce', axis=1)

            df_time = df['Timestamp']
            df_price = df[self.h_price]

            x = []
            y = []

            for item in df_time:
                item = int(item)
                x.append(item)
            for item in df_price:
                y.append(item)

            new_lst.append([df, [x, y]])
        return new_lst


class GetPredData(QThread):
    pass_pred_data = Signal(list)

    def __init__(self, crypto, p_price, p_days, today):
        super().__init__()
        self.crypto = crypto
        # self.p_price = p_price
        self.p_days = p_days
        self.today = today

    def run(self):
        self.df_btc = pd.read_csv('csv/pred_btc.csv')
        self.df_eth = pd.read_csv('csv/pred_eth.csv')
        self.df_doge = pd.read_csv('csv/pred_doge.csv')

        if self.crypto == 'btn_all':
            lst = [self.df_btc, self.df_eth, self.df_doge]
        if self.crypto == 'btn_btc':
            lst = [self.df_btc]
        if self.crypto == 'btn_eth':
            lst = [self.df_eth]
        if self.crypto == 'btn_doge':
            lst = [self.df_doge]

        # numeric = ['High', 'Low', 'Closing']
        new_lst = list()

        future_d = self.today + timedelta(days=self.p_days)

        for df in lst:
            df2 = df.drop(df.columns[0], axis=1)
            df = df2
            df.columns = ['Date', 'Price']
            df['Date'] = pd.to_datetime(df['Date'])
            df['Price'] = df['Price'].apply(pd.to_numeric, errors='coerce', axis=1)
            # print(df.head())

            df_date = []
            df_price = []

            df_ = df.loc[(df['Date'] >= future_d) & (df['Date'] <= self.today)]
            df_date = df_['Date']
            df_price = df_['Price']

            x = []
            y = []

            for item in df_date:
                item = datetime.timestamp(item)
                x.append(item)
            for item in df_price:
                y.append(item)

            new_lst.append([df, [x, y]])
        self.pass_pred_data.emit(new_lst)