import sys
import os
import pyrebase
import requests
import json

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
            # # self.windows.append(window)
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
            
            except requests.HTTPError as e:
                error = json.loads(e.args[1])['error']['message']
                print(error)
                self.ui.username_signup.clear()
                self.ui.pass_signup.clear()
                self.ui.confirmPass.clear()
        else:
            print('PASSWORD NOT MATCH')
    

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

        self.setDefaultDisplay()
        self.signals()
    

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
        
        widgets.btn_pred_closing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_pred_closing.styleSheet()))
        widgets.btn_histo_closing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_histo_closing.styleSheet()))

        widgets.btn_3.setStyleSheet(UIFunctions.selectHistoDay(widgets.btn_3.styleSheet()))

        # TRAIN PAGE
        widgets.trainContent.setCurrentWidget(widgets.getDataPage)
        widgets.btn_startTraining.hide()

        # TEST PAGE
        widgets.testContent.setCurrentWidget(widgets.testingPage)
        widgets.btn_viewDataAnalysis.hide()

        # VALUES
        self.selected_crypto = 'btn_all'
        self.selected_predicted_price = 'Closing'
        self.selected_histo_price = 'Closing'
        self.selected_histo_day = 30

        self.access_db()
        # AppFunctions.get_data(self)

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

        widgets.btn_pred_closing.clicked.connect(self.get_price)
        widgets.btn_pred_high.clicked.connect(self.get_price)
        widgets.btn_pred_low.clicked.connect(self.get_price)

        # widgets.btn_0.clicked.connect(self.get_histo_day)
        widgets.btn_1.clicked.connect(self.get_histo_day)
        widgets.btn_2.clicked.connect(self.get_histo_day)
        widgets.btn_3.clicked.connect(self.get_histo_day)
        widgets.btn_4.clicked.connect(self.get_histo_day)

        # ////////// widgets.horizontalSlider.valueChanged.connect(self.get_pred_day)

        # TRAIN
        widgets.btn_proceed.clicked.connect(lambda: AppFunctions.get_dataset_selection(self))
        widgets.btn_cancel.clicked.connect(lambda: AppFunctions.cancel_selection(self))
        widgets.btn_startTraining.clicked.connect(self.show_terminal)

        # TEST
        widgets.btn_startTesting.clicked.connect(self.show_terminal)
        widgets.btn_getData.clicked.connect(self.buttonClick)
        widgets.btn_viewDataAnalysis.clicked.connect(self.show_data_analysis)

    
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_getData":
            AppFunctions.cancel_selection(self)
            widgets.stackedWidget.setCurrentWidget(widgets.train)
            widgets.trainContent.setCurrentWidget(widgets.getDataPage)
            UIFunctions.resetStyle(self, "btn_train")
            widgets.btn_train.setStyleSheet(UIFunctions.selectMenu(widgets.btn_train.styleSheet()))

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
                widgets.stackedWidget.setCurrentWidget(widgets.deploy)
            
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
    

    def get_selected_date(self):
        date = widgets.dateEdit.date()
        widgets.selected_dateLabel.setText(date.toString('MMMM d, yyyy'))
        self.selected_date = date.toString()
        self.selected_date = pd.to_datetime(self.selected_date)

        self.access_db()
        # AppFunctions.get_data(self)


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
        
        # self.access_db()
        AppFunctions.get_data(self)

    def get_price(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'btn_histo_closing':
            self.selected_histo_price = 'Closing'
        
        if btnName == 'btn_histo_high':
            self.selected_histo_price = 'High'

        if btnName == 'btn_histo_low':
            self.selected_histo_price = 'Low'

        if btnName == 'btn_pred_closing':
            self.selected_predicted_price = 'Closing'
        
        if btnName == 'btn_pred_high':
            self.selected_predicted_price = 'High'
        
        if btnName == 'btn_pred_low':
            self.selected_predicted_price = 'Low'

        UIFunctions.resetPriceStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectPrice(btn.styleSheet()))

        # self.access_db()
        AppFunctions.get_data(self)

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
        AppFunctions.get_data(self)

    
    def show_terminal(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'btn_startTraining':
            widgets.btn_startTraining.hide()
            widgets.trainContent.setCurrentWidget(widgets.startTrainingPage)
        
        if btnName == 'btn_startTesting':
            widgets.btn_viewDataAnalysis.show()

    def show_data_analysis(self):
        widgets.testContent.setCurrentWidget(widgets.dataAnalysisPage)
        widgets.btn_viewDataAnalysis.hide()

    def logout(self):
        self.window = Login()
        # self.windows.append(window)
        self.window.show()
        self.close()

    def access_db(self):
        self.db_worker = AccessDatabase(self.selected_date)
        self.db_worker.start()
        # run = partial(self.db_worker.access_db, self.selected_date)
        # QTimer.singleShot(0, run)
        self.db_worker.import_data_complete.connect(lambda: AppFunctions.get_data(self))
    
    def get_dataset(self):
        self.ds_worker =  ImportDataset(self.dataset_date_from, 
                                        self.dataset_date_until,
                                        self.dataset_crypto, 
                                        self.dataset_source)
        self.ds_worker.start()
        self.ds_worker.pass_dataset.connect(self.catch_dataset)
        
    
    def catch_histo_data(self, histo_data):
        # print('catch_histo_data: ', histo_data)
        widgets.histoGraph.clear()
        btc = list()
        eth = list()
        doge = list()

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


        self.worker.terminate()

    def plot(self, x, y, plot, pen):
        widgets.histoGraph.plot(x, y, name=plot, pen=pen)

    def catch_dataset(self, my_df):
        widgets.trainTable.setColumnCount(len(my_df.columns))
        widgets.trainTable.setHorizontalHeaderLabels(my_df.columns)
        widgets.trainTable.setRowCount(len(my_df.index))

        for i in range(len(my_df.index)):
            for j in range(len(my_df.columns)):
                item = QTableWidgetItem(str(my_df.iat[i, j]))
                item.setTextAlignment(Qt.AlignCenter)
                widgets.trainTable.setItem(i, j, item)

        widgets.trainTable.show()
        widgets.trainTable.resizeColumnsToContents()
        widgets.trainTable.resizeRowsToContents()

        self.ds_worker.terminate()
        
        widgets.btn_startTraining.show()

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