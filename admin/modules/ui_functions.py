from main import *

# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions(MainWindow):
    
    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + MainSettings.MENU_SELECTED_STYLESHEET
        return select

    def selectCrypto(getStyle):
        select = getStyle + MainSettings.CRYPTO_SELECTED_STYLESHEET
        return select

    def selectCard(getStyle):
        select = getStyle + MainSettings.CURRPRICE_SELECTED_STYLESHEET
        return select

    def selectPrice(getStyle):
        select = getStyle + MainSettings.PRICE_SELECTED_STYLESHEET
        return select

    def selectHistoDay(getStyle):
        select = getStyle + MainSettings.HISTODAY_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(MainSettings.MENU_SELECTED_STYLESHEET, "")
        return deselect
    
    def deselectCrypto(getStyle):
        deselect = getStyle.replace(MainSettings.CRYPTO_SELECTED_STYLESHEET, "")
        return deselect

    def deselectCard(getStyle):
        deselect = getStyle.replace(MainSettings.CURRPRICE_SELECTED_STYLESHEET, "")
        return deselect

    def deselectPrice(getStyle):
        deselect = getStyle.replace(MainSettings.PRICE_SELECTED_STYLESHEET, "")
        return deselect

    def deselectHistoDay(getStyle):
        deselect = getStyle.replace(MainSettings.HISTODAY_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    def selectStandardCrypto(self, widget):
        for w in self.ui.cryptoButtons.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectCrypto(w.styleSheet()))

    def selectStandardCard(self, card):
        for w in self.ui.currPriceCards.findChildren(QFrame):
            if w.objectName() == card:
                w.setStyleSheet(UIFunctions.selectCard(w.styleSheet()))

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
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    def resetCryptoStyle(self, widget):
        for w in self.ui.cryptoButtons.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectCrypto(w.styleSheet()))

    def resetCardStyle(self, card):
        for w in self.ui.currPriceCards.findChildren(QFrame):
            if w.objectName() != card:
                w.setStyleSheet(UIFunctions.deselectCard(w.styleSheet()))

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

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):

        if MainSettings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.contentTopBg.mouseMoveEvent = moveWindow

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

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


    def ui_logindefinitions(self):
        
        if LoginSettings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    p = event.globalPosition()
                    globalPos = p.toPoint()
                    self.dragPos = globalPos
                    # self.dragPos = event.globalPos()
                    event.accept()
            self.ui.login.mouseMoveEvent = moveWindow

        # CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame.setGraphicsEffect(self.shadow)

    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS
