import sys
import os
import time

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

        # SET DATE
        today = datetime.today().strftime('%B %d, %Y')
        widgets.dateToday.setText(today)
        widgets.home_dateToday.setText(today)

        # DISPLAY
        widgets.stackedWidget.setCurrentWidget(widgets.homePage)
        widgets.btn_home.setStyleSheet(UIFunctions.selectCrypto(widgets.btn_home.styleSheet()))

        # SIGNALS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_btc.clicked.connect(self.buttonClick)
        widgets.btn_eth.clicked.connect(self.buttonClick)
        widgets.btn_doge.clicked.connect(self.buttonClick)

        # self.show()

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