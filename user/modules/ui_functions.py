from main import *

class UIFunctions(MainWindow):

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectCrypto(getStyle):
        select = getStyle + AppSettings.CRYPTO_SELECTED_STYLESHEET
        return select

    def selectPrice(getStyle):
        select = getStyle + AppSettings.PRICE_SELECTED_STYLESHEET
        return select

    def selectHistoDay(getStyle):
        select = getStyle + AppSettings.HISTODAY_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectCrypto(getStyle):
        deselect = getStyle.replace(AppSettings.CRYPTO_SELECTED_STYLESHEET, "")
        return deselect

    def deselectPrice(getStyle):
        deselect = getStyle.replace(AppSettings.PRICE_SELECTED_STYLESHEET, "")
        return deselect

    def deselectHistoDay(getStyle):
        deselect = getStyle.replace(AppSettings.HISTODAY_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardCrypto(self, widget):
        for w in self.ui.cryptoButtons.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectCrypto(w.styleSheet()))

    def selectStandardPrice(self, widget):
        if widget.startswith('btn_histo_'):
            for w in self.ui.histoPriceFrame.findChildren(QPushButton):
                if w.objectName() == widget:
                    w.setStyleSheet(UIFunctions.selectPrice(w.styleSheet()))

        if widget.startswith('btn_pred_'):
            for w in self.ui.predPriceButtons.findChildren(QPushButton):
                if w.objectName() == widget:
                    w.setStyleSheet(UIFunctions.selectPrice(w.styleSheet()))

    def selectStandardHistoday(self, widget):
        for w in self.ui.daysButtons.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectHistoDay(w.styleSheet()))

    # RESET SELECTION
    def resetCryptoStyle(self, widget):
        for w in self.ui.cryptoButtons.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectCrypto(w.styleSheet()))

    def resetPriceStyle(self, widget):
        if widget.startswith('btn_histo_'):
            for w in self.ui.histoPriceFrame.findChildren(QPushButton):
                if w.objectName() != widget:
                    w.setStyleSheet(UIFunctions.deselectPrice(w.styleSheet()))

        if widget.startswith('btn_pred_'):
            for w in self.ui.predPriceButtons.findChildren(QPushButton):
                if w.objectName() != widget:
                    w.setStyleSheet(UIFunctions.deselectPrice(w.styleSheet()))

    def resetHistoDayStyle(self, widget):
        for w in self.ui.daysButtons.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectHistoDay(w.styleSheet()))

    def uiDefinitions(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, Qt.WA_DeleteOnClose)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.topNav.mouseMoveEvent = moveWindow

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())


class AppSettings():
    # CRYPTO SELECTED STYLESHEET
    CRYPTO_SELECTED_STYLESHEET = """
    border-left: 5px solid #2AB7CA;
    """

    PRICE_SELECTED_STYLESHEET = """
    background: 'white';
	border-color: 'white';
    """

    CURRPRICE_SELECTED_STYLESHEET = """
    background: #21252B;
    border-radius: 10px;
    color: #2AB7CA;
    """

    HISTODAY_SELECTED_STYLESHEET = """
    background: #8C88BF;
    """