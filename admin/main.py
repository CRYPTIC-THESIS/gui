import sys
import os

import numpy as np

from modules import *
os.environ["QT_FONT_DPI"] = "96"


# Login Window
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Login_MainWindow()
        self.ui.setupUi(self)

        # CUSTOM TITLE BAR
        LoginSettings.ENABLE_CUSTOM_TITLE_BAR = True

        # UI FUNCTIONS DEFINITIONS
        UIFunctions.ui_logindefinitions(self)
        
        self.ui.content.setCurrentWidget(self.ui.loginPage)
        
        self.ui.btn_login.clicked.connect(self.loginfunction)
        self.ui.btn_toSignup.clicked.connect(lambda : self.ui.content.setCurrentWidget(self.ui.signupPage))
        
        self.ui.btn_signup.clicked.connect(self.signupfunction)
        self.ui.btn_toLogin.clicked.connect(lambda : self.ui.content.setCurrentWidget(self.ui.loginPage))

        self.windows = list()

    def loginfunction(self):
        username = self.ui.username_login.text()
        password = self.ui.pass_login.text()
        print("username: ", username, "password: ", password)
        
        self.close()
        window = MainWindow()
        self.windows.append(window)
        window.show()

    
    def signupfunction(self):
        username = self.ui.username_signup.text()
        if self.ui.pass_signup.text() == self.ui.confirmPass.text():
            password = self.ui.pass_signup.text()
            print("username: ", username, "password: ", password)
            self.ui.content.setCurrentWidget(self.ui.loginPage)

    
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


# Main Window Dashboard
widgets = None
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        global widgets
        widgets = self.ui
        widgets.setupUi(self)

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
        self.selected_predicted_day = int(widgets.daysValue.text())

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
        self.dash_btc = pd.DataFrame()
        self.dash_eth = pd.DataFrame()
        self.dash_doge = pd.DataFrame()

        self.dash_btc, self.dash_eth, self.dash_doge = import_data(self.selected_date)
        print('dash_data')
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
                print(self.dash_btc[self.selected_histo_price])
                
                df_ = self.dash_btc.loc[(self.dash_btc['Date'] >= past) & (self.dash_btc['Date'] <= self.selected_date)]
                df_date = df_['Date']
                df_price = df_[str(self.selected_histo_price)]

            if self.selected_crypto == 'Ethereum_Data':
                widgets.histoGraph.clear()
                print(self.dash_eth[self.selected_histo_price])
                
                df_ = self.dash_eth.loc[(self.dash_eth['Date'] >= past) & (self.dash_eth['Date'] <= self.selected_date)]
                df_date = df_['Date']
                df_price = df_[str(self.selected_histo_price)]

            if self.selected_crypto == 'Dogecoin_Data':
                widgets.histoGraph.clear()
                print(self.dash_doge[self.selected_histo_price])
                
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
                widgets.histoGraph.plot(x, y, pen=mkPen('#4ad29f', width=2.5))  # , labels=labels
            else: 
                widgets.histoGraph.plot(x, y, pen=mkPen('#4ad29f', width=2.5), symbol='o', symbolBrush = 0.2)
            
            # ax = widgets.histoGraph.getAxis('bottom')
            # ax.setTicks([labels])

            widgets.histoGraph.show()

    def dash_pred_graph(self):
        print('hello dash pred graph')

    def dash_pred_table(self):
        widgets.predictedTable.setHorizontalHeaderLabels()

    def train_dataset_table(self):
        self.dataset_table_df = get_dataset_df(self.dataset_date_from, self.dataset_date_until,
                                    self.dataset_crypto, self.dataset_source)
        print(self.dataset_table_df)
        self.dataset_table_df.to_csv('dataset.csv')

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
        widgets.btn_viewDataAnalysis.clicked.connect(self.next_page)


    def deploySignals(self):
        widgets.btn_deployDeploy.clicked.connect(self.deploy_prediction)


    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW DASHBOARD PAGE
        if btnName == "btn_dash":
            widgets.stackedWidget.setCurrentWidget(widgets.dash)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

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


        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


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
        
        if btnName == 'btn_pred_high':
            self.selected_predicted_price = 'High'
        
        if btnName == 'btn_pred_low':
            self.selected_predicted_price = 'Low'

        UIFunctions.resetPriceStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectPrice(btn.styleSheet()))

        self.dash_histo_graph()

        print(self.selected_histo_price)
        print(self.selected_predicted_price)


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
        print(self.selected_histo_day)


    def get_pred_day(self):
        widgets.daysValue.setNum
        self.selected_predicted_day = widgets.daysValue.text()
        print(self.selected_predicted_day)


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

        print(self.dataset_date_from)
        print(self.dataset_date_until)
        print(self.dataset_crypto)
        print(self.dataset_source)

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
        
        # SOURCE
        for checkBox in widgets.sourceCheckBox.findChildren(QCheckBox):
            checkBox.setChecked(False)
        self.dataset_source = list()

        widgets.btn_startTraining.hide()

        print(self.dataset_date_from)
        print(self.dataset_date_until)
        print(self.dataset_crypto)
        print(self.dataset_source)

        widgets.testTimeFrameList.clear()
        widgets.testCryptoList.clear()
        widgets.testSourceList.clear()

        widgets.deployTimeFrameList.clear()
        widgets.deployCryptoList.clear()
        widgets.deploySourceList.clear()

        widgets.trainTable.clear()
        widgets.trainTable.hide()

        widgets.btn_proceed.setEnabled(True)


    def next_page(self):
        widgets.testContent.setCurrentWidget(widgets.dataAnalysisPage)
        widgets.btn_viewDataAnalysis.hide()


    def show_terminal(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'btn_startTraining':
            widgets.trainContent.setCurrentWidget(widgets.startTrainingPage)
            widgets.btn_startTraining.hide()

            command_line = 'python model/training_model.py'
            p = os.popen(command_line)
            if p:
                widgets.trainTerminal.clear()
                output = p.read()
                widgets.trainTerminal.insertPlainText(output)

        if btnName == 'btn_startTesting':
            widgets.btn_viewDataAnalysis.show()

            command_line = 'python model/testing_model.py'
            p = os.popen(command_line)
            if p:
                widgets.testTerminal.clear()
                output = p.read()
                widgets.testTerminal.insertPlainText(output)


    def deploy_prediction(self):
        print('hello Deploy!!!')


    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("icon.ico"))
    window = Login()
    window.show()
    sys.exit(app.exec())