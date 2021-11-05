import os
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets


class DatabaseWorker(QtCore.QObject):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    @QtCore.pyqtSlot(object)
    def writeToDatabase(self, value):
        self.started.emit()
        for i in range(value):
            QtCore.QThread.msleep(10)
            print(i)
        self.finished.emit()


class Windows_GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(200, 200, 500, 500)
        button = QtWidgets.QPushButton("Open window")
        self.setCentralWidget(button)
        thread = QtCore.QThread(self)
        thread.start()
        self.m_database_worker = DatabaseWorker()
        self.m_database_worker.moveToThread(thread)
        self.m_database_worker.started.connect(self.start_animation)

        button.clicked.connect(self.on_clicked)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        value = 1000
        wrapper = partial(self.m_database_worker.writeToDatabase, value)
        QtCore.QTimer.singleShot(0, wrapper)

    @QtCore.pyqtSlot()
    def start_animation(self):

        gif_path = os.path.join("system", "icons", "loading.gif")
        self.loading_window = QtWidgets.QDialog()
        self.loading_window.setWindowFlags(QtCore.Qt.SplashScreen)
        self.loading_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        movie = QtGui.QMovie(gif_path, cacheMode=QtGui.QMovie.CacheAll)

        movie_label = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        movie_label.setStyleSheet("border: 0px;")
        movie_label.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        movie_label.setFixedSize(500, 500)
        movie_label.setMovie(movie)

        vbox = QtWidgets.QVBoxLayout(self.loading_window)
        vbox.addWidget(movie_label)
        self.m_database_worker.finished.connect(self.loading_window.close)
        self.loading_window.show()
        movie.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = Windows_GUI()
    w.show()
    sys.exit(app.exec_())