import sys
import os
import time

# import pyrebase
# from modules import *
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
            self.close()

    def catch_db_data(self):
        print('Successfully imported db data.')
        self.show()
        # print(db_data)
        # self.close()

class AccessDatabase(QThread):
    update_progress = Signal(int)
    import_data_complete = Signal()
    def run(self):
        
        db_btc = get_data_table('Bitcoin_Data')
        db_eth = get_data_table('Ethereum_Data')
        db_doge = get_data_table('Dogecoin_Data')

        lst = [db_btc, db_eth, db_doge]
        fn = ['csv/db_btc.csv', 'csv/db_eth.csv', 'csv/db_doge.csv']

        today = datetime.today().strftime('%Y-%m-%d')
        today = pd.to_datetime(today)
        past = today - timedelta(days=365)

        for i, df in enumerate(lst):
            df['date'] = pd.to_datetime(df['date'])
            df = df.loc[(df['date'] >= past) & (df['date'] <= today)]
            df.to_csv(fn[i])

        print(today)
        print(past)

        self.import_data_complete.emit()

        for x in range(13, 101):
            time.sleep(0.07)
            self.update_progress.emit(x)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    # window.show()
    sys.exit(app.exec())