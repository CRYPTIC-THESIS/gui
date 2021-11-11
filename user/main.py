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
        self.default_values()
        print(self.selected_crypto)

        # SIGNALS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_btc.clicked.connect(self.buttonClick)
        widgets.btn_eth.clicked.connect(self.buttonClick)
        widgets.btn_doge.clicked.connect(self.buttonClick)

        # AppFunctions.df(self)

        # self.show()

    def testing(self):
        btnName = self.sender().objectName()
        print('hello ', btnName)

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.homePage)
        else:
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
        AppFunctions.get_df(self)

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
        self.home_pred_price = 'Price'
        self.home_histo_price = 'Closing'
        self.home_pred_days = int(widgets.home_daysValue.text())
        self.home_histo_days = 1
        
        AppFunctions.get_df(self)
        # AppFunctions.pred_graph(self)
    
    # def default_crypto_vals(self):

    def catch_histo_data(self, histo_data):
        widgets.home_histoGraph.clear()
        btc = list()
        eth = list()
        doge = list()

        if self.selected_crypto == 'btn_home':
            for i, data in enumerate(histo_data):
                print(i)
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

        self.worker.terminate()

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