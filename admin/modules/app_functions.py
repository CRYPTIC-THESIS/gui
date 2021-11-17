from main import *

class AppFunctions(MainWindow):

    def loading(self):
        self.Dialog = QDialog()
        self.Dialog.ui = Ui_Dialog()
        self.Dialog.ui.setupUi(self.Dialog)

        self.Dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.Dialog.setAttribute(Qt.WA_TranslucentBackground, Qt.WA_DeleteOnClose)

        # DROP SHADOW
        self.Dialog.shadow = QGraphicsDropShadowEffect(self)
        self.Dialog.shadow.setBlurRadius(17)
        self.Dialog.shadow.setXOffset(0)
        self.Dialog.shadow.setYOffset(0)
        self.Dialog.shadow.setColor(QColor(0, 0, 0, 150))
        self.Dialog.ui.frame.setGraphicsEffect(self.Dialog.shadow)

        self.Dialog.ui.loadingBar.setRange(0,0)
        self.Dialog.ui.title.setText(self.desc)
        
        self.Dialog.show()

    def popup(self, arg):
        # print(arg)
        self.Popup = QDialog()
        self.Popup.ui = Ui_Popup()
        self.Popup.ui.setupUi(self.Popup)

        self.Popup.setWindowFlags(Qt.FramelessWindowHint)
        self.Popup.setAttribute(Qt.WA_TranslucentBackground, Qt.WA_DeleteOnClose)

        # DROP SHADOW
        self.Popup.shadow = QGraphicsDropShadowEffect(self)
        self.Popup.shadow.setBlurRadius(17)
        self.Popup.shadow.setXOffset(0)
        self.Popup.shadow.setYOffset(0)
        self.Popup.shadow.setColor(QColor(0, 0, 0, 150))
        self.Popup.ui.frame.setGraphicsEffect(self.Popup.shadow)

        if arg == 1:
            self.Popup.ui.ok.hide()
            self.Popup.ui.cancel.setStyleSheet(u"border: 2px solid #54B9CA;")
        
        self.Popup.setModal(True)
        self.Popup.show()

    def dash_histo(self):
        self.h_worker = GetHistoData(self.selected_crypto, 
                                self.selected_histo_price, 
                                self.selected_histo_day, 
                                self.selected_date)
        self.h_worker.start()
        self.h_worker.pass_histo_data.connect(self.catch_histo_data)

    def dash_pred(self):
        self.pg_worker = GetPredData(self.selected_crypto,
                                self.selected_predicted_day,
                                self.selected_date)
        self.pg_worker.start()
        self.pg_worker.pass_pred_data.connect(self.catch_pred_data)

    def get_accuracy(self):
        self.a_worker = GetAccuracy(self.analyze_crypto)
        self.a_worker.start()
        self.a_worker.pass_acc_data.connect(self.catch_analysis)


    def get_dataset_selection(self):
        # CRYPTO
        for checkBox in self.ui.cryptoCheckBox.findChildren(QCheckBox):
            if checkBox.isChecked() == True:
                self.dataset_crypto.append(checkBox.text())
        
        # SOURCE
        temp_source = None
        for checkBox in self.ui.sourceCheckBox.findChildren(QRadioButton):
            if checkBox.isChecked() == True:
                temp_source = checkBox.text()
                # print(temp_source)

        if (not self.dataset_crypto) or (temp_source is None):
            print('Incomplete Selection.')
            self.empty_ds()
        
        else:
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
            self.disable('proceed')

            # DATE
            self.dataset_date_from = self.ui.trainFromDateEdit.date().toString()
            self.dataset_date_from = pd.to_datetime(self.dataset_date_from).date()

            self.dataset_date_until = self.ui.trainUntilDateEdit.date().toString()
            self.dataset_date_until = pd.to_datetime(self.dataset_date_until).date()
            
            if temp_source == 'Historical Data':
                self.ui.trainTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.dataset_source = ['CoinDesk Historical Data']
            elif temp_source == 'Historical Data + Internet Trends':
                self.ui.trainTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                self.dataset_source = ['CoinDesk Historical Data', 'Twitter', 'Reddit', 'GoogleTrends']
            # print(self.dataset_source)

            # self.train_dataset_table()
            self.get_dataset()
            # self.ui.btn_startTraining.show()

            self.ui.testTimeFrameList.addItems([str(self.dataset_date_from), str(self.dataset_date_until)])
            self.ui.testCryptoList.addItems(self.dataset_crypto)
            self.ui.testSourceList.addItem(temp_source)

            self.ui.deployTimeFrameList.addItems([str(self.dataset_date_from), str(self.dataset_date_until)])
            self.ui.deployCryptoList.addItems(self.dataset_crypto)
            self.ui.deploySourceList.addItem(temp_source)

            self.ui.testCryptoCombo.addItems(self.dataset_crypto)
            self.ui.deployCryptoCombo.addItems(self.dataset_crypto)

    def cancel_selection(self):
        try:
            self.Popup.close()
        except Exception:
            pass

        # DATE
        self.ui.trainFromDateEdit.setDate(QDate(2020, 1, 1))
        self.ui.trainUntilDateEdit.setDate(QDate(2021, 10, 31))
        self.dataset_date_from = None
        self.dataset_date_until = None

        # CRYPTO
        for checkBox in self.ui.cryptoCheckBox.findChildren(QCheckBox):
            checkBox.setChecked(False)
        self.dataset_crypto = list()
        
        # SOURCE
        self.ui.RadioGroup.setExclusive(False)
        for checkBox in self.ui.sourceCheckBox.findChildren(QRadioButton):
            checkBox.setChecked(False)
        self.ui.RadioGroup.setExclusive(True)
        self.dataset_source = list()

        for checkBox in self.ui.sourceCheckBox.findChildren(QRadioButton):
            if checkBox.isChecked() == True:
                print('the audacity !')

        self.ui.btn_startTraining.hide()

        self.ui.testTimeFrameList.clear()
        self.ui.testCryptoList.clear()
        self.ui.testSourceList.clear()

        self.ui.deployTimeFrameList.clear()
        self.ui.deployCryptoList.clear()
        self.ui.deploySourceList.clear()

        self.ui.testCryptoCombo.clear()
        self.ui.deployCryptoCombo.clear()

        self.ui.trainTable.clear()
        self.ui.trainTable.hide()

        self.enable('proceed')
        self.ui.btn_proceed.setEnabled(True)


