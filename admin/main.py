import sys
import os
import pyrebase

from modules import *
os.environ["QT_FONT_DPI"] = "96"


# Login Window
firebaseConfig = {
    "apiKey": "AIzaSyC0k1EEv-FNciFulCDa5C5hsOhX7nsfXQc",
    "authDomain": "cryptic-database.firebaseapp.com",
    "databaseURL": "https://cryptic-database-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "cryptic-database",
    "storageBucket": "cryptic-database.appspot.com",
    "messagingSenderId": "975253440847",
    "appId": "1:975253440847:web:58ec1b6fe880fea93e5d3a",
    "measurementId": "G-H0JJDEYFW9"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Login_MainWindow()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)

        # CUSTOM TITLE BAR
        LoginSettings.ENABLE_CUSTOM_TITLE_BAR = True

        # UI FUNCTIONS DEFINITIONS
        UIFunctions.ui_logindefinitions(self)
        
        self.ui.content.setCurrentWidget(self.ui.loginPage)
        self.ui.pass_login.setEchoMode(QLineEdit.Password)
        self.ui.pass_signup.setEchoMode(QLineEdit.Password)
        self.ui.confirmPass.setEchoMode(QLineEdit.Password)
        
        self.ui.btn_login.clicked.connect(self.loginfunction)
        self.ui.btn_toSignup.clicked.connect(lambda : self.ui.content.setCurrentWidget(self.ui.signupPage))
        
        self.ui.btn_signup.clicked.connect(self.signupfunction)
        self.ui.btn_toLogin.clicked.connect(lambda : self.ui.content.setCurrentWidget(self.ui.loginPage))

        # self.windows = list()

    def loginfunction(self):
        self.ui.username_signup.clear()
        self.ui.pass_signup.clear()
        self.ui.confirmPass.clear()

        email = self.ui.username_login.text()
        password = self.ui.pass_login.text()

        try:
            auth.sign_in_with_email_and_password(email, password)
            self.window = MainWindow()
            # self.windows.append(window)
            self.window.show()
            self.close()
        except Exception:
            print('INVALID ACCOUNT.')
            self.ui.username_login.clear()
            self.ui.pass_login.clear()

    
    def signupfunction(self):
        self.ui.username_login.clear()
        self.ui.pass_login.clear()

        email = self.ui.username_signup.text()
        if self.ui.pass_signup.text() == self.ui.confirmPass.text():
            password = self.ui.pass_signup.text()

            try:
                auth.create_user_with_email_and_password(email, password)
                self.ui.content.setCurrentWidget(self.ui.loginPage)
            except Exception:
                print('INVALID ACCOUNT.')
                self.ui.username_signup.clear()
                self.ui.pass_signup.clear()
                self.ui.confirmPass.clear()

    
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos
        # self.dragPos = event.globalPos()


# Main Window Dashboard
from model import *

widgets = None
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        global widgets
        widgets = self.ui
        widgets.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)

        # CUSTOM TITLE BAR
        MainSettings.ENABLE_CUSTOM_TITLE_BAR = True

        # UI FUNCTIONS DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # DATA
        self.selected_date = None
        self.selected_crypto = None
        self.selected_histo_price = None
        self.selected_histo_day = None
        self.selected_predicted_price = None
        self.selected_predicted_day = None
        self.dataset_date_from = None
        self.dataset_date_until = None
        self.dataset_crypto = list()
        self.dataset_source = list()

        # self.windows = list()

        # QTableWidget Stretch
        widgets.predictedTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widgets.trainTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        widgets.dataAnalysisTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widgets.deployTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        # DISPLAY DEFAULT
        self.setDefaultDisplay()

        # SIGNALS
        self.dashSignals()
        self.trainSignals()
        self.testSignals()
        self.deploySignals()


    def setDefaultDisplay(self):
        # DEFAULTS
        # DASH PAGE
        widgets.stackedWidget.setCurrentWidget(widgets.dash)
        widgets.btn_dash.setStyleSheet(UIFunctions.selectMenu(widgets.btn_dash.styleSheet()))

        # DATE
        widgets.selected_dateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        date = widgets.dateEdit.date()
        widgets.selected_dateLabel.setText(date.toString('MMMM d, yyyy'))
        self.selected_date = date.toString()
        self.selected_date = pd.to_datetime(self.selected_date)
        self.dash_data()

        # CRYPTO
        widgets.btn_btc.setStyleSheet(UIFunctions.selectCrypto(widgets.btn_btc.styleSheet()))
        widgets.btc_card.setStyleSheet(UIFunctions.selectCard(widgets.btc_card.styleSheet()))
        self.selected_crypto = 'Bitcoin_Data'

        # PREDICTED PRICE
        widgets.btn_pred_closing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_pred_closing.styleSheet()))
        self.selected_predicted_price = 'Closing'

        # PREDICTED DAYS
        # self.selected_predicted_day = int(widgets.daysValue.text())
        self.get_pred_day()

        # HISTORY PRICE
        widgets.btn_histo_closing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_histo_closing.styleSheet()))
        self.selected_histo_price = 'Closing'

        # HISTORY DAYS
        widgets.btn_1.setStyleSheet(UIFunctions.selectHistoDay(widgets.btn_1.styleSheet()))
        self.selected_histo_day = 3

        # CARDS
        widgets.btcCurrPriceLabel.setText('$'+str(self.dash_btc['Closing'].iat[-1]))
        widgets.ethCurrPriceLabel.setText('$'+str(self.dash_eth['Closing'].iat[-1]))
        widgets.dogeCurrPriceLabel.setText('$'+str(self.dash_doge['Closing'].iat[-1]))
        
        # self.dash_pred_graph()
        self.dash_histo_graph()

        # TRAIN PAGE
        widgets.trainContent.setCurrentWidget(widgets.getDataPage)
        widgets.btn_startTraining.hide()

        # TEST PAGE
        widgets.testContent.setCurrentWidget(widgets.testingPage)
        widgets.btn_viewDataAnalysis.hide()

        # DEPLOY PAGE
        widgets.deployPriceCombo.addItems(['Closing', 'High', 'Low'])


    def dash_data(self):
        self.dash_btc, self.dash_eth, self.dash_doge = import_data(self.selected_date)
        # print(self.dash_btc, self.dash_eth, self.dash_doge)

    def dash_histo_graph(self):
        widgets.histoGraph.clear()
        widgets.histoGraph.hide()
        
        # axis = DateAxisItem(orientation='bottom')
        # axis.attachToPlotItem(widgets.histoGraph.getPlotItem())

        past = self.selected_date - timedelta(days=self.selected_histo_day)
        df_date = []
        df_price = []

        if self.selected_crypto == 'all':
            widgets.histoGraph.clear()
            print('all')
        
        else:
            if self.selected_crypto == 'Bitcoin_Data':
                widgets.histoGraph.clear()
                df_ = self.dash_btc.loc[(self.dash_btc['Date'] >= past) & (self.dash_btc['Date'] <= self.selected_date)]
                df_date = df_['Date']
                df_price = df_[str(self.selected_histo_price)]

            if self.selected_crypto == 'Ethereum_Data':
                widgets.histoGraph.clear()
                df_ = self.dash_eth.loc[(self.dash_eth['Date'] >= past) & (self.dash_eth['Date'] <= self.selected_date)]
                df_date = df_['Date']
                df_price = df_[str(self.selected_histo_price)]

            if self.selected_crypto == 'Dogecoin_Data':
                widgets.histoGraph.clear()
                df_ = self.dash_doge.loc[(self.dash_doge['Date'] >= past) & (self.dash_doge['Date'] <= self.selected_date)]
                df_date = df_['Date']
                df_price = df_[str(self.selected_histo_price)]

            x = []
            y = []
            for item in df_date:
                item = datetime.timestamp(item)
                x.append(item)
            for item in df_price:
                y.append(item)

            # widgets.histoGraph.axis.plot(x, y)
            # widgets.histoGraph.canvas.draw()

            # axis = DateAxisItem(orientation='bottom')
            # axis.attachToPlotItem(widgets.histoGraph.getPlotItem())

            # labels = [ (date, datetime.fromtimestamp(date).strftime('%Y %b/%d')) for date in x ]

            if self.selected_histo_day >= 30:
                widgets.histoGraph.plot(x, y, pen=mkPen('#8C88BF', width=2.5))  # , labels=labels
            else: 
                widgets.histoGraph.plot(x, y, pen=mkPen('#8C88BF', width=2.5), symbol='o', symbolBrush = 0.2)
            
            # ax = widgets.histoGraph.getAxis('bottom')
            # ax.setTicks([labels])

            widgets.histoGraph.show()

            del df_, df_date, df_price

    def dash_pred_graph(self):
        self.df_ = get_prediction_df(self.dash_btc, self.selected_date)

        widgets.predGraph.clear()
        widgets.predictedTable.clear()
        widgets.predGraph.hide()
        
        df_date = []
        df_price = []

        if self.selected_crypto == 'all':
            widgets.predGraph.clear()
            print('all')

            del self.df_
        
        else:
            if self.selected_crypto == 'Bitcoin_Data':
                widgets.predGraph.clear()
                df_ = self.df_.loc[(self.df_['Date'] >= self.selected_date) & (self.df_['Date'] <= pd.to_datetime(self.pred_day_date))]
                df_date = df_['Date']
                df_price = df_[str(self.selected_predicted_price)]

            if self.selected_crypto == 'Ethereum_Data':
                widgets.predGraph.clear()
                df_ = self.df_.loc[(self.df_['Date'] >= self.selected_date) & (self.df_['Date'] <= pd.to_datetime(self.pred_day_date))]
                df_date = df_['Date']
                df_price = df_[str(self.selected_predicted_price)]

            if self.selected_crypto == 'Dogecoin_Data':
                widgets.predGraph.clear()
                df_ = self.df_.loc[(self.df_['Date'] >= self.selected_date) & (self.df_['Date'] <= pd.to_datetime(self.pred_day_date))]
                df_date = df_['Date']
                df_price = df_[str(self.selected_predicted_price)]

            # del df_

            x = []
            y = []
            for item in df_date:
                item = datetime.timestamp(item)
                x.append(item)
            for item in df_price:
                y.append(item)

            widgets.predGraph.plot(x, y, pen=mkPen('#259CA5', width=2.5), symbol='o', symbolBrush = 0.2)

            widgets.predGraph.show()

            df_ = df_[['Date', str(self.selected_predicted_price)]]
            df_['Date'] = df_['Date'].dt.date

            widgets.predictedTable.setColumnCount(len(df_.columns))
            widgets.predictedTable.setRowCount(len(df_.index))

            for i in range(len(df_.index)):
                for j in range(len(df_.columns)):
                    item = QTableWidgetItem(str(df_.iat[i, j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    widgets.predictedTable.setItem(i, j, item)

            widgets.predictedTable.setHorizontalHeaderLabels(df_.columns)
            widgets.predictedTable.resizeColumnsToContents()
            widgets.predictedTable.resizeRowsToContents()

            del df_, self.df_, df_date, df_price

    # def dash_pred_table(self):
    #     widgets.predictedTable.setHorizontalHeaderLabels()

    def train_dataset_table(self):
        self.dataset_table_df = get_dataset_df(self.dataset_date_from, self.dataset_date_until,
                                    self.dataset_crypto, self.dataset_source)
        self.dataset_table_df.to_csv('csv/dataset.csv')

        widgets.trainTable.setColumnCount(len(self.dataset_table_df.columns))
        widgets.trainTable.setRowCount(len(self.dataset_table_df.index))

        for i in range(len(self.dataset_table_df.index)):
            for j in range(len(self.dataset_table_df.columns)):
                item = QTableWidgetItem(str(self.dataset_table_df.iat[i, j]))
                item.setTextAlignment(Qt.AlignCenter)
                widgets.trainTable.setItem(i, j, item)

        widgets.trainTable.setHorizontalHeaderLabels(self.dataset_table_df.columns)
        widgets.trainTable.resizeColumnsToContents()
        widgets.trainTable.resizeRowsToContents()


    def dashSignals(self):
        # BUTTON SIGNALS
        # LEFT MENUS
        widgets.btn_dash.clicked.connect(self.buttonClick)
        widgets.btn_train.clicked.connect(self.buttonClick)
        widgets.btn_test.clicked.connect(self.buttonClick)
        widgets.btn_deploy.clicked.connect(self.buttonClick)
        widgets.btn_logout.clicked.connect(self.logout)

        # DASHBOARD BUTTONS
        widgets.dateEdit.dateTimeChanged.connect(self.get_selected_date)
        widgets.btn_all.clicked.connect(self.get_selected_crypto)
        widgets.btn_btc.clicked.connect(self.get_selected_crypto)
        widgets.btn_eth.clicked.connect(self.get_selected_crypto)
        widgets.btn_doge.clicked.connect(self.get_selected_crypto)

        widgets.btn_histo_closing.clicked.connect(self.get_price)
        widgets.btn_histo_high.clicked.connect(self.get_price)
        widgets.btn_histo_low.clicked.connect(self.get_price)

        # widgets.btn_0.clicked.connect(self.get_histo_day)
        widgets.btn_1.clicked.connect(self.get_histo_day)
        widgets.btn_2.clicked.connect(self.get_histo_day)
        widgets.btn_3.clicked.connect(self.get_histo_day)
        widgets.btn_4.clicked.connect(self.get_histo_day)
        
        widgets.btn_pred_closing.clicked.connect(self.get_price)
        widgets.btn_pred_high.clicked.connect(self.get_price)
        widgets.btn_pred_low.clicked.connect(self.get_price)

        widgets.horizontalSlider.valueChanged.connect(self.get_pred_day)


    def trainSignals(self):
        # GET DATA
        widgets.btn_proceed.clicked.connect(self.get_dataset_selection)
        widgets.btn_cancel.clicked.connect(self.cancel_selection)

        # START TRAINING
        widgets.btn_startTraining.clicked.connect(self.show_terminal)


    def testSignals(self):
        # START TESTING
        widgets.btn_startTesting.clicked.connect(self.show_terminal)
        widgets.btn_getData.clicked.connect(self.buttonClick)

        # DATA ANALYSIS
        widgets.btn_viewDataAnalysis.clicked.connect(self.show_data_analysis)
        # widgets.testCryptoCombo.activated.connect(self.get_crypto_analyze)


    def deploySignals(self):
        widgets.btn_deployDeploy.clicked.connect(self.deploy_prediction)


    def buttonClick(self):
        # /////// Empty dataframes
        self.dataset_table_df = pd.DataFrame()
        self.dash_btc = pd.DataFrame()
        self.dash_eth = pd.DataFrame()
        self.dash_doge = pd.DataFrame()

        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW DASHBOARD PAGE
        if btnName == "btn_dash":
            widgets.stackedWidget.setCurrentWidget(widgets.dash)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.dash_data()

        # SHOW TRAIN PAGE
        if btnName == "btn_train":
            widgets.stackedWidget.setCurrentWidget(widgets.train)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_getData":
            widgets.testTimeFrameList.clear()
            widgets.testCryptoList.clear()
            widgets.testSourceList.clear()

            widgets.deployTimeFrameList.clear()
            widgets.deployCryptoList.clear()
            widgets.deploySourceList.clear()

            self.cancel_selection()

            widgets.stackedWidget.setCurrentWidget(widgets.train)
            widgets.trainContent.setCurrentWidget(widgets.getDataPage)
            UIFunctions.resetStyle(self, "btn_train")
            widgets.btn_train.setStyleSheet(UIFunctions.selectMenu(widgets.btn_train.styleSheet()))

        # SHOW TEST PAGE
        if btnName == "btn_test":
            widgets.stackedWidget.setCurrentWidget(widgets.test)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            

        # SHOW DEPLOY PAGE
        if btnName == "btn_deploy":
            widgets.stackedWidget.setCurrentWidget(widgets.deploy)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        
        # print(self.dash_btc)

        # # PRINT BTN NAME
        # print(f'Button "{btnName}" pressed!')


    def logout(self):
        self.window = Login()
        # self.windows.append(window)
        self.window.show()
        self.close()


    def get_selected_date(self):
        date = widgets.dateEdit.date()
        widgets.selected_dateLabel.setText(date.toString('MMMM d, yyyy'))
        self.selected_date = date.toString()
        self.selected_date = pd.to_datetime(self.selected_date)
        self.dash_data()

        widgets.btcCurrPriceLabel.clear()
        widgets.ethCurrPriceLabel.clear()
        widgets.dogeCurrPriceLabel.clear()

        widgets.btcCurrPriceLabel.setText('$'+str(self.dash_btc['Closing'].iat[-1]))
        widgets.ethCurrPriceLabel.setText('$'+str(self.dash_eth['Closing'].iat[-1]))
        widgets.dogeCurrPriceLabel.setText('$'+str(self.dash_doge['Closing'].iat[-1]))

        self.dash_pred_graph()
        self.dash_histo_graph()


    def get_selected_crypto(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # ALL CRYPTO
        if btnName == "btn_all":
            self.selected_crypto = 'all'
            card = 'all'
            UIFunctions.resetCardStyle(self, card)

        else:
            # BTC
            if btnName == "btn_btc":
                self.selected_crypto = 'Bitcoin_Data'
                card = 'btc_card'
                card_frame = widgets.btc_card

            # ETH
            if btnName == "btn_eth":
                self.selected_crypto = 'Ethereum_Data'
                card = 'eth_card'
                card_frame = widgets.eth_card

            # DOGE
            if btnName == "btn_doge":
                self.selected_crypto = 'Dogecoin_Data'
                card = 'doge_card'
                card_frame = widgets.doge_card

            UIFunctions.resetCardStyle(self, card)
            card_frame.setStyleSheet(UIFunctions.selectCard(card_frame.styleSheet()))

        UIFunctions.resetCryptoStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectCrypto(btn.styleSheet()))
        
        self.dash_pred_graph()
        self.dash_histo_graph()


    def get_price(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'btn_histo_closing':
            self.selected_histo_price = 'Closing'
            self.dash_histo_graph()
        
        if btnName == 'btn_histo_high':
            self.selected_histo_price = 'High'
            self.dash_histo_graph()

        if btnName == 'btn_histo_low':
            self.selected_histo_price = 'Low'
            self.dash_histo_graph()

        if btnName == 'btn_pred_closing':
            self.selected_predicted_price = 'Closing'
            self.dash_pred_graph()
        
        if btnName == 'btn_pred_high':
            self.selected_predicted_price = 'High'
            self.dash_pred_graph()
        
        if btnName == 'btn_pred_low':
            self.selected_predicted_price = 'Low'
            self.dash_pred_graph()

        UIFunctions.resetPriceStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectPrice(btn.styleSheet()))


    def get_histo_day(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # if btnName == 'btn_0':
        #     self.selected_histo_day = 1

        if btnName == 'btn_1':
            self.selected_histo_day = 3
        
        if btnName == 'btn_2':
            self.selected_histo_day = 7

        if btnName == 'btn_3':
            self.selected_histo_day = 30

        if btnName == 'btn_4':
            self.selected_histo_day = 365


        # for i in range(5):
        #     btn_ = 'btn_' + str(i)
        #     if btnName == btn_:
        #         self.selected_histo_day = i + 1

        UIFunctions.resetHistoDayStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectHistoDay(btn.styleSheet()))

        self.dash_histo_graph()


    def get_pred_day(self):
        widgets.daysValue.setNum
        self.selected_predicted_day = int(widgets.daysValue.text())
        # print(self.selected_predicted_day)

        self.pred_day_date = self.selected_date + timedelta(days=self.selected_predicted_day)
        # print(self.pred_day_date)
        str_sel_date = self.selected_date.strftime('%b. %d, %Y')
        str_pred_date = self.pred_day_date.strftime('%b. %d, %Y')

        # print(str_sel_date+' - '+str_pred_date)
        widgets.predictedRangeLabel.setText(str_sel_date+' - '+str_pred_date)

        self.dash_pred_graph()


    def get_dataset_selection(self):
        widgets.testTimeFrameList.clear()
        widgets.testCryptoList.clear()
        widgets.testSourceList.clear()

        widgets.deployTimeFrameList.clear()
        widgets.deployCryptoList.clear()
        widgets.deploySourceList.clear()

        widgets.testCryptoCombo.clear()
        widgets.deployCryptoCombo.clear()

        widgets.trainTable.clear()

        widgets.btn_proceed.setEnabled(False)
        

        # DATE
        self.dataset_date_from = widgets.trainFromDateEdit.date().toString()
        self.dataset_date_from = pd.to_datetime(self.dataset_date_from).date()

        self.dataset_date_until = widgets.trainUntilDateEdit.date().toString()
        self.dataset_date_until = pd.to_datetime(self.dataset_date_until).date()

        # CRYPTO
        for checkBox in widgets.cryptoCheckBox.findChildren(QCheckBox):
            if checkBox.isChecked() == True:
                self.dataset_crypto.append(checkBox.text())
        
        # SOURCE
        for checkBox in widgets.sourceCheckBox.findChildren(QCheckBox):
            if checkBox.isChecked() == True:
                self.dataset_source.append(checkBox.text())

        self.train_dataset_table()
        widgets.trainTable.show()
        widgets.btn_startTraining.show()

        # print(self.dataset_date_from)
        # print(self.dataset_date_until)
        # print(self.dataset_crypto)
        # print(self.dataset_source)

        widgets.testTimeFrameList.addItems([str(self.dataset_date_from), str(self.dataset_date_until)])
        widgets.testCryptoList.addItems(self.dataset_crypto)
        widgets.testSourceList.addItems(self.dataset_source)

        widgets.deployTimeFrameList.addItems([str(self.dataset_date_from), str(self.dataset_date_until)])
        widgets.deployCryptoList.addItems(self.dataset_crypto)
        widgets.deploySourceList.addItems(self.dataset_source)

        widgets.testCryptoCombo.addItems(self.dataset_crypto)
        widgets.deployCryptoCombo.addItems(self.dataset_crypto)


    def cancel_selection(self):
        # DATE
        widgets.trainFromDateEdit.setDate(QDate(2020, 1, 1))
        widgets.trainUntilDateEdit.setDate(QDate(2021, 5, 31))
        self.dataset_date_from = None
        self.dataset_date_until = None

        # CRYPTO
        for checkBox in widgets.cryptoCheckBox.findChildren(QCheckBox):
            checkBox.setChecked(False)
        self.dataset_crypto = list()
        
        # # SOURCE
        # for checkBox in widgets.sourceCheckBox.findChildren(QCheckBox):
        #     checkBox.setChecked(False)
        # self.dataset_source = list()

        widgets.btn_startTraining.hide()

        # print(self.dataset_date_from)
        # print(self.dataset_date_until)
        # print(self.dataset_crypto)
        # print(self.dataset_source)

        widgets.testTimeFrameList.clear()
        widgets.testCryptoList.clear()
        widgets.testSourceList.clear()

        widgets.deployTimeFrameList.clear()
        widgets.deployCryptoList.clear()
        widgets.deploySourceList.clear()

        widgets.trainTable.clear()
        widgets.trainTable.hide()

        widgets.btn_proceed.setEnabled(True)


    def get_crypto_analyze(self, value):
        self.analyze_crypto = str(value)
        # print(self.analyze_crypto)

        self.show_data_analysis()


    def show_data_analysis(self):
        widgets.testContent.setCurrentWidget(widgets.dataAnalysisPage)
        widgets.btn_viewDataAnalysis.hide()

        # self.get_crypto_analyze()
        self.analyze_crypto = str(widgets.testCryptoCombo.currentText())
        widgets.testCryptoCombo.currentTextChanged.connect(self.get_crypto_analyze)
        crypto_df = pd.DataFrame()

        if self.analyze_crypto.startswith('Bitcoin') == True:
            crypto_df = pd.read_csv("csv/BTC_Sample.csv")

        if self.analyze_crypto.startswith('Ethereum') == True:
            crypto_df = pd.read_csv("csv/ETH_Sample.csv")
        
        if self.analyze_crypto.startswith('Dogecoin') == True:
            crypto_df = pd.read_csv("csv/DOGE_Sample.csv")

        # CORRELATION
        corr_analysis(crypto_df)

        # Create Graph
        # widgets.corrAnalysisGraph = QLabel(widgets.corrAnalysisGraphFrame)
        pixmap = QPixmap('images/corr.png')
        pixmap = pixmap.scaled(471, 324, Qt.KeepAspectRatioByExpanding, Qt.FastTransformation)
        widgets.corrAnalysisGraph.setPixmap(pixmap)
        

        # CONFUSION MATRIX
        class_df = classification_analysis(crypto_df)

        # Create Graph
        # widgets.conMatrixGraph = QLabel(widgets.conMatrixGraphFrame)
        pixmap = QPixmap('images/conf.png')
        pixmap = pixmap.scaled(471, 324, Qt.KeepAspectRatioByExpanding, Qt.FastTransformation)
        widgets.conMatrixGraph.setPixmap(pixmap)
        
        del crypto_df


    def show_terminal(self):
        # /////// Empty dataframe
        self.dataset_table_df = pd.DataFrame()

        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'btn_startTraining':
            widgets.trainContent.setCurrentWidget(widgets.startTrainingPage)
            widgets.btn_startTraining.hide()

            # self.showMinimized()
            self.hide()
            print("LOADING DATA...")  # working on loading screen

            # command_line = 'python model/training_model.py'
            # p = os.popen(command_line)
            # if p:
            #     widgets.trainTerminal.clear()
            #     output = p.read()
            #     widgets.trainTerminal.insertPlainText(output)

            # self.setWindowState(Qt.WindowNoState)
            self.show()

        if btnName == 'btn_startTesting':
            widgets.btn_viewDataAnalysis.show()

            # command_line = 'python model/testing_model.py'
            # p = os.popen(command_line)
            # if p:
            #     widgets.testTerminal.clear()
            #     output = p.read()
            #     widgets.testTerminal.insertPlainText(output)


    def deploy_prediction(self):
        print('hello Deploy!!!')


    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos
        # self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("icon.ico"))
    window = Login()
    window.show()
    sys.exit(app.exec())