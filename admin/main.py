# ------------------------------------------------------------------------------------------- #
#    CRYPTIC: AN IMPROVED CNN-LSTM CRYPTOCURRENCY PRICE FORECASTING USING INTERNET TRENDS
# 
# Authors:
# Arconado, Kristine N.             Dalay, Jeremy Tristen A.
# Berse, Nikko R.                   Faustino, Kyle C.
# 
# BSCS 4-2 AY 2021-2022
# ------------------------------------------------------------------------------------------- #

import sys, os
import time
import pyrebase, requests, json

from modules import *
from dbconnect import *
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
            
        except Exception as e:
            error = json.loads(e.args[1])['error']['message']
            print(error)
            self.ui.username_login.clear()
            self.ui.pass_login.clear()

            AppFunctions.popup(self, 1)
            self.Popup.ui.cancel.clicked.connect(lambda: self.Popup.close())
            self.Popup.ui.error_message.setText(str(error)+". Try Again?")
            self.Popup.ui.cancel.setText('OK')

    
    def signupfunction(self):
        self.ui.username_login.clear()
        self.ui.pass_login.clear()

        email = self.ui.username_signup.text()
        if self.ui.pass_signup.text() == self.ui.confirmPass.text():
            password = self.ui.pass_signup.text()

            try:
                auth.create_user_with_email_and_password(email, password)
                self.ui.content.setCurrentWidget(self.ui.loginPage)
            
            except requests.HTTPError as e:
                error = json.loads(e.args[1])['error']['message']
                print(error)
                self.ui.username_signup.clear()
                self.ui.pass_signup.clear()
                self.ui.confirmPass.clear()

                AppFunctions.popup(self, 1)
                self.Popup.ui.cancel.clicked.connect(lambda: self.Popup.close())
                self.Popup.ui.error_message.setText(str(error)+"\nTry Again?")
                self.Popup.ui.cancel.setText('OK')
        else:
            error = 'PASSWORD NOT MATCH'
            AppFunctions.popup(self, 1)
            self.Popup.ui.cancel.clicked.connect(lambda: self.Popup.close())
            self.Popup.ui.error_message.setText(str(error)+". Try Again?")
            self.Popup.ui.cancel.setText('OK')
    

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos
        # self.dragPos = event.globalPos()


# Main Window Dashboard
# from model import *