class GetHistoData(QThread):
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


class ImplementModel(QObject):
    process_complete = Signal(str)
    deploy_complete = Signal()

    def __init__(self, process):
        super().__init__()
        self.process = process

    def run_terminal(self):
        print(self.process)

        if self.process == 'deploy':
            command_line = 'python model/deploy.py'
            p = os.popen(command_line)
            if p:
                # print('Done')
                print(p.read())
                self.deploy_complete.emit()
        else:
            if self.process == 'train':
                command_line = 'python model/training_model.py'
            
            if self.process == 'test':
                command_line = 'python model/testing_model.py'

            p = os.popen(command_line)
            if p:
                output = p.read()
                print('Done')
                self.process_complete.emit(output)


class GetAccuracy(QThread):
    pass_acc_data = Signal(pd.DataFrame)
    # finished = Signal()

    def __init__(self, crypto):
        super().__init__()
        self.crypto = crypto

    def run(self):
        df = pd.DataFrame()

        error_ = pd.read_csv('csv/All_Error_Analysis.csv', index_col=[0])
        # print(error_)
        if self.crypto.startswith('Bitcoin') == True:
            error_ = error_.loc[['BTC']]
            class_ = pd.read_csv('csv/BTC_classification_analysis.csv', index_col=[0])

        if self.crypto.startswith('Ethereum') == True:
            error_ = error_.loc[['ETH']]
            class_ = pd.read_csv('csv/ETH_classification_analysis.csv', index_col=[0])
        
        if self.crypto.startswith('Dogecoin') == True:
            error_ = error_.loc[['DOGE']]
            class_ = pd.read_csv('csv/DOGE_classification_analysis.csv', index_col=[0])
        
        class_.reset_index(drop=True, inplace=True)
        error_.reset_index(drop=True, inplace=True)

        error_ = error_.round(4)
        class_ = class_.round(4)

        df = pd.concat([df, error_], axis=1)
        df = pd.concat([df, class_], axis=1)

        # print('error_: ', error_)
        # print('class_: ', class_)
        # print('df: ', df)
        
        self.pass_acc_data.emit(df)