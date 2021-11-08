from main import *

class AppFunctions(MainWindow):

    def appDefinitions(self):
        self.selected_crypto = None
        self.home_pred_price = None
        self.home_histo_price = None
        self.home_pred_days = None
        self.home_histo_days = None

    def get_df(self):
        self.worker = GenerateDf()
        self.worker.start()
        self.worker.new_df.connect(self.catch_new_df)

    def histo_graph_data(self, lst):
        self.ui.home_histoGraph.clear()
        self.btc = list()
        self.eth = list()
        self.doge = list()
        
        for i, item in enumerate(lst):
            if i >= 0 and i <= 2: self.btc.append(item)
            if i >= 3 and i <= 5: self.eth.append(item)
            if i >= 6 and i <= 8: self.doge.append(item)
        print('# of items: ', i)

        for i, item in enumerate(self.btc):
            print(i)

        # self.printdata()

        # if self.home_histo_price == 'Closing' and self.selected_crypto == 'btn_home':
        #     grph_lst = lst[:1]
        #     print('grph_lst: ', grph_lst)
        #     x = grph_lst[0]
        #     y = grph_lst[1]
        # self.ui.home_histoGraph.plot(x, y, pen=mkPen('#8C88BF', width=2.5))


class GenerateDf(QThread):
    new_df = Signal(list)
    pass_plot = Signal(list)
    # pass_plot_btc = Signal(list)
    # pass_plot_eth = Signal(list)
    # pass_plot_doge = Signal(list)

    def run(self):
        sys.path.append('..')
        df_btc = pd.read_csv('csv/db_btc.csv')
        df_eth = pd.read_csv('csv/db_eth.csv')
        df_doge = pd.read_csv('csv/db_doge.csv')

        lst = [df_btc, df_eth, df_doge]
        numeric = ['High', 'Low', 'Open', 'Closing']
        new_lst = list()

        for df in lst:
            df2 = df.drop(df.columns[0], axis=1)
            df = df2
            df.columns = ['Date', 'High', 'Low', 'Open', 'Closing']
            df['Date'] = pd.to_datetime(df['Date'])
            df[numeric] = df[numeric].apply(pd.to_numeric, errors='coerce', axis=1)
            # print(df.head())
            new_lst.append(df)

        self.new_df.emit(new_lst)

    def plot_this(self, df, past, future, today):
        
        today = pd.to_datetime(today)
        
        if future is None:
            past_d = today - timedelta(days=past)
            print(past)
        
        if past is None:
            future_d = today + timedelta(days=future)
            print(future)
        
        df = pd.DataFrame(df, columns=['Date', 'High', 'Low', 'Open', 'Closing'])
        # print('df: ', df, df.dtypes)

        prices = ['Closing', 'High', 'Low']
        lst = list()
        
        for price in prices:
            df_date = []
            df_price = []

            if future is None:
                df_ = df.loc[(df['Date'] >= past_d) & (df['Date'] <= today)]
            
            if past is None:
                df_ = df.loc[(df['Date'] >= today) & (df['Date'] <= future_d)]

            df_date = df_['Date']
            df_price = df_[price]

            x = []
            y = []

            for item in df_date:
                item = datetime.timestamp(item)
                x.append(item)
            for item in df_price:
                y.append(item)

            # print('df_ :', df_)
            lst.append([x, y])
        # print('Inside thread', lst)

        self.pass_plot.emit(lst)