widgets = None
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        global widgets
        widgets = self.ui
        widgets.setupUi(self)

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
        self.retrained = False

        # QTableWidget Stretch
        widgets.predictedTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widgets.trainTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widgets.dataAnalysisTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widgets.deployTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setDefaultDisplay()
        self.signals()


    # ///////////////////////////////////////////
    # DISPLAY GUI
    def setDefaultDisplay(self):
        # DEFAULTS
        # DATE
        widgets.selected_dateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        date = widgets.dateEdit.date()
        widgets.selected_dateLabel.setText(date.toString('MMMM d, yyyy'))
        self.selected_date = date.toString()
        self.selected_date = pd.to_datetime(self.selected_date)
         
        # DASH PAGE
        widgets.stackedWidget.setCurrentWidget(widgets.dash)
        widgets.btn_dash.setStyleSheet(UIFunctions.selectMenu(widgets.btn_dash.styleSheet()))

        widgets.btn_all.setStyleSheet(UIFunctions.selectCrypto(widgets.btn_all.styleSheet()))
        # widgets.btc_card.setStyleSheet(UIFunctions.selectCard(widgets.btc_card.styleSheet()))
        
        # widgets.btn_pred_closing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_pred_closing.styleSheet()))
        widgets.btn_histo_closing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_histo_closing.styleSheet()))

        widgets.btn_3.setStyleSheet(UIFunctions.selectHistoDay(widgets.btn_3.styleSheet()))

        # TRAIN PAGE
        widgets.trainContent.setCurrentWidget(widgets.getDataPage)
        widgets.btn_startTraining.hide()

        for checkBox in widgets.sourceCheckBox.findChildren(QRadioButton):
            if checkBox.isChecked() == True:
                print('the audacity !')

        # TEST PAGE
        widgets.testContent.setCurrentWidget(widgets.testingPage)
        widgets.btn_viewDataAnalysis.hide()

        # VALUES
        self.selected_crypto = 'btn_all'
        self.selected_predicted_price = 'Price'
        self.selected_histo_price = 'Closing'
        self.selected_histo_day = 30

        self.get_pred_day()
        self.access_db()


    # ///////////////////////////////////////////
    # SIGNALS
    def signals(self):
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

        widgets.horizontalSlider.valueChanged.connect(self.get_pred_day)

        # TRAIN
        widgets.btn_proceed.clicked.connect(lambda: AppFunctions.get_dataset_selection(self))
        widgets.btn_cancel.clicked.connect(lambda: AppFunctions.cancel_selection(self))
        widgets.btn_startTraining.clicked.connect(self.show_terminal)

        # TEST
        self.disable('test')
        widgets.btn_getData.clicked.connect(self.buttonClick)
        widgets.btn_viewDataAnalysis.clicked.connect(self.show_data_analysis)

        # DEPLOY
        self.disable('deploy')
        widgets.btn_reset.clicked.connect(self.reset_all)

    
    # ///////////////////////////////////////////
    # SIDE MENU
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_getData":
            self.window = MainWindow()
            self.window.ui.stackedWidget.setCurrentWidget(self.window.ui.train)
            self.window.ui.trainContent.setCurrentWidget(self.window.ui.getDataPage)
            UIFunctions.resetStyle(self.window, "btn_train")
            self.window.ui.btn_train.setStyleSheet(UIFunctions.selectMenu(self.window.ui.btn_train.styleSheet()))
            self.window.show()
            self.close()

        else:
            # SHOW DASHBOARD PAGE
            if btnName == "btn_dash":
                widgets.stackedWidget.setCurrentWidget(widgets.dash)

            # SHOW TRAIN PAGE
            if btnName == "btn_train":
                widgets.stackedWidget.setCurrentWidget(widgets.train)

            # SHOW TEST PAGE
            if btnName == "btn_test":
                widgets.stackedWidget.setCurrentWidget(widgets.test)
                
            # SHOW DEPLOY PAGE
            if btnName == "btn_deploy":
                if (widgets.testContent.currentWidget() == widgets.dataAnalysisPage) and (self.retrained == False):
                    self.deploy_retrain()
                else:
                    widgets.stackedWidget.setCurrentWidget(widgets.deploy)
            
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
    

    # ///////////////////////////////////////////
    # SLOTS
    def deploy_retrain(self):
        self.retrained = True
        self.desc = '<strong>RETRAINING</strong> DATA'
        AppFunctions.loading(self)
        self.hide()
        AppFunctions.start_retrain_data(self)
    
    def catch_deploy_pred(self, dct):
        self.r_thread.quit()
        self.r_thread.wait()
        
        widgets.stackedWidget.setCurrentWidget(widgets.deploy)

        # DISPLAY PRED & TABLE
        self.dct = dct
        self.print()

        self.Dialog.ui.loadingBar.setRange(0, 1)
        self.Dialog.ui.loadingBar.setValue(1)
        self.Dialog.ui.subtitle.setText("Done!")

        QTimer.singleShot(1300, self.Dialog.close)
        QTimer.singleShot(1200, self.show)

    def get_deploy_crypto(self, value):
        self.deploy_crypto = str(value)

        self.display_deploy_crypto()

    def display_deploy_crypto(self):
        widgets.deployGraph.clear()
        widgets.deployTable.clear()

        if widgets.deployCryptoCombo.count() > 0:

            if self.deploy_crypto.startswith('Bitcoin') == True:
                my_dict = self.dct.get('btc')
                pen=mkPen('#F9AA4B', width=2.5)

            if self.deploy_crypto.startswith('Ethereum') == True:
                my_dict = self.dct.get('eth')
                pen=mkPen('#2082FA', width=2.5)
            
            if self.deploy_crypto.startswith('Dogecoin') == True:
                my_dict = self.dct.get('doge')
                pen=mkPen('#6374C3', width=2.5)


            df = my_dict[0]
            xy = my_dict[1]

            widgets.deployGraph.plot(xy[0], xy[1], pen=pen)
            widgets.deployTable.setColumnCount(len(df.columns))
            widgets.deployTable.setHorizontalHeaderLabels(df.columns)
            widgets.deployTable.setRowCount(len(df.index))

            for i in range(len(df.index)):
                for j in range(len(df.columns)):
                    item = QTableWidgetItem(str(df.iat[i, j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    widgets.deployTable.setItem(i, j, item)
            
            
            widgets.deployTable.resizeColumnsToContents()
            widgets.deployTable.show()
            widgets.deployTable.resizeRowsToContents()

            # print(xy)

    def print(self):
        # print(self.dct)

        widgets.deployCryptoCombo.currentTextChanged.connect(self.get_deploy_crypto)
        self.deploy_crypto = str(widgets.deployCryptoCombo.currentText())
        # print(self.deploy_crypto)
        self.display_deploy_crypto()
        

    def empty_ds(self):
        AppFunctions.popup(self, 2)
        self.Popup.ui.ok.clicked.connect(lambda: self.Popup.close())
        self.Popup.ui.cancel.clicked.connect(lambda: AppFunctions.cancel_selection(self))
        self.Popup.ui.error_message.setText(self.error_txt)
        self.Popup.ui.ok.setText('OK')
        self.Popup.ui.cancel.setText('CANCEL')

    def reset_all(self):
        self.window = MainWindow()
        self.window.ui.stackedWidget.setCurrentWidget(self.window.ui.deploy)
        UIFunctions.resetStyle(self.window, 'btn_deploy')
        self.window.ui.btn_deploy.setStyleSheet(UIFunctions.selectMenu(self.window.ui.btn_deploy.styleSheet()))
        self.window.show()
        self.close()

    def get_selected_date(self):
        date = widgets.dateEdit.date()
        widgets.selected_dateLabel.setText(date.toString('MMMM d, yyyy'))
        self.selected_date = date.toString()
        self.selected_date = pd.to_datetime(self.selected_date)

        self.access_db()

    def get_selected_crypto(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # ALL CRYPTO
        if btnName == "btn_all":
            card = 'all'
            UIFunctions.resetCardStyle(self, card)

        else:
            # BTC
            if btnName == "btn_btc":
                card = 'btc_card'
                card_frame = widgets.btc_card

            # ETH
            if btnName == "btn_eth":
                card = 'eth_card'
                card_frame = widgets.eth_card

            # DOGE
            if btnName == "btn_doge":
                card = 'doge_card'
                card_frame = widgets.doge_card

            UIFunctions.resetCardStyle(self, card)
            card_frame.setStyleSheet(UIFunctions.selectCard(card_frame.styleSheet()))

        UIFunctions.resetCryptoStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectCrypto(btn.styleSheet()))
        self.selected_crypto = btnName
        
        self.get_data()

    def get_price(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName.startswith('btn_histo'):
            if btnName == 'btn_histo_closing':
                self.selected_histo_price = 'Closing'
            
            if btnName == 'btn_histo_high':
                self.selected_histo_price = 'High'

            if btnName == 'btn_histo_low':
                self.selected_histo_price = 'Low'
                
            AppFunctions.dash_histo(self)

        if btnName.startswith('btn_pred'):
            if btnName == 'btn_pred_closing':
                self.selected_predicted_price = 'Closing'
            
            if btnName == 'btn_pred_high':
                self.selected_predicted_price = 'High'
            
            if btnName == 'btn_pred_low':
                self.selected_predicted_price = 'Low'
            
            AppFunctions.dash_pred(self)

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

        UIFunctions.resetHistoDayStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectHistoDay(btn.styleSheet()))

        # self.access_db()
        AppFunctions.dash_histo(self)

    def get_pred_day(self):
        self.ui.daysValue.setNum
        self.selected_predicted_day = int(self.ui.daysValue.text())

        self.pred_day_date = self.selected_date + timedelta(days=self.selected_predicted_day)

        # str_sel_date = self.selected_date.strftime('%b %d, %Y')
        # str_pred_date = self.pred_day_date.strftime('%b %d, %Y')

        # self.ui.predictedRangeLabel.setText(str_sel_date+' - '+str_pred_date)

        AppFunctions.dash_pred(self)

    def disable(self, arg):
        if arg == 'proceed':
            widgets.btn_proceed.setStyleSheet(widgets.btn_proceed.styleSheet() + MainSettings.DISABLED)
        if arg == 'test':
            widgets.btn_startTesting.setStyleSheet(widgets.btn_startTesting.styleSheet() + MainSettings.DISABLED)
            widgets.btn_startTesting.setEnabled(False)
        if arg == 'deploy':
            widgets.btn_deployDeploy.setStyleSheet(widgets.btn_deployDeploy.styleSheet() + MainSettings.DISABLED)
            widgets.btn_deployDeploy.setEnabled(False)
    
    def enable(self, arg):
        if arg == 'proceed':
            widgets.btn_proceed.setStyleSheet(widgets.btn_proceed.styleSheet().replace(MainSettings.DISABLED, ""))
        if arg == 'test':
            widgets.btn_startTesting.setStyleSheet(widgets.btn_startTesting.styleSheet().replace(MainSettings.DISABLED, ""))
            widgets.btn_startTesting.setEnabled(True)
        if arg == 'deploy':
            widgets.btn_deployDeploy.setStyleSheet(widgets.btn_deployDeploy.styleSheet().replace(MainSettings.DISABLED, ""))
            widgets.btn_deployDeploy.setEnabled(True)
    

    # ///////////////////////////////////////////
    # TRAIN & TEST TERMINAL DISPLAY
    def show_terminal(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'btn_startTraining':
            widgets.btn_startTraining.hide()
            self.enable('test')
            widgets.trainContent.setCurrentWidget(widgets.startTrainingPage)
            widgets.btn_startTesting.clicked.connect(self.show_terminal)
            self.process = 'train'
            self.desc = '<strong>TRAINING</strong> DATA'
        
        if btnName == 'btn_startTesting':
            widgets.btn_viewDataAnalysis.show()
            self.enable('deploy')
            widgets.btn_deployDeploy.clicked.connect(self.deploy)
            self.process = 'test'
            self.desc = '<strong>TESTING</strong> DATA'

        AppFunctions.loading(self)
        self.hide()
        self.p_thread = QThread()
        self.p_worker = ImplementModel(self.process)
        self.p_worker.moveToThread(self.p_thread)
        self.p_worker.process_complete.connect(self.catch_output)
        self.p_thread.started.connect(self.p_worker.run_terminal)
        self.p_thread.start()

    
    def deploy(self):
        self.process = 'deploy'
        self.desc = '<strong>DEPLOYING</strong> PREDICTED DATA'
        AppFunctions.loading(self)
        self.hide()
        self.d_thread = QThread()
        self.d_worker = ImplementModel(self.process)
        self.d_worker.moveToThread(self.d_thread)
        self.d_worker.deploy_complete.connect(self.complete)
        self.d_thread.started.connect(self.d_worker.run_terminal)
        self.d_thread.start()

    def complete(self):
        print('Complete!')
        self.d_thread.quit()
        self.d_thread.wait()

        self.Dialog.ui.loadingBar.setRange(0, 1)
        self.Dialog.ui.loadingBar.setValue(1)
        self.Dialog.ui.subtitle.setText("Done!")

        QTimer.singleShot(1300, self.Dialog.close)
        QTimer.singleShot(1200, self.show)

        del self.d_worker, self.d_thread

    
    # ///////////////////////////////////////////
    # DATA ANALYSIS
    def get_crypto_analyze(self, value):
        self.analyze_crypto = str(value)

        self.get_analysis()

    def get_analysis(self):
        widgets.corrAnalysisGraph.clear()
        widgets.conMatrixGraph.clear()
        widgets.dataAnalysisTable.clear()

        if widgets.testCryptoCombo.count() > 0:

            AppFunctions.get_accuracy(self)

            if self.analyze_crypto.startswith('Bitcoin') == True:
                corr = 'images\BTC_corr.png'
                conf = 'images\BTC_conf.png'

            if self.analyze_crypto.startswith('Ethereum') == True:
                corr = 'images\ETH_corr.png'
                conf = 'images\ETH_conf.png'
            
            if self.analyze_crypto.startswith('Dogecoin') == True:
                corr = 'images\DOGE_corr.png'
                conf = 'images\DOGE_conf.png'

            pixmap = QPixmap(corr)
            pixmap = pixmap.scaled(471, 324, Qt.KeepAspectRatioByExpanding, Qt.FastTransformation)
            widgets.corrAnalysisGraph.setPixmap(pixmap)

            pixmap = QPixmap(conf)
            pixmap = pixmap.scaled(471, 324, Qt.KeepAspectRatioByExpanding, Qt.FastTransformation)
            widgets.conMatrixGraph.setPixmap(pixmap)

    def show_data_analysis(self):
        widgets.testContent.setCurrentWidget(widgets.dataAnalysisPage)
        widgets.btn_viewDataAnalysis.hide()

        widgets.testCryptoCombo.currentTextChanged.connect(self.get_crypto_analyze)
        self.analyze_crypto = str(widgets.testCryptoCombo.currentText())
        self.get_analysis()


    # ///////////////////////////////////////////
    # CATCH THREAD SIGNALS
    def access_db(self):
        self.db_thread = QThread()
        self.db_worker = AccessDatabase(self.selected_date)
        self.db_worker.moveToThread(self.db_thread)
        self.db_worker.import_data_complete.connect(self.get_data)
        self.db_thread.started.connect(self.db_worker.access_now)
        self.db_thread.start()

    def get_data(self):
        self.db_thread.quit()
        self.db_thread.wait()
        AppFunctions.dash_pred(self)
        AppFunctions.dash_histo(self)

    def get_dataset(self):
        self.ds_worker =  ImportDataset(self.dataset_date_from, 
                                        self.dataset_date_until,
                                        self.dataset_crypto, 
                                        self.dataset_source)
        self.ds_worker.start()
        self.ds_worker.pass_dataset.connect(self.catch_dataset)

    def catch_output(self, output):
        self.p_thread.quit()
        self.p_thread.wait()
        
        if self.process == 'train':
            widgets.trainTerminal.clear()
            widgets.trainTerminal.insertPlainText(output)

        if self.process == 'test':
            widgets.testTerminal.clear()
            widgets.testTerminal.insertPlainText(output)

        self.Dialog.ui.loadingBar.setRange(0, 1)
        self.Dialog.ui.loadingBar.setValue(1)
        self.Dialog.ui.subtitle.setText("Done!")

        # QTimer.singleShot(1300, self.Dialog.close)
        # QTimer.singleShot(1200, self.show)
        self.show()
        self.Dialog.close()        

        # self.p_worker.stop()
        del self.p_worker, self.p_thread
        
    def catch_dataset(self, my_df):
        widgets.trainTable.setColumnCount(len(my_df.columns))
        widgets.trainTable.setHorizontalHeaderLabels(my_df.columns)
        widgets.trainTable.setRowCount(len(my_df.index))

        for i in range(len(my_df.index)):
            for j in range(len(my_df.columns)):
                item = QTableWidgetItem(str(my_df.iat[i, j]))
                item.setTextAlignment(Qt.AlignCenter)
                widgets.trainTable.setItem(i, j, item)
        
        
        widgets.trainTable.resizeColumnsToContents()
        widgets.trainTable.show()
        widgets.trainTable.resizeRowsToContents()
        
        self.ds_worker.quit()
        widgets.btn_startTraining.show()

    def catch_histo_data(self, histo_data):
        widgets.histoGraph.clear()
        btc = list()
        eth = list()
        doge = list()

        # if pd.to_datetime(self.selected_date).date() == datetime.now().date():
        #     print(self.selected_date)
        #     print(datetime.now().date())

        if self.selected_crypto == 'btn_all':
            for i, data in enumerate(histo_data):
                if i == 0:
                    btc = data
                    xy = btc[1]
                    x = xy[0]
                    y = xy[1]
                if i == 1:
                    eth = data
                    xy = eth[1]
                    y2 = xy[1]
                if i == 2:
                    doge = data
                    xy = doge[1]
                    y3 = xy[1]
            
            self.plot(x, y, 'BITCOIN', pen=mkPen('#F9AA4B', width=2.5))
            self.plot(x, y2, 'ETHEREUM', pen=mkPen('#2082FA', width=2.5))
            self.plot(x, y3, 'DOGECOIN', pen=mkPen('#6374C3', width=2.5))

            widgets.btcCurrPriceLabel.clear()
            widgets.ethCurrPriceLabel.clear()
            widgets.dogeCurrPriceLabel.clear()

            widgets.btcCurrPriceLabel.setText('$'+str(y[i]))
            widgets.ethCurrPriceLabel.setText('$'+str(y2[i]))
            widgets.dogeCurrPriceLabel.setText('$'+str(y3[i]))

        else:
            if self.selected_crypto == 'btn_btc':
                btc = histo_data[0]
                xy = btc[1]
                pen=mkPen('#F9AA4B', width=2.5)
            if self.selected_crypto == 'btn_eth':
                eth = histo_data[0]
                xy = eth[1]
                pen=mkPen('#2082FA', width=2.5)
            if self.selected_crypto == 'btn_doge':
                doge = histo_data[0]
                xy = doge[1]
                pen=mkPen('#6374C3', width=2.5)
            
            x = xy[0]
            y = xy[1]
            widgets.histoGraph.plot(x, y, pen=pen)

        self.h_worker.quit()
        # del self.h_worker
    
    def catch_pred_data(self, pred_data):
        widgets.predGraph.clear()
        widgets.predictedTable.clear()
        btc = list()
        eth = list()
        doge = list()

        if self.selected_crypto == 'btn_all':
            for i, data in enumerate(pred_data):
                if i == 0:
                    btc = data
                    xy = btc[1]
                    x = xy[0]
                    y = xy[1]
                if i == 1:
                    eth = data
                    xy = eth[1]
                    y2 = xy[1]
                if i == 2:
                    doge = data
                    xy = doge[1]
                    y3 = xy[1]
            
            self.pplot(x, y, 'BITCOIN', pen=mkPen('#F9AA4B', width=2.5))
            self.pplot(x, y2, 'ETHEREUM', pen=mkPen('#2082FA', width=2.5))
            self.pplot(x, y3, 'DOGECOIN', pen=mkPen('#6374C3', width=2.5))

            dates = list()
            for date in x:
                dates.append(datetime.fromtimestamp(int(date)).strftime('%Y-%m-%d'))
            tbl = pd.concat([pd.Series(dates,name='Date'),
                             pd.Series(y,name='BITCOIN'), 
                             pd.Series(y2,name='ETHEREUM'), 
                             pd.Series(y3,name='DOGECOIN')], axis=1)
            
            widgets.predictedTable.setColumnCount(len(tbl.columns))
            widgets.predictedTable.setRowCount(len(tbl.index))

            for i in range(len(tbl.index)):
                for j in range(len(tbl.columns)):
                    item = QTableWidgetItem(str(tbl.iat[i, j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    widgets.predictedTable.setItem(i, j, item)

            widgets.predictedTable.setHorizontalHeaderLabels(tbl.columns)
            widgets.predictedTable.resizeColumnsToContents()
            widgets.predictedTable.resizeRowsToContents()
            widgets.predictedTable.show()

        else:
            if self.selected_crypto == 'btn_btc':
                btc = pred_data[0]
                xy = btc[1]
                pen=mkPen('#F9AA4B', width=2.5)
                columns = btc[0].columns
                ind = btc[0].index
                new_df = btc[0]
            
            if self.selected_crypto == 'btn_eth':
                eth = pred_data[0]
                xy = eth[1]
                pen=mkPen('#2082FA', width=2.5)
                columns = eth[0].columns
                ind = eth[0].index
                new_df = eth[0]
            
            if self.selected_crypto == 'btn_doge':
                doge = pred_data[0]
                xy = doge[1]
                pen=mkPen('#6374C3', width=2.5)
                columns = doge[0].columns
                ind = doge[0].index
                new_df = doge[0]
            
            x = xy[0]
            y = xy[1]
            widgets.predGraph.plot(x, y, pen=pen)

            widgets.predictedTable.setColumnCount(len(columns))
            widgets.predictedTable.setRowCount(len(ind))

            for i in range(len(ind)):
                for j in range(len(columns)):
                    item = QTableWidgetItem(str(new_df.iat[i, j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    widgets.predictedTable.setItem(i, j, item)

            widgets.predictedTable.setHorizontalHeaderLabels(new_df.columns)
            widgets.predictedTable.resizeColumnsToContents()
            widgets.predictedTable.resizeRowsToContents()
            widgets.predictedTable.show()

        self.pg_worker.quit()
        # del self.pg_worker
    
    
    def plot(self, x, y, plot, pen):
        widgets.histoGraph.plot(x, y, name=plot, pen=pen)

    def pplot(self, x, y, plot, pen):
        widgets.predGraph.plot(x, y, name=plot, pen=pen)

    def catch_analysis(self, my_df):
        self.a_worker.quit()
        # del self.a_worker

        widgets.dataAnalysisTable.setColumnCount(len(my_df.columns))
        widgets.dataAnalysisTable.setHorizontalHeaderLabels(my_df.columns)
        widgets.dataAnalysisTable.setRowCount(len(my_df.index))

        for i in range(len(my_df.index)):
            for j in range(len(my_df.columns)):
                item = QTableWidgetItem(str(my_df.iat[i, j]))
                item.setTextAlignment(Qt.AlignCenter)
                widgets.dataAnalysisTable.setItem(i, j, item)
        
        
        # widgets.dataAnalysisTable.resizeColumnsToContents()
        widgets.dataAnalysisTable.show()
        widgets.dataAnalysisTable.resizeRowsToContents()

    
    # ///////////////////////////////////////////
    # LOGOUT
    def logout(self):
        self.window = Login()
        self.window.show()
        self.close()

    
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("icon.ico"))
    window = Login()
    window.show()
    sys.exit(app.exec())