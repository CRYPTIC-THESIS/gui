from main import *

class AppFunctions(MainWindow):

    def get_data(self):
        self.db_worker.terminate()

        self.worker =   GetData(self.selected_crypto, 
                                self.selected_histo_price, 
                                self.selected_histo_day, 
                                self.selected_date)
        self.worker.start()
        self.worker.pass_histo_data.connect(self.catch_histo_data)

    def get_dataset_selection(self):
        self.ui.testTimeFrameList.clear()
        self.ui.testCryptoList.clear()
        self.ui.testSourceList.clear()

        self.ui.deployTimeFrameList.clear()
        self.ui.deployCryptoList.clear()
        self.ui.deploySourceList.clear()

        self.ui.testCryptoCombo.clear()
        self.ui.deployCryptoCombo.clear()

        self.ui.trainTable.clear()

        self.ui.btn_proceed.setEnabled(False)

        # DATE
        self.dataset_date_from = self.ui.trainFromDateEdit.date().toString()
        self.dataset_date_from = pd.to_datetime(self.dataset_date_from).date()

        self.dataset_date_until = self.ui.trainUntilDateEdit.date().toString()
        self.dataset_date_until = pd.to_datetime(self.dataset_date_until).date()

        # CRYPTO
        for checkBox in self.ui.cryptoCheckBox.findChildren(QCheckBox):
            if checkBox.isChecked() == True:
                self.dataset_crypto.append(checkBox.text())
        
        # SOURCE
        for checkBox in self.ui.sourceCheckBox.findChildren(QCheckBox):
            if checkBox.isChecked() == True:
                self.dataset_source.append(checkBox.text())

        # self.train_dataset_table()
        self.get_dataset()
        # self.ui.btn_startTraining.show()

        self.ui.testTimeFrameList.addItems([str(self.dataset_date_from), str(self.dataset_date_until)])
        self.ui.testCryptoList.addItems(self.dataset_crypto)
        self.ui.testSourceList.addItems(self.dataset_source)

        self.ui.deployTimeFrameList.addItems([str(self.dataset_date_from), str(self.dataset_date_until)])
        self.ui.deployCryptoList.addItems(self.dataset_crypto)
        self.ui.deploySourceList.addItems(self.dataset_source)

        self.ui.testCryptoCombo.addItems(self.dataset_crypto)
        self.ui.deployCryptoCombo.addItems(self.dataset_crypto)

    def cancel_selection(self):
        # DATE
        self.ui.trainFromDateEdit.setDate(QDate(2020, 1, 1))
        self.ui.trainUntilDateEdit.setDate(QDate(2021, 5, 31))
        self.dataset_date_from = None
        self.dataset_date_until = None

        # CRYPTO
        for checkBox in self.ui.cryptoCheckBox.findChildren(QCheckBox):
            checkBox.setChecked(False)
        self.dataset_crypto = list()
        
        # # SOURCE
        # for checkBox in self.ui.sourceCheckBox.findChildren(QCheckBox):
        #     checkBox.setChecked(False)
        self.dataset_source = list()

        self.ui.btn_startTraining.hide()

        self.ui.testTimeFrameList.clear()
        self.ui.testCryptoList.clear()
        self.ui.testSourceList.clear()

        self.ui.deployTimeFrameList.clear()
        self.ui.deployCryptoList.clear()
        self.ui.deploySourceList.clear()

        self.ui.trainTable.clear()
        self.ui.trainTable.hide()

        self.ui.btn_proceed.setEnabled(True)


class GetData(QThread):
    pass_histo_data = Signal(list)

    def __init__(self, crypto, h_price, h_days, today):
        super().__init__()
        self.crypto = crypto
        self.h_price = h_price
        self.h_days = h_days
        self.today = today

    def run(self):
        self.df_btc = pd.read_csv('csv/db_btc.csv')
        self.df_eth = pd.read_csv('csv/db_eth.csv')
        self.df_doge = pd.read_csv('csv/db_doge.csv')

        if self.crypto == 'btn_all':
            lst = [self.df_btc, self.df_eth, self.df_doge]
        if self.crypto == 'btn_btc':
            lst = [self.df_btc]
        if self.crypto == 'btn_eth':
            lst = [self.df_eth]
        if self.crypto == 'btn_doge':
            lst = [self.df_doge]

        numeric = ['High', 'Low', 'Open', 'Closing']
        new_lst = list()

        # today = pd.to_datetime(today)
        past_d = self.today - timedelta(days=self.h_days)
        
        for df in lst:
            df2 = df.drop(df.columns[0], axis=1)
            df = df2
            df.columns = ['Date', 'High', 'Low', 'Open', 'Closing']
            df['Date'] = pd.to_datetime(df['Date'])
            df[numeric] = df[numeric].apply(pd.to_numeric, errors='coerce', axis=1)
            # print(df.head())

            df_date = []
            df_price = []

            df_ = df.loc[(df['Date'] >= past_d) & (df['Date'] <= self.today)]
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
        self.pass_histo_data.emit(new_lst)

