import sys
import os
import time

from functools import partial

from modules import *
from dbconnect import *
os.environ["QT_FONT_DPI"] = "96"


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, Qt.WA_DeleteOnClose)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.access_db()
    
    def access_db(self):
        self.worker = AccessDatabase()
        self.worker.start()
        self.worker.import_data_complete.connect(self.catch_db_data)
        self.worker.update_progress.connect(self.evt_update_progress)

    def evt_update_progress(self, ctr):
        self.ui.progressBar.setValue(ctr)
        if ctr == 35:
            self.ui.label.setText("<strong>LOADING</strong> DATABASE")
        if ctr == 75:
            self.ui.label.setText("<strong>LOADING</strong> USER INTERFACE")
        if ctr == 100:
            self.worker.terminate()
            self.window = MainWindow()
            self.window.show()
            self.close()

    def catch_db_data(self):
        print('Successfully imported db data.')
        self.show()
        # print(db_data)
        # self.close()


widgets = None
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        global widgets
        widgets = self.ui
        widgets.setupUi(self)

        # SET UI FUNCTIONS
        UIFunctions.uiDefinitions(self)
        # AppFunctions.appDefinitions(self)
        # print(self.selected_crypto)

        # SET DATE
        self.today = datetime.today().strftime('%B %d, %Y')
        widgets.dateToday.setText(self.today)
        widgets.home_dateToday.setText(self.today)

        # DISPLAY
        widgets.stackedWidget.setCurrentWidget(widgets.homePage)

        # AppFunctions.df(self)
        self.default_values()
        self.signals()


    def default_values(self):
        # HOME
        widgets.btn_home.setStyleSheet(UIFunctions.selectCrypto(widgets.btn_home.styleSheet()))
        # widgets.btn_homePredClosing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_homePredClosing.styleSheet()))
        
        widgets.btn_homeHistoClosing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_homeHistoClosing.styleSheet()))
        widgets.btn_home1d.setStyleSheet(UIFunctions.selectHistoDay(widgets.btn_home1d.styleSheet()))

        # BTC, ETH, DOGE
        widgets.btn_0.setStyleSheet(UIFunctions.selectHistoDay(widgets.btn_0.styleSheet()))
        widgets.btn_histo_closing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_histo_closing.styleSheet()))
        # widgets.btn_predPriceClosing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_predPriceClosing.styleSheet()))

        # VALUES
        self.selected_crypto = 'btn_home'
        # self.home_pred_price = 'all'
        self.home_histo_price = 'Closing'
        # self.home_pred_days = int(widgets.home_daysValue.text())
        self.home_histo_days = 1

        # self.btc_pred_price = 'btc'
        self.btc_histo_price = 'Closing'
        self.btc_histo_days = 1

        # self.eth_pred_price = 'eth'
        self.eth_histo_price = 'Closing'
        self.eth_histo_days = 1

        # self.doge_pred_price = 'doge'
        self.doge_histo_price = 'Closing'
        self.doge_histo_days = 1
        
        self.get_df()
        # AppFunctions.pred_graph(self)

    def signals(self):
        # HOME PAGE
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_btc.clicked.connect(self.buttonClick)
        widgets.btn_eth.clicked.connect(self.buttonClick)
        widgets.btn_doge.clicked.connect(self.buttonClick)

        widgets.btn_homeHistoClosing.clicked.connect(self.get_price)
        widgets.btn_homeHistoHigh.clicked.connect(self.get_price)
        widgets.btn_homeHistoLow.clicked.connect(self.get_price)

        widgets.btn_home1d.clicked.connect(self.get_histo_day)
        widgets.btn_home3d.clicked.connect(self.get_histo_day)
        widgets.btn_home1w.clicked.connect(self.get_histo_day)
        widgets.btn_home1m.clicked.connect(self.get_histo_day)
        widgets.btn_home1y.clicked.connect(self.get_histo_day)

        # widgets.home_predSlider.valueChanged.connect(self.get_pred_day)

        # CRYPTO PAGE
        widgets.btn_histo_closing.clicked.connect(self.get_price)
        widgets.btn_histo_high.clicked.connect(self.get_price)
        widgets.btn_histo_low.clicked.connect(self.get_price)

        widgets.btn_0.clicked.connect(self.get_histo_day)
        widgets.btn_1.clicked.connect(self.get_histo_day)
        widgets.btn_2.clicked.connect(self.get_histo_day)
        widgets.btn_3.clicked.connect(self.get_histo_day)
        widgets.btn_4.clicked.connect(self.get_histo_day)

        # widgets.crypto_predSlider.valueChanged.connect(self.get_pred_day)


    def get_df(self):
        AppFunctions.dash_pred(self)
        AppFunctions.dash_histo(self)

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.homePage)
        else:

            # self.btc_pred_price = 'btc'
            self.btc_histo_price = 'Closing'
            self.btc_histo_days = 1

            # self.eth_pred_price = 'eth'
            self.eth_histo_price = 'Closing'
            self.eth_histo_days = 1

            # self.doge_pred_price = 'doge'
            self.doge_histo_price = 'Closing'
            self.doge_histo_days = 1

            UIFunctions.resetPriceStyle(self, 'btn_histo_closing')
            UIFunctions.resetHistoDayStyle(self, 'btn_0')

            widgets.btn_0.setStyleSheet(UIFunctions.selectHistoDay(widgets.btn_0.styleSheet()))
            widgets.btn_histo_closing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_histo_closing.styleSheet()))

            if btnName == "btn_btc":
                widgets.cryptocurrency.setText("BITCOIN (BTC)")

            if btnName == "btn_eth":
                widgets.cryptocurrency.setText("ETHEREUM (ETH)")

            if btnName == "btn_doge":
                widgets.cryptocurrency.setText("DOGECOIN (DOGE)")

            widgets.stackedWidget.setCurrentWidget(widgets.cryptoPage)

        UIFunctions.resetCryptoStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectCrypto(btn.styleSheet()))
        self.selected_crypto = btnName

        # self.default_values()
        # AppFunctions.get_df(self)
        self.get_df()


    def get_price(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # if btnName.startswith('btn_histo') or btnName.startswith('btn_home'):
        if btnName == 'btn_histo_closing' or btnName == 'btn_homeHistoClosing':
            if self.selected_crypto == 'btn_home':
                self.home_histo_price = 'Closing'
            if self.selected_crypto == 'btn_btc':
                self.btc_histo_price = 'Closing'
            if self.selected_crypto == 'btn_eth':
                self.eth_histo_price = 'Closing'
            if self.selected_crypto == 'btn_doge':
                self.doge_histo_price = 'Closing'
        
        if btnName == 'btn_histo_high' or btnName == 'btn_homeHistoHigh':
            if self.selected_crypto == 'btn_home':
                self.home_histo_price = 'High'
            if self.selected_crypto == 'btn_btc':
                self.btc_histo_price = 'High'
            if self.selected_crypto == 'btn_eth':
                self.eth_histo_price = 'High'
            if self.selected_crypto == 'btn_doge':
                self.doge_histo_price = 'High'

        if btnName == 'btn_histo_low' or btnName == 'btn_homeHistoLow':
            if self.selected_crypto == 'btn_home':
                self.home_histo_price = 'Low'
            if self.selected_crypto == 'btn_btc':
                self.btc_histo_price = 'Low'
            if self.selected_crypto == 'btn_eth':
                self.eth_histo_price = 'Low'
            if self.selected_crypto == 'btn_doge':
                self.doge_histo_price = 'Low'
            
        AppFunctions.dash_histo(self)

        UIFunctions.resetPriceStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectPrice(btn.styleSheet()))


    def get_histo_day(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'btn_0' or btnName == 'btn_home1d':
            if self.selected_crypto == 'btn_home':
                self.home_histo_days = 1
            if self.selected_crypto == 'btn_btc':
                self.btc_histo_days = 1
            if self.selected_crypto == 'btn_eth':
                self.eth_histo_days = 1
            if self.selected_crypto == 'btn_doge':
                self.doge_histo_days = 1

        if btnName == 'btn_1' or btnName == 'btn_home3d':
            if self.selected_crypto == 'btn_home':
                self.home_histo_days = 3
            if self.selected_crypto == 'btn_btc':
                self.btc_histo_days = 3
            if self.selected_crypto == 'btn_eth':
                self.eth_histo_days = 3
            if self.selected_crypto == 'btn_doge':
                self.doge_histo_days = 3
        
        if btnName == 'btn_2' or btnName == 'btn_home1w':
            if self.selected_crypto == 'btn_home':
                self.home_histo_days = 7
            if self.selected_crypto == 'btn_btc':
                self.btc_histo_days = 7
            if self.selected_crypto == 'btn_eth':
                self.eth_histo_days = 7
            if self.selected_crypto == 'btn_doge':
                self.doge_histo_days = 7

        if btnName == 'btn_3' or btnName == 'btn_home1m':
            if self.selected_crypto == 'btn_home':
                self.home_histo_days = 30
            if self.selected_crypto == 'btn_btc':
                self.btc_histo_days = 30
            if self.selected_crypto == 'btn_eth':
                self.eth_histo_days = 30
            if self.selected_crypto == 'btn_doge':
                self.doge_histo_days = 30

        if btnName == 'btn_4' or btnName == 'btn_home1y':
            if self.selected_crypto == 'btn_home':
                self.home_histo_days = 365
            if self.selected_crypto == 'btn_btc':
                self.btc_histo_days = 365
            if self.selected_crypto == 'btn_eth':
                self.eth_histo_days = 365
            if self.selected_crypto == 'btn_doge':
                self.doge_histo_days = 365

        UIFunctions.resetHistoDayStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectHistoDay(btn.styleSheet()))

        # self.access_db()
        AppFunctions.dash_histo(self)


    def catch_histo_data(self, histo_data):
        btc = list()
        eth = list()
        doge = list()

        if self.selected_crypto == 'btn_home':
            widgets.home_histoGraph.clear()
            for i, data in enumerate(histo_data):
                # print(i)
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
            widgets.crypto_histoGraph.clear()
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
            widgets.crypto_histoGraph.plot(x, y, pen=pen)

        self.h_worker.terminate()

    def plot(self, x, y, plot, pen):
        widgets.home_histoGraph.plot(x, y, name=plot, pen=pen)


    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    # window.show()
    sys.exit(app.exec())