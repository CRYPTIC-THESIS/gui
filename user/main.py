# ------------------------------------------------------------------------------------------- #
#    CRYPTIC: AN IMPROVED CNN-LSTM CRYPTOCURRENCY PRICE FORECASTING USING INTERNET TRENDS
# 
# Authors:
# Arconado, Kristine N.             Dalay, Jeremy Tristen A.
# Berse, Nikko R.                   Faustino, Kyle C.
# 
# BSCS 4-2 AY 2021-2022
# ------------------------------------------------------------------------------------------- #

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

        print('Connecting to database...')
        self.access_db()
    
    def access_db(self):
        self.worker = AccessDatabase()
        self.worker.start()

        self.worker2 = GetDecisionSupport()
        self.worker2.start()
        self.worker2.decision_complete.connect(self.worker2.quit)

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
            self.window.activateWindow()
            self.close()

    def catch_db_data(self):
        print('Successfully imported db data.')
        self.show()


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

        # SET DATE
        self.today = datetime.today().strftime('%B %d, %Y')
        widgets.dateToday.setText(self.today)
        widgets.home_dateToday.setText(self.today)

        # DISPLAY
        widgets.stackedWidget.setCurrentWidget(widgets.homePage)
        widgets.help.hide()

        # QTableWidget Stretch
        widgets.home_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widgets.cryptoPredTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # AppFunctions.df(self)
        self.default_values()
        self.signals()


    def default_values(self):
        # HOME
        widgets.btn_home.setStyleSheet(UIFunctions.selectCrypto(widgets.btn_home.styleSheet()))
        
        widgets.btn_homeHistoClosing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_homeHistoClosing.styleSheet()))
        widgets.btn_home1d.setStyleSheet(UIFunctions.selectHistoDay(widgets.btn_home1d.styleSheet()))

        # BTC, ETH, DOGE
        widgets.btn_0.setStyleSheet(UIFunctions.selectHistoDay(widgets.btn_0.styleSheet()))
        widgets.btn_histo_closing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_histo_closing.styleSheet()))

        # VALUES
        self.lblHidden = None
        self.ctr = None

        df = pd.read_csv('csv/decsupport.csv')
        self.labels = list()
        for i in range(1, 4):
            self.labels.append(str(df.iloc[0][i]))
        ## print('self.labels: ', self.labels)
        
        self.selected_crypto = 'btn_home'
        self.home_histo_price = 'Close'
        self.home_histo_days = '24h'

        # self.btc_pred_price = 'btc'
        self.btc_histo_price = 'Close'
        self.btc_histo_days = '24h'

        # self.eth_pred_price = 'eth'
        self.eth_histo_price = 'Close'
        self.eth_histo_days = '24h'

        # self.doge_pred_price = 'doge'
        self.doge_histo_price = 'Close'
        self.doge_histo_days = '24h'

        # SUGGESTION
        self.suggestion()
        
        self.get_pred_day()
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

        widgets.home_predSlider.valueChanged.connect(self.get_pred_day)

        # CRYPTO PAGE
        widgets.btn_histo_closing.clicked.connect(self.get_price)
        widgets.btn_histo_high.clicked.connect(self.get_price)
        widgets.btn_histo_low.clicked.connect(self.get_price)

        widgets.btn_0.clicked.connect(self.get_histo_day)
        widgets.btn_1.clicked.connect(self.get_histo_day)
        widgets.btn_2.clicked.connect(self.get_histo_day)
        widgets.btn_3.clicked.connect(self.get_histo_day)
        widgets.btn_4.clicked.connect(self.get_histo_day)

        widgets.crypto_predSlider.valueChanged.connect(self.get_pred_day)


    def get_df(self):
        AppFunctions.display_prices(self)
        # AppFunctions.dash_pred(self)
        AppFunctions.dash_histo(self)


    # SUGGESTION
    def suggestion(self):
        self.timer = QTimer()
        self.lblcolors = ['#F9AA4B;', '#2082FA;', '#8C88BF;']
        
        if self.selected_crypto == 'btn_home':
            self.timer.stop()
            self.lblHidden = True
            self.ctr = 0
            self.timer.timeout.connect(self.flashLbl_all)
            self.timer.start(830)

        else:
            self.timer.stop()

            # if self.ctr != 3:
            #     widgets.home_dateToday.styleSheet().replace('color: '+self.lblcolors[self.ctr], "")

            if self.selected_crypto == 'btn_btc':
                self.ctr = 0
            
            if self.selected_crypto == 'btn_eth':
                self.ctr = 1
            
            if self.selected_crypto == 'btn_doge':
                self.ctr = 2
                
            widgets.cryptocurrency.setText(self.labels[self.ctr])
            widgets.cryptocurrency.setStyleSheet(widgets.cryptocurrency.styleSheet() + 'color: '+self.lblcolors[self.ctr])
            widgets.cryptocurrency.show()

            self.lblHidden = True
            self.timer.timeout.connect(self.flashLbl)
            self.timer.start(800)

    def flashLbl_all(self):
        if self.ctr == 3:
            self.ctr = 0
        widgets.home_dateToday.setText(self.labels[self.ctr])
        widgets.home_dateToday.setStyleSheet(widgets.home_dateToday.styleSheet() + 'color: '+self.lblcolors[self.ctr])
        
        if self.lblHidden == False:
            widgets.home_dateToday.hide()
            self.lblHidden = True
        else:
            widgets.home_dateToday.show()
            self.lblHidden = False
            widgets.home_dateToday.styleSheet().replace('color: '+self.lblcolors[self.ctr], "")
            self.ctr = self.ctr + 1

    def flashLbl(self):
        if self.lblHidden == False:
            widgets.cryptocurrency.setStyleSheet(widgets.cryptocurrency.styleSheet() + 'color: #2AB7CA;')
            self.lblHidden = True
        else:
            widgets.cryptocurrency.styleSheet().replace('color: #2AB7CA;', '')
            widgets.cryptocurrency.setStyleSheet(widgets.cryptocurrency.styleSheet() + 'color: '+self.lblcolors[self.ctr])
            self.lblHidden = False


    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.homePage)
            widgets.crypto_histoGraph.clear()
            widgets.crypto_predGraph.clear()
        else:

            widgets.home_histoGraph.clear()
            widgets.home_predGraph.clear()

            # self.btc_pred_price = 'btc'
            self.btc_histo_price = 'Close'
            self.btc_histo_days = '24h'

            # self.eth_pred_price = 'eth'
            self.eth_histo_price = 'Close'
            self.eth_histo_days = '24h'

            # self.doge_pred_price = 'doge'
            self.doge_histo_price = 'Close'
            self.doge_histo_days = '24h'

            UIFunctions.resetPriceStyle(self, 'btn_histo_closing')
            UIFunctions.resetHistoDayStyle(self, 'btn_0')

            widgets.btn_0.setStyleSheet(UIFunctions.selectHistoDay(widgets.btn_0.styleSheet()))
            widgets.btn_histo_closing.setStyleSheet(UIFunctions.selectPrice(widgets.btn_histo_closing.styleSheet()))

            # widgets.btn_histo_high.setEnabled(False)
            # widgets.btn_histo_low.setEnabled(False)

            if btnName == "btn_btc":
                widgets.cryptocurrency.setText("BITCOIN (BTC)")
                widgets.histoCurrPriceLabel.setText(widgets.home_btc_currPriceLabel.text())
                widgets.histoOpenPriceLabel.setText(widgets.home_btc_openPriceLabel.text())
                widgets.histoHighPriceLabel.setText(widgets.home_btc_highPriceLabel.text())
                widgets.histoLowPriceLabel.setText(widgets.home_btc_lowPriceLabel.text())

            if btnName == "btn_eth":
                widgets.cryptocurrency.setText("ETHEREUM (ETH)")
                widgets.histoCurrPriceLabel.setText(widgets.home_eth_currPriceLabel.text())
                widgets.histoOpenPriceLabel.setText(widgets.home_eth_openPriceLabel.text())
                widgets.histoHighPriceLabel.setText(widgets.home_eth_highPriceLabel.text())
                widgets.histoLowPriceLabel.setText(widgets.home_eth_lowPriceLabel.text())

            if btnName == "btn_doge":
                widgets.cryptocurrency.setText("DOGECOIN (DOGE)")
                widgets.histoCurrPriceLabel.setText(widgets.home_doge_currPriceLabel.text())
                widgets.histoOpenPriceLabel.setText(widgets.home_doge_openPriceLabel.text())
                widgets.histoHighPriceLabel.setText(widgets.home_doge_highPriceLabel.text())
                widgets.histoLowPriceLabel.setText(widgets.home_doge_lowPriceLabel.text())

            widgets.stackedWidget.setCurrentWidget(widgets.cryptoPage)

        UIFunctions.resetCryptoStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectCrypto(btn.styleSheet()))
        self.selected_crypto = btnName
        self.get_pred_day()

        # SUGGESTION
        self.suggestion()

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
                self.home_histo_price = 'Close'
            if self.selected_crypto == 'btn_btc':
                self.btc_histo_price = 'Close'
            if self.selected_crypto == 'btn_eth':
                self.eth_histo_price = 'Close'
            if self.selected_crypto == 'btn_doge':
                self.doge_histo_price = 'Close'
        
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
                self.home_histo_days = '24h'
                widgets.btn_homeHistoHigh.setEnabled(True)
                widgets.btn_homeHistoLow.setEnabled(True)
            else:
                if self.selected_crypto == 'btn_btc':
                    self.btc_histo_days = '24h'
                if self.selected_crypto == 'btn_eth':
                    self.eth_histo_days = '24h'
                if self.selected_crypto == 'btn_doge':
                    self.doge_histo_days = '24h'
                widgets.btn_histo_high.setEnabled(True)
                widgets.btn_histo_low.setEnabled(True)
            
        if btnName == 'btn_1' or btnName == 'btn_home3d':
            if self.selected_crypto == 'btn_home':
                self.home_histo_days = 3
                widgets.btn_homeHistoHigh.setEnabled(True)
                widgets.btn_homeHistoLow.setEnabled(True)
            else:
                if self.selected_crypto == 'btn_btc':
                    self.btc_histo_days = 3
                if self.selected_crypto == 'btn_eth':
                    self.eth_histo_days = 3
                if self.selected_crypto == 'btn_doge':
                    self.doge_histo_days = 3
                widgets.btn_histo_high.setEnabled(True)
                widgets.btn_histo_low.setEnabled(True)

        
        if btnName == 'btn_2' or btnName == 'btn_home1w':
            if self.selected_crypto == 'btn_home':
                self.home_histo_days = 7
                widgets.btn_homeHistoHigh.setEnabled(True)
                widgets.btn_homeHistoLow.setEnabled(True)
            else:
                if self.selected_crypto == 'btn_btc':
                    self.btc_histo_days = 7
                if self.selected_crypto == 'btn_eth':
                    self.eth_histo_days = 7
                if self.selected_crypto == 'btn_doge':
                    self.doge_histo_days = 7
                widgets.btn_histo_high.setEnabled(True)
                widgets.btn_histo_low.setEnabled(True)


        if btnName == 'btn_3' or btnName == 'btn_home1m':
            if self.selected_crypto == 'btn_home':
                self.home_histo_days = 30
                widgets.btn_homeHistoHigh.setEnabled(True)
                widgets.btn_homeHistoLow.setEnabled(True)
            else:
                if self.selected_crypto == 'btn_btc':
                    self.btc_histo_days = 30
                if self.selected_crypto == 'btn_eth':
                    self.eth_histo_days = 30
                if self.selected_crypto == 'btn_doge':
                    self.doge_histo_days = 30
                widgets.btn_histo_high.setEnabled(True)
                widgets.btn_histo_low.setEnabled(True)


        if btnName == 'btn_4' or btnName == 'btn_home1y':
            if self.selected_crypto == 'btn_home':
                self.home_histo_days = '1y'
                widgets.btn_homeHistoHigh.setEnabled(True)
                widgets.btn_homeHistoLow.setEnabled(True)
            else:
                if self.selected_crypto == 'btn_btc':
                    self.btc_histo_days = '1y'
                if self.selected_crypto == 'btn_eth':
                    self.eth_histo_days = '1y'
                if self.selected_crypto == 'btn_doge':
                    self.doge_histo_days = '1y'
                widgets.btn_histo_high.setEnabled(True)
                widgets.btn_histo_low.setEnabled(True)


        UIFunctions.resetHistoDayStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectHistoDay(btn.styleSheet()))

        # self.access_db()
        AppFunctions.dash_histo(self)

    
    def get_pred_day(self):
        if self.selected_crypto == 'btn_home':
            widgets.home_daysValue.setNum
            text = widgets.home_daysValue.text()
        else:
            widgets.crypto_daysValue.setNum
            text = widgets.crypto_daysValue.text()
        self.selected_predicted_day = int(text)

        AppFunctions.dash_pred(self)


    def display_this(self, dct):
        b = dct.get('btc')
        e = dct.get('eth')
        d = dct.get('doge')
        # self.prices.terminate()

        widgets.home_btc_currPriceLabel.setText('$'+str(b[0]))
        widgets.home_eth_currPriceLabel.setText('$'+str(e[0]))
        widgets.home_doge_currPriceLabel.setText('$'+str(d[0]))

        widgets.home_btc_openPriceLabel.setText('$'+str(b[1]))
        widgets.home_eth_openPriceLabel.setText('$'+str(e[1]))
        widgets.home_doge_openPriceLabel.setText('$'+str(d[1]))

        widgets.home_btc_highPriceLabel.setText('$'+str(b[2]))
        widgets.home_eth_highPriceLabel.setText('$'+str(e[2]))
        widgets.home_doge_highPriceLabel.setText('$'+str(d[2]))

        widgets.home_btc_lowPriceLabel.setText('$'+str(b[3]))
        widgets.home_eth_lowPriceLabel.setText('$'+str(e[3]))
        widgets.home_doge_lowPriceLabel.setText('$'+str(d[3]))


    def catch_histo_data(self, histo_data):
        self.h_thread.quit()
        self.h_thread.wait()
        
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

        # self.h_worker.terminate()

    def catch_pred_data(self, pred_data):
        # print('pred_data: \n', pred_data)
        widgets.home_predGraph.clear()
        widgets.home_tableWidget.clear()
        widgets.crypto_predGraph.clear()
        widgets.cryptoPredTable.clear()

        btc = list()
        eth = list()
        doge = list()

        if self.selected_crypto == 'btn_home':
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

            # x = datetime.fromtimestamp(int(x)).strftime('%Y-%m-%d')
            dates = list()
            for date in x:
                dates.append(datetime.fromtimestamp(int(date)).strftime('%Y-%m-%d'))
            tbl = pd.concat([pd.Series(dates,name='Date'),
                             pd.Series(y,name='BITCOIN'), 
                             pd.Series(y2,name='ETHEREUM'), 
                             pd.Series(y3,name='DOGECOIN')], axis=1)
            
            widgets.home_tableWidget.setColumnCount(len(tbl.columns))
            widgets.home_tableWidget.setRowCount(len(tbl.index))

            for i in range(len(tbl.index)):
                for j in range(len(tbl.columns)):
                    item = QTableWidgetItem(str(tbl.iat[i, j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    widgets.home_tableWidget.setItem(i, j, item)

            widgets.home_tableWidget.setHorizontalHeaderLabels(tbl.columns)
            widgets.home_tableWidget.resizeColumnsToContents()
            widgets.home_tableWidget.resizeRowsToContents()
            widgets.home_tableWidget.show()

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
            widgets.crypto_predGraph.plot(x, y, pen=pen)

            widgets.cryptoPredTable.setColumnCount(len(columns))
            widgets.cryptoPredTable.setRowCount(len(ind))

            for i in range(len(ind)):
                for j in range(len(columns)):
                    item = QTableWidgetItem(str(new_df.iat[i, j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    widgets.cryptoPredTable.setItem(i, j, item)

            widgets.cryptoPredTable.setHorizontalHeaderLabels(new_df.columns)
            widgets.cryptoPredTable.resizeColumnsToContents()
            widgets.cryptoPredTable.resizeRowsToContents()
            widgets.cryptoPredTable.show()

        # self.pg_worker.terminate()
        # del self.pg_worker
    
    def plot(self, x, y, plot, pen):
        widgets.home_histoGraph.plot(x, y, name=plot, pen=pen)

    def pplot(self, x, y, plot, pen):
        widgets.home_predGraph.plot(x, y, name=plot, pen=pen)


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