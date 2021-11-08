from main import *

class AppFunctions(MainWindow):

    def appDefinitions(self):
        self.selected_crypto = None
        self.home_pred_price = None
        self.home_histo_price = None
        self.home_pred_days = None
        self.home_histo_days = None

    def get_df(self):
        self.worker = GetData()
        self.worker.start()
        run = partial(self.worker.histo, self.selected_crypto, self.home_histo_price, self.home_histo_days, self.today)
        QTimer.singleShot(0, run)
        self.worker.pass_histo_data.connect(self.catch_histo_data)


class GetData(QThread):
    pass_histo_data = Signal(list)
    df_btc = pd.read_csv('csv/db_btc.csv')
    df_eth = pd.read_csv('csv/db_eth.csv')
    df_doge = pd.read_csv('csv/db_doge.csv')

    def histo(self, crypto, h_price, h_days, today):

        if crypto == 'btn_home':
            lst = [self.df_btc, self.df_eth, self.df_doge]
        if crypto == 'btn_btc':
            lst = [self.df_btc]
        if crypto == 'btn_eth':
            lst = [self.df_eth]
        if crypto == 'btn_doge':
            lst = [self.df_eth]

        numeric = ['High', 'Low', 'Open', 'Closing']
        new_lst = list()

        today = pd.to_datetime(today)
        past_d = today - timedelta(days=h_days)
        
        for df in lst:
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
            df_price = df_[h_price]

            x = []
            y = []

            for item in df_date:
                item = datetime.timestamp(item)
                x.append(item)
            for item in df_price:
                y.append(item)

            new_lst.append([df, [x, y]])
        self.pass_histo_data.emit(new_lst)




