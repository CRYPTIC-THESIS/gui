# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainzCpiiG.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from pyqtgraph import PlotWidget, DateAxisItem, mkPen

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 740)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#bgApp {\n"
"	background: #21252B;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#content {\n"
"	background: #282C34;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#content QPushButton {\n"
"	color: #259CA5;\n"
"	font: 13px \"Segoe UI\"; font-weight: bold;\n"
"	/* border: 2px solid rgb(52, 59, 72); */\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#content QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"	color: #DDDDDD;\n"
"}\n"
"#content QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	color: #DDDDDD;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
""
                        "#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	background: none;\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid #259CA5;\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72); \n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    backgrou"
                        "nd-color: #259CA5; /*rgb(189, 147, 249)*/\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #2AB7CA; /*rgb(195, 155, 255)*/\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #2AB7CA; /*rgb(255, 121, 198)*/\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color:#259CA5;\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #29B3A7;\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #29B3A7;\n"
"}\n"
"\n"
"/* //////////////////////////////////////////////////////////////////////////"
                        "///////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(51, 56, 64);/*rgb(44, 49, 58);*/\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {background-color: transparent; }\n"
"\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: #2AB7CA;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: transparent;\n"
"	/* max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);*/\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"/*QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}*/\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    /*border: 1px solid rgb(33, 37, 43);*/\n"
"	background-colo"
                        "r: transparent;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"/* QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}*/\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #2AB7CA;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #"
                        "2AB7CA;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #259CA5;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizo"
                        "ntal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: #259CA5;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" Q"
                        "ScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.centralwidget)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideMenu = QFrame(self.bgApp)
        self.sideMenu.setObjectName(u"sideMenu")
        self.sideMenu.setMinimumSize(QSize(90, 0))
        self.sideMenu.setMaximumSize(QSize(100, 16777215))
        self.sideMenu.setStyleSheet(u"")
        self.sideMenu.setFrameShape(QFrame.NoFrame)
        self.sideMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sideMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.sideMenu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 25))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 12pt \"Segoe UI Semibold\";\n"
"color: rgba(221, 221, 221, 0.35);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_16, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.sideMenu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 10)
        self.cryptoButtons = QFrame(self.frame_7)
        self.cryptoButtons.setObjectName(u"cryptoButtons")
        self.cryptoButtons.setMaximumSize(QSize(16777215, 16777215))
        self.cryptoButtons.setStyleSheet(u"QPushButton {	\n"
"    background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	border-radius: 0px;\n"
"	width: 49px;\n"
"	height: 49px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	/*border-left: 25px solid qlineargradient(spread:pad, x1:0.034, y1:1, x2:0.216, y2:1, stop:0.399 #2AB7CA, stop:0.4 rgba(85, 170, 255, 0));*/\n"
"	border-left: 4px solid rgba(42, 183, 202, 0.4);\n"
"}\n")
        self.cryptoButtons.setFrameShape(QFrame.NoFrame)
        self.cryptoButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.cryptoButtons)
        self.verticalLayout_8.setSpacing(17)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.cryptoButtons)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 0))
        self.btn_home.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/images/images/btnHome.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(45, 45))

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_btc = QPushButton(self.cryptoButtons)
        self.btn_btc.setObjectName(u"btn_btc")
        self.btn_btc.setMinimumSize(QSize(0, 0))
        self.btn_btc.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/images/btnBitcoin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_btc.setIcon(icon1)
        self.btn_btc.setIconSize(QSize(45, 45))

        self.verticalLayout_8.addWidget(self.btn_btc)

        self.btn_eth = QPushButton(self.cryptoButtons)
        self.btn_eth.setObjectName(u"btn_eth")
        self.btn_eth.setMinimumSize(QSize(0, 0))
        self.btn_eth.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/images/btnEthereum.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_eth.setIcon(icon2)
        self.btn_eth.setIconSize(QSize(45, 45))

        self.verticalLayout_8.addWidget(self.btn_eth)

        self.btn_doge = QPushButton(self.cryptoButtons)
        self.btn_doge.setObjectName(u"btn_doge")
        self.btn_doge.setMinimumSize(QSize(0, 0))
        self.btn_doge.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/images/btnDogecoin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_doge.setIcon(icon3)
        self.btn_doge.setIconSize(QSize(45, 45))

        self.verticalLayout_8.addWidget(self.btn_doge)


        self.verticalLayout_7.addWidget(self.cryptoButtons)


        self.verticalLayout_3.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.sideMenu)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 20)
        self.help = QPushButton(self.frame_6)
        self.help.setObjectName(u"help")
        self.help.setMinimumSize(QSize(35, 35))
        self.help.setMaximumSize(QSize(35, 35))
        self.help.setToolTipDuration(-1)
        self.help.setStyleSheet(u"/* Top Buttons */\n"
"QPushButton { background-color: rgb(52, 59, 72); border: none;  border-radius: 5px; }\n"
"QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help.setIcon(icon4)
        self.help.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.help)


        self.verticalLayout_3.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.sideMenu)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topNav = QFrame(self.contentBox)
        self.topNav.setObjectName(u"topNav")
        self.topNav.setMinimumSize(QSize(0, 25))
        self.topNav.setMaximumSize(QSize(16777215, 25))
        self.topNav.setFrameShape(QFrame.NoFrame)
        self.topNav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.topNav)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.topNav)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_17)

        self.frame_31 = QFrame(self.topNav)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid #259CA5;\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.dateToday = QLabel(self.frame_31)
        self.dateToday.setObjectName(u"dateToday")
        self.dateToday.setMinimumSize(QSize(238, 0))
        self.dateToday.setStyleSheet(u"font: 10pt \"Segoe UI Semibold\";")
        self.dateToday.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.dateToday)

        self.rightButtons = QFrame(self.frame_31)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setStyleSheet(u"border: none;")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon5)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setStyleSheet(u"border-top-right-radius: 10px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon6)
        self.closeAppBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_15.addWidget(self.closeAppBtn)


        self.horizontalLayout_13.addWidget(self.rightButtons)


        self.horizontalLayout_11.addWidget(self.frame_31, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.topNav)

        self.content = QFrame(self.contentBox)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent; ")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.gridLayout = QGridLayout(self.homePage)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.home_predictionFrame = QFrame(self.homePage)
        self.home_predictionFrame.setObjectName(u"home_predictionFrame")
        self.home_predictionFrame.setMinimumSize(QSize(0, 0))
        self.home_predictionFrame.setMaximumSize(QSize(16777215, 16777215))
        self.home_predictionFrame.setStyleSheet(u"background: #2C313A;\n"
"border-radius: 10px;")
        self.home_predictionFrame.setFrameShape(QFrame.NoFrame)
        self.home_predictionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.home_predictionFrame)
        self.verticalLayout_38.setSpacing(5)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(15, 13, 15, 13)
        self.frame_50 = QFrame(self.home_predictionFrame)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(10, 0, 10, 0)
        self.frame_52 = QFrame(self.frame_50)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_52)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_52)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_35.addWidget(self.label_23, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_31.addWidget(self.frame_52)

        self.home_predPriceButtons = QFrame(self.frame_50)
        self.home_predPriceButtons.setObjectName(u"home_predPriceButtons")
        self.home_predPriceButtons.setStyleSheet(u"* {\n"
"	border-radius: 12px; \n"
"	border-color: #2C313A;\n"
"	font: 13px \"Segoe UI\"; font-weight: bold;\n"
"}\n"
"\n"
"*:hover {\n"
"	color: #259CA5;\n"
"	border-color: 'white';\n"
"}\n"
"\n"
"*:activate, *:focus {\n"
"	color: #259CA5;\n"
"	background: 'white';\n"
"	border-color: 'white';\n"
"}")
        self.home_predPriceButtons.setFrameShape(QFrame.NoFrame)
        self.home_predPriceButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.home_predPriceButtons)
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        # self.btn_homePredClosing = QPushButton(self.home_predPriceButtons)
        # self.btn_homePredClosing.setObjectName(u"btn_homePredClosing")
        # self.btn_homePredClosing.setMinimumSize(QSize(86, 25))

        # self.horizontalLayout_32.addWidget(self.btn_homePredClosing)

        # self.btn_homePredHigh = QPushButton(self.home_predPriceButtons)
        # self.btn_homePredHigh.setObjectName(u"btn_homePredHigh")
        # self.btn_homePredHigh.setMinimumSize(QSize(65, 25))

        # self.horizontalLayout_32.addWidget(self.btn_homePredHigh)

        # self.btn_homePredLow = QPushButton(self.home_predPriceButtons)
        # self.btn_homePredLow.setObjectName(u"btn_homePredLow")
        # self.btn_homePredLow.setMinimumSize(QSize(65, 25))

        # self.horizontalLayout_32.addWidget(self.btn_homePredLow)


        self.horizontalLayout_31.addWidget(self.home_predPriceButtons, 0, Qt.AlignRight)


        self.verticalLayout_38.addWidget(self.frame_50)

        self.home_predGraphFrame = QFrame(self.home_predictionFrame)
        self.home_predGraphFrame.setObjectName(u"home_predGraphFrame")
        self.home_predGraphFrame.setMinimumSize(QSize(0, 0))
        self.home_predGraphFrame.setMaximumSize(QSize(573, 290))
        self.home_predGraphFrame.setStyleSheet(u"border-radius: 0; background: transparent;")
        self.home_predGraphFrame.setFrameShape(QFrame.NoFrame)
        self.home_predGraphFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.home_predGraphFrame)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.home_predGraph = PlotWidget(self.home_predGraphFrame, axisItems={'bottom': DateAxisItem(orientation='bottom')})
        self.home_predGraph.setObjectName(u"home_predGraph")
        self.home_predGraph.setFrameShape(QFrame.NoFrame)
        brush = QBrush(QColor(44, 49, 58, 1))
        brush.setStyle(Qt.NoBrush)
        self.home_predGraph.setBackground('#2C313A')

        self.verticalLayout_36.addWidget(self.home_predGraph)


        self.verticalLayout_38.addWidget(self.home_predGraphFrame)

        self.frame_53 = QFrame(self.home_predictionFrame)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(0, 22))
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(10, 0, 10, 0)
        self.home_sliderFrame = QFrame(self.frame_53)
        self.home_sliderFrame.setObjectName(u"home_sliderFrame")
        self.home_sliderFrame.setFrameShape(QFrame.NoFrame)
        self.home_sliderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.home_sliderFrame)
        self.horizontalLayout_34.setSpacing(10)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.home_sliderFrame)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_34.addWidget(self.label_24, 0, Qt.AlignVCenter)

        self.home_predSlider = QSlider(self.home_sliderFrame)
        self.home_predSlider.setObjectName(u"home_predSlider")
        self.home_predSlider.setMinimumSize(QSize(170, 0))
        self.home_predSlider.setMinimum(2)
        self.home_predSlider.setMaximum(14)
        self.home_predSlider.setSliderPosition(7)
        self.home_predSlider.setOrientation(Qt.Horizontal)
        self.home_predSlider.setTickPosition(QSlider.NoTicks)
        self.home_predSlider.setTickInterval(0)

        self.horizontalLayout_34.addWidget(self.home_predSlider)

        self.home_daysValue = QLabel(self.home_sliderFrame)
        self.home_daysValue.setObjectName(u"home_daysValue")

        self.horizontalLayout_34.addWidget(self.home_daysValue, 0, Qt.AlignVCenter)


        self.horizontalLayout_33.addWidget(self.home_sliderFrame, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.home_predRangeLabelFrame = QFrame(self.frame_53)
        self.home_predRangeLabelFrame.setObjectName(u"home_predRangeLabelFrame")
        self.home_predRangeLabelFrame.setFrameShape(QFrame.NoFrame)
        self.home_predRangeLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.home_predRangeLabelFrame)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.home_predRangeLabel = QLabel(self.home_predRangeLabelFrame)
        self.home_predRangeLabel.setObjectName(u"home_predRangeLabel")
        self.home_predRangeLabel.setMinimumSize(QSize(236, 22))
        self.home_predRangeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_37.addWidget(self.home_predRangeLabel, 0, Qt.AlignRight)


        self.horizontalLayout_33.addWidget(self.home_predRangeLabelFrame)


        self.verticalLayout_38.addWidget(self.frame_53)


        self.gridLayout.addWidget(self.home_predictionFrame, 0, 0, 1, 1)

        self.home_predTableFrame = QFrame(self.homePage)
        self.home_predTableFrame.setObjectName(u"home_predTableFrame")
        self.home_predTableFrame.setMaximumSize(QSize(603, 270))
        self.home_predTableFrame.setStyleSheet(u"background: #21252B;\n"
"border-radius: 10px;")
        self.home_predTableFrame.setFrameShape(QFrame.NoFrame)
        self.home_predTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.home_predTableFrame)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.home_tableWidget = QTableWidget(self.home_predTableFrame)
        self.home_tableWidget.setObjectName(u"home_tableWidget")
        self.home_tableWidget.setFrameShape(QFrame.NoFrame)
        self.home_tableWidget.verticalHeader().setHighlightSections(False)

        self.verticalLayout_20.addWidget(self.home_tableWidget)


        self.gridLayout.addWidget(self.home_predTableFrame, 1, 0, 1, 1)

        self.home_histoFrame = QFrame(self.homePage)
        self.home_histoFrame.setObjectName(u"home_histoFrame")
        self.home_histoFrame.setMaximumSize(QSize(540, 16777215))
        self.home_histoFrame.setStyleSheet(u"")
        self.home_histoFrame.setFrameShape(QFrame.NoFrame)
        self.home_histoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.home_histoFrame)
        self.verticalLayout_39.setSpacing(20)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.home_histoFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 300))
        self.frame.setStyleSheet(u"background: transparent;\n"
"border-radius: 10px;\n"
"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.home_dateToday = QLabel(self.frame_2)
        self.home_dateToday.setObjectName(u"home_dateToday")
        self.home_dateToday.setMinimumSize(QSize(275, 41))
        self.home_dateToday.setStyleSheet(u"font: 30px \"Segoe UI\"; font-weight: bold;\n"
"color: white;\n"
"background: #21252B;\n"
"color: #2AB7CA;")
        self.home_dateToday.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.home_dateToday)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background: #21252B;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 10, 10, 10)
        self.frame_56 = QFrame(self.frame_3)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMaximumSize(QSize(85, 16777215))
        self.frame_56.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_56)
        self.verticalLayout_40.setSpacing(8)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(15, 10, 0, 10)
        self.label_25 = QLabel(self.frame_56)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 37))
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_40.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_56)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_40.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_56)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"border-top: 2px solid #41464E; border-radius: 0px;")
        self.label_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_40.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_56)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"border-top: 2px solid #41464E; border-radius: 0px;")
        self.label_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_40.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_56)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"border-top: 2px solid #41464E; border-radius: 0px;")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_40.addWidget(self.label_29)


        self.horizontalLayout_16.addWidget(self.frame_56)

        self.home_btcCard = QFrame(self.frame_3)
        self.home_btcCard.setObjectName(u"home_btcCard")
        self.home_btcCard.setStyleSheet(u"background: #41464E;")
        self.home_btcCard.setFrameShape(QFrame.NoFrame)
        self.home_btcCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.home_btcCard)
        self.verticalLayout_41.setSpacing(10)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(10, 10, 10, 10)
        self.btcLogoTitle = QFrame(self.home_btcCard)
        self.btcLogoTitle.setObjectName(u"btcLogoTitle")
        self.btcLogoTitle.setFrameShape(QFrame.NoFrame)
        self.btcLogoTitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.btcLogoTitle)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_65 = QFrame(self.btcLogoTitle)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.NoFrame)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frame_65)
        self.verticalLayout_116.setSpacing(0)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_65)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_116.addWidget(self.label_35)

        self.label_30 = QLabel(self.frame_65)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.verticalLayout_116.addWidget(self.label_30)


        self.horizontalLayout_36.addWidget(self.frame_65, 0, Qt.AlignVCenter)

        self.frame_66 = QFrame(self.btcLogoTitle)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setStyleSheet(u"background-image: url(:/images/images/images/btc-logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right top;")
        self.frame_66.setFrameShape(QFrame.NoFrame)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_36.addWidget(self.frame_66)


        self.verticalLayout_41.addWidget(self.btcLogoTitle)

        self.frame_63 = QFrame(self.home_btcCard)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.NoFrame)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_63)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.home_btc_currPriceLabel = QLabel(self.frame_63)
        self.home_btc_currPriceLabel.setObjectName(u"home_btc_currPriceLabel")
        self.home_btc_currPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_42.addWidget(self.home_btc_currPriceLabel)


        self.verticalLayout_41.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.home_btcCard)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.NoFrame)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_64)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.home_btc_openPriceLabel = QLabel(self.frame_64)
        self.home_btc_openPriceLabel.setObjectName(u"home_btc_openPriceLabel")
        self.home_btc_openPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_43.addWidget(self.home_btc_openPriceLabel)


        self.verticalLayout_41.addWidget(self.frame_64)

        self.frame_5 = QFrame(self.home_btcCard)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_5)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.home_btc_highPriceLabel = QLabel(self.frame_5)
        self.home_btc_highPriceLabel.setObjectName(u"home_btc_highPriceLabel")
        self.home_btc_highPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_44.addWidget(self.home_btc_highPriceLabel)


        self.verticalLayout_41.addWidget(self.frame_5)

        self.frame_62 = QFrame(self.home_btcCard)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.NoFrame)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_62)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.home_btc_lowPriceLabel = QLabel(self.frame_62)
        self.home_btc_lowPriceLabel.setObjectName(u"home_btc_lowPriceLabel")
        self.home_btc_lowPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_45.addWidget(self.home_btc_lowPriceLabel)


        self.verticalLayout_41.addWidget(self.frame_62)


        self.horizontalLayout_16.addWidget(self.home_btcCard)

        self.home_ethCard = QFrame(self.frame_3)
        self.home_ethCard.setObjectName(u"home_ethCard")
        self.home_ethCard.setStyleSheet(u"background: #41464E;")
        self.home_ethCard.setFrameShape(QFrame.NoFrame)
        self.home_ethCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.home_ethCard)
        self.verticalLayout_50.setSpacing(10)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(10, 10, 10, 10)
        self.ethLogoTitle = QFrame(self.home_ethCard)
        self.ethLogoTitle.setObjectName(u"ethLogoTitle")
        self.ethLogoTitle.setFrameShape(QFrame.NoFrame)
        self.ethLogoTitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.ethLogoTitle)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.ethLogoTitle)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.NoFrame)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_70)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_70)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_117.addWidget(self.label_43)

        self.label_44 = QLabel(self.frame_70)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.verticalLayout_117.addWidget(self.label_44)


        self.horizontalLayout_37.addWidget(self.frame_70, 0, Qt.AlignVCenter)

        self.frame_71 = QFrame(self.ethLogoTitle)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setStyleSheet(u"background-image: url(:/images/images/images/eth-logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right top;")
        self.frame_71.setFrameShape(QFrame.NoFrame)
        self.frame_71.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_37.addWidget(self.frame_71)


        self.verticalLayout_50.addWidget(self.ethLogoTitle)

        self.frame_68 = QFrame(self.home_ethCard)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.NoFrame)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_68)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.home_eth_currPriceLabel = QLabel(self.frame_68)
        self.home_eth_currPriceLabel.setObjectName(u"home_eth_currPriceLabel")
        self.home_eth_currPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_47.addWidget(self.home_eth_currPriceLabel)


        self.verticalLayout_50.addWidget(self.frame_68)

        self.frame_72 = QFrame(self.home_ethCard)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.NoFrame)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_72)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.home_eth_openPriceLabel = QLabel(self.frame_72)
        self.home_eth_openPriceLabel.setObjectName(u"home_eth_openPriceLabel")
        self.home_eth_openPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_48.addWidget(self.home_eth_openPriceLabel)


        self.verticalLayout_50.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.home_ethCard)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.NoFrame)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_73)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.home_eth_highPriceLabel = QLabel(self.frame_73)
        self.home_eth_highPriceLabel.setObjectName(u"home_eth_highPriceLabel")
        self.home_eth_highPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_49.addWidget(self.home_eth_highPriceLabel)


        self.verticalLayout_50.addWidget(self.frame_73)

        self.frame_67 = QFrame(self.home_ethCard)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.NoFrame)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_67)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.home_eth_lowPriceLabel = QLabel(self.frame_67)
        self.home_eth_lowPriceLabel.setObjectName(u"home_eth_lowPriceLabel")
        self.home_eth_lowPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_46.addWidget(self.home_eth_lowPriceLabel)


        self.verticalLayout_50.addWidget(self.frame_67)


        self.horizontalLayout_16.addWidget(self.home_ethCard)

        self.home_dogeCard = QFrame(self.frame_3)
        self.home_dogeCard.setObjectName(u"home_dogeCard")
        self.home_dogeCard.setStyleSheet(u"background: #41464E;")
        self.home_dogeCard.setFrameShape(QFrame.NoFrame)
        self.home_dogeCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.home_dogeCard)
        self.verticalLayout_55.setSpacing(10)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(10, 10, 10, 10)
        self.dogeLogoTitle = QFrame(self.home_dogeCard)
        self.dogeLogoTitle.setObjectName(u"dogeLogoTitle")
        self.dogeLogoTitle.setFrameShape(QFrame.NoFrame)
        self.dogeLogoTitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.dogeLogoTitle)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_79 = QFrame(self.dogeLogoTitle)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.NoFrame)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.frame_79)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.frame_79)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_118.addWidget(self.label_51)

        self.label_52 = QLabel(self.frame_79)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.verticalLayout_118.addWidget(self.label_52)


        self.horizontalLayout_38.addWidget(self.frame_79, 0, Qt.AlignVCenter)

        self.frame_80 = QFrame(self.dogeLogoTitle)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setStyleSheet(u"background-image: url(:/images/images/images/doge-logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right top;")
        self.frame_80.setFrameShape(QFrame.NoFrame)
        self.frame_80.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_38.addWidget(self.frame_80)


        self.verticalLayout_55.addWidget(self.dogeLogoTitle)

        self.frame_76 = QFrame(self.home_dogeCard)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.NoFrame)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_76)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.home_doge_currPriceLabel = QLabel(self.frame_76)
        self.home_doge_currPriceLabel.setObjectName(u"home_doge_currPriceLabel")
        self.home_doge_currPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_53.addWidget(self.home_doge_currPriceLabel)


        self.verticalLayout_55.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.home_dogeCard)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.NoFrame)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_77)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.home_doge_openPriceLabel = QLabel(self.frame_77)
        self.home_doge_openPriceLabel.setObjectName(u"home_doge_openPriceLabel")
        self.home_doge_openPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_54.addWidget(self.home_doge_openPriceLabel)


        self.verticalLayout_55.addWidget(self.frame_77)

        self.frame_75 = QFrame(self.home_dogeCard)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.NoFrame)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_75)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.home_doge_highPriceLabel = QLabel(self.frame_75)
        self.home_doge_highPriceLabel.setObjectName(u"home_doge_highPriceLabel")
        self.home_doge_highPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_52.addWidget(self.home_doge_highPriceLabel)


        self.verticalLayout_55.addWidget(self.frame_75)

        self.frame_74 = QFrame(self.home_dogeCard)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.NoFrame)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_74)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.home_doge_lowPriceLabel = QLabel(self.frame_74)
        self.home_doge_lowPriceLabel.setObjectName(u"home_doge_lowPriceLabel")
        self.home_doge_lowPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_51.addWidget(self.home_doge_lowPriceLabel)


        self.verticalLayout_55.addWidget(self.frame_74)


        self.horizontalLayout_16.addWidget(self.home_dogeCard)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_39.addWidget(self.frame)

        self.homeHistoFrame = QFrame(self.home_histoFrame)
        self.homeHistoFrame.setObjectName(u"homeHistoFrame")
        self.homeHistoFrame.setStyleSheet(u"background: #2C313A;\n"
"border-radius: 10px;")
        self.homeHistoFrame.setFrameShape(QFrame.NoFrame)
        self.homeHistoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.homeHistoFrame)
        self.verticalLayout_58.setSpacing(5)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(15, 13, 15, 13)
        self.frame_81 = QFrame(self.homeHistoFrame)
        self.frame_81.setObjectName(u"frame_81")
        self.horizontalLayout_40 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(10, 0, 10, 0)
        self.frame_82 = QFrame(self.frame_81)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.NoFrame)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_82)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.frame_82)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_56.addWidget(self.label_53)


        self.horizontalLayout_40.addWidget(self.frame_82, 0, Qt.AlignLeft)

        self.home_histoPriceButtons = QFrame(self.frame_81)
        self.home_histoPriceButtons.setObjectName(u"home_histoPriceButtons")
        self.home_histoPriceButtons.setStyleSheet(u"* {\n"
"	border-radius: 12px; \n"
"	border-color: #2C313A;\n"
"	color: #8C88BF;\n"
"	font: 13px \"Segoe UI\"; font-weight: bold;\n"
"}\n"
"\n"
"*:hover {\n"
"	border-color: 'white';\n"
"}\n"
"\n"
"*:focus {\n"
"	background: 'white';\n"
"	border-color: 'white';\n"
"}")
        self.home_histoPriceButtons.setFrameShape(QFrame.NoFrame)
        self.home_histoPriceButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.home_histoPriceButtons)
        self.horizontalLayout_41.setSpacing(10)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.btn_homeHistoClosing = QPushButton(self.home_histoPriceButtons)
        self.btn_homeHistoClosing.setObjectName(u"btn_homeHistoClosing")
        self.btn_homeHistoClosing.setMinimumSize(QSize(86, 25))
        font = QFont()
        font.setFamily(u"Segoe UI BOLD")
        font.setBold(False)
        font.setItalic(False)
        # font.setWeight(50)
        self.btn_homeHistoClosing.setFont(font)
        self.btn_homeHistoClosing.setStyleSheet(u"")

        self.horizontalLayout_41.addWidget(self.btn_homeHistoClosing)

        self.btn_homeHistoHigh = QPushButton(self.home_histoPriceButtons)
        self.btn_homeHistoHigh.setObjectName(u"btn_homeHistoHigh")
        self.btn_homeHistoHigh.setMinimumSize(QSize(65, 25))
        self.btn_homeHistoHigh.setStyleSheet(u"")

        self.horizontalLayout_41.addWidget(self.btn_homeHistoHigh)

        self.btn_homeHistoLow = QPushButton(self.home_histoPriceButtons)
        self.btn_homeHistoLow.setObjectName(u"btn_homeHistoLow")
        self.btn_homeHistoLow.setMinimumSize(QSize(65, 25))
        self.btn_homeHistoLow.setStyleSheet(u"")

        self.horizontalLayout_41.addWidget(self.btn_homeHistoLow)


        self.horizontalLayout_40.addWidget(self.home_histoPriceButtons, 0, Qt.AlignRight)


        self.verticalLayout_58.addWidget(self.frame_81)

        self.home_histoGraphFrame = QFrame(self.homeHistoFrame)
        self.home_histoGraphFrame.setObjectName(u"home_histoGraphFrame")
        self.home_histoGraphFrame.setMinimumSize(QSize(510, 200))
        self.home_histoGraphFrame.setMaximumSize(QSize(16777215, 16777215))
        self.home_histoGraphFrame.setFrameShape(QFrame.NoFrame)
        self.home_histoGraphFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.home_histoGraphFrame)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.home_histoGraph = PlotWidget(self.home_histoGraphFrame, axisItems={'bottom': DateAxisItem(orientation='bottom')})
        self.home_histoGraph.setObjectName(u"home_histoGraph")
        self.home_histoGraph.setFrameShape(QFrame.NoFrame)
        self.home_histoGraph.setBackground('#2C313A')
        self.home_histoGraph.addLegend()

        self.verticalLayout_57.addWidget(self.home_histoGraph)


        self.verticalLayout_58.addWidget(self.home_histoGraphFrame)

        self.home_histoDayButtons = QFrame(self.homeHistoFrame)
        self.home_histoDayButtons.setObjectName(u"home_histoDayButtons")
        self.home_histoDayButtons.setStyleSheet(u"* {\n"
"	border-radius: 0;\n"
"	border: 0;\n"
"	color: 'white';\n"
"	font: 13px \"Segoe UI\"; font-weight: bold;\n"
"	width: 32px;\n"
"	height: 25px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #41464E;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: #8C88BF;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	background: #8C88BF;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid #259CA5;\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"	font: 10pt \"Segoe UI\";\n"
"}")
        self.home_histoDayButtons.setFrameShape(QFrame.NoFrame)
        self.home_histoDayButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.home_histoDayButtons)
        self.horizontalLayout_39.setSpacing(10)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(10, 0, 0, 0)
        # self.btn_home1d = QPushButton(self.home_histoDayButtons)
        # self.btn_home1d.setObjectName(u"btn_home1d")
        # self.btn_home1d.setStyleSheet(u"")

        # self.horizontalLayout_39.addWidget(self.btn_home1d)

        self.btn_home3d = QPushButton(self.home_histoDayButtons)
        self.btn_home3d.setObjectName(u"btn_home3d")
        self.btn_home3d.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.btn_home3d)

        self.btn_home1w = QPushButton(self.home_histoDayButtons)
        self.btn_home1w.setObjectName(u"btn_home1w")
        self.btn_home1w.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.btn_home1w)

        self.btn_home1m = QPushButton(self.home_histoDayButtons)
        self.btn_home1m.setObjectName(u"btn_home1m")
        self.btn_home1m.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.btn_home1m)

        self.btn_home1y = QPushButton(self.home_histoDayButtons)
        self.btn_home1y.setObjectName(u"btn_home1y")
        self.btn_home1y.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.btn_home1y)


        self.verticalLayout_58.addWidget(self.home_histoDayButtons, 0, Qt.AlignLeft)


        self.verticalLayout_39.addWidget(self.homeHistoFrame)


        self.gridLayout.addWidget(self.home_histoFrame, 0, 1, 2, 1)

        self.stackedWidget.addWidget(self.homePage)
        self.cryptoPage = QWidget()
        self.cryptoPage.setObjectName(u"cryptoPage")
        self.horizontalLayout_2 = QHBoxLayout(self.cryptoPage)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cryptoHistoDiv = QFrame(self.cryptoPage)
        self.cryptoHistoDiv.setObjectName(u"cryptoHistoDiv")
        self.cryptoHistoDiv.setMaximumSize(QSize(450, 16777215))
        self.cryptoHistoDiv.setStyleSheet(u"background: #252930;\n"
"border-top-left-radius: 10px;")
        self.cryptoHistoDiv.setFrameShape(QFrame.NoFrame)
        self.cryptoHistoDiv.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.cryptoHistoDiv)
        self.verticalLayout_10.setSpacing(25)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 15, 20, 8)
        self.frame_11 = QFrame(self.cryptoHistoDiv)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 33))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(15, 0, 15, 0)
        self.frame_29 = QFrame(self.frame_11)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_29)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.cryptocurrency = QLabel(self.frame_29)
        self.cryptocurrency.setObjectName(u"cryptocurrency")
        self.cryptocurrency.setMinimumSize(QSize(368, 33))
        self.cryptocurrency.setStyleSheet(u"font: 30px \"Segoe UI\"; font-weight: bold;\n"
"color: white;")
        self.cryptocurrency.setFrameShadow(QFrame.Plain)
        self.cryptocurrency.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.cryptocurrency, 0, Qt.AlignVCenter)


        self.horizontalLayout_9.addWidget(self.frame_29, 0, Qt.AlignVCenter)


        self.verticalLayout_10.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.cryptoHistoDiv)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 350))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 20))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_14)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_30)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_30)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_18.addWidget(self.label_15)


        self.horizontalLayout_10.addWidget(self.frame_30, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.frame_14)

        self.histoGraphFrame = QFrame(self.frame_12)
        self.histoGraphFrame.setObjectName(u"histoGraphFrame")
        self.histoGraphFrame.setMaximumSize(QSize(16777215, 16777215))
        self.histoGraphFrame.setFrameShape(QFrame.NoFrame)
        self.histoGraphFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.histoGraphFrame)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.crypto_histoPriceButtons = QFrame(self.histoGraphFrame)
        self.crypto_histoPriceButtons.setObjectName(u"crypto_histoPriceButtons")
        self.crypto_histoPriceButtons.setStyleSheet(u"* {\n"
"	border-radius: 12px; \n"
"	border-color: #2C313A;\n"
"	color: #8C88BF;\n"
"	font: 13px \"Segoe UI\"; font-weight: bold;\n"
"}\n"
"\n"
"*:hover {\n"
"	border-color: 'white';\n"
"}\n"
"\n"
"*:focus {\n"
"	background: 'white';\n"
"	border-color: 'white';\n"
"}")
        self.crypto_histoPriceButtons.setFrameShape(QFrame.NoFrame)
        self.crypto_histoPriceButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.crypto_histoPriceButtons)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btn_histo_closing = QPushButton(self.crypto_histoPriceButtons)
        self.btn_histo_closing.setObjectName(u"btn_histo_closing")
        self.btn_histo_closing.setMinimumSize(QSize(86, 25))
        self.btn_histo_closing.setFont(font)
        self.btn_histo_closing.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.btn_histo_closing)

        self.btn_histo_high = QPushButton(self.crypto_histoPriceButtons)
        self.btn_histo_high.setObjectName(u"btn_histo_high")
        self.btn_histo_high.setMinimumSize(QSize(65, 25))
        self.btn_histo_high.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.btn_histo_high)

        self.btn_histo_low = QPushButton(self.crypto_histoPriceButtons)
        self.btn_histo_low.setObjectName(u"btn_histo_low")
        self.btn_histo_low.setMinimumSize(QSize(65, 25))
        self.btn_histo_low.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.btn_histo_low)


        self.verticalLayout_15.addWidget(self.crypto_histoPriceButtons, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.crypto_histoGraphFrame = QFrame(self.histoGraphFrame)
        self.crypto_histoGraphFrame.setObjectName(u"crypto_histoGraphFrame")
        self.crypto_histoGraphFrame.setMinimumSize(QSize(0, 255))
        self.crypto_histoGraphFrame.setStyleSheet(u"border: 3px solid #FFFFFF;\n"
"border-radius: 0px;")
        self.crypto_histoGraphFrame.setFrameShape(QFrame.NoFrame)
        self.crypto_histoGraphFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.crypto_histoGraphFrame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.crypto_histoGraph = PlotWidget(self.crypto_histoGraphFrame, axisItems={'bottom': DateAxisItem(orientation='bottom')})
        self.crypto_histoGraph.setObjectName(u"crypto_histoGraph")
        self.crypto_histoGraph.setStyleSheet(u"border: 0px;")
        self.crypto_histoGraph.setFrameShape(QFrame.NoFrame)
        self.crypto_histoGraph.setBackgroundBrush(brush)

        self.verticalLayout_17.addWidget(self.crypto_histoGraph)


        self.verticalLayout_15.addWidget(self.crypto_histoGraphFrame)

        self.crypto_daysButtons = QFrame(self.histoGraphFrame)
        self.crypto_daysButtons.setObjectName(u"crypto_daysButtons")
        self.crypto_daysButtons.setStyleSheet(u"* {\n"
"	border-radius: 0;\n"
"	border: 0;\n"
"	color: 'white';\n"
"	font: 13px \"Segoe UI\"; font-weight: bold;\n"
"	width: 32px;\n"
"	height: 25px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #41464E;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: #8C88BF;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	background: #8C88BF;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid #259CA5;\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"	font: 10pt \"Segoe UI\";\n"
"}")
        self.crypto_daysButtons.setFrameShape(QFrame.NoFrame)
        self.crypto_daysButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.crypto_daysButtons)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        # self.btn_0 = QPushButton(self.crypto_daysButtons)
        # self.btn_0.setObjectName(u"btn_0")
        # self.btn_0.setStyleSheet(u"")

        # self.horizontalLayout_14.addWidget(self.btn_0)

        self.btn_1 = QPushButton(self.crypto_daysButtons)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.btn_1)

        self.btn_2 = QPushButton(self.crypto_daysButtons)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.btn_2)

        self.btn_3 = QPushButton(self.crypto_daysButtons)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.btn_3)

        self.btn_4 = QPushButton(self.crypto_daysButtons)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.btn_4)


        self.verticalLayout_15.addWidget(self.crypto_daysButtons, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.histoGraphFrame)


        self.verticalLayout_10.addWidget(self.frame_12)

        self.realtimePriceLabels = QFrame(self.cryptoHistoDiv)
        self.realtimePriceLabels.setObjectName(u"realtimePriceLabels")
        self.realtimePriceLabels.setStyleSheet(u"")
        self.realtimePriceLabels.setFrameShape(QFrame.NoFrame)
        self.realtimePriceLabels.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.realtimePriceLabels)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, 10, 20, 0)
        self.histoCurrPriceFrame = QFrame(self.realtimePriceLabels)
        self.histoCurrPriceFrame.setObjectName(u"histoCurrPriceFrame")
        self.histoCurrPriceFrame.setFrameShape(QFrame.NoFrame)
        self.histoCurrPriceFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.histoCurrPriceFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.histoCurrPriceFrame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.histoCurrPriceLabel = QLabel(self.histoCurrPriceFrame)
        self.histoCurrPriceLabel.setObjectName(u"histoCurrPriceLabel")
        self.histoCurrPriceLabel.setStyleSheet(u"color: #B3AFEB;\n"
"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.histoCurrPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.histoCurrPriceLabel)


        self.verticalLayout_12.addWidget(self.histoCurrPriceFrame)

        self.histoOpenPriceFrame = QFrame(self.realtimePriceLabels)
        self.histoOpenPriceFrame.setObjectName(u"histoOpenPriceFrame")
        self.histoOpenPriceFrame.setFrameShape(QFrame.NoFrame)
        self.histoOpenPriceFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.histoOpenPriceFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.histoOpenPriceFrame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.histoOpenPriceLabel = QLabel(self.histoOpenPriceFrame)
        self.histoOpenPriceLabel.setObjectName(u"histoOpenPriceLabel")
        self.histoOpenPriceLabel.setStyleSheet(u"color: #B3AFEB;\n"
"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.histoOpenPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.histoOpenPriceLabel)


        self.verticalLayout_12.addWidget(self.histoOpenPriceFrame)

        self.histoHighPriceFrame = QFrame(self.realtimePriceLabels)
        self.histoHighPriceFrame.setObjectName(u"histoHighPriceFrame")
        self.histoHighPriceFrame.setFrameShape(QFrame.NoFrame)
        self.histoHighPriceFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.histoHighPriceFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.histoHighPriceFrame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.histoHighPriceLabel = QLabel(self.histoHighPriceFrame)
        self.histoHighPriceLabel.setObjectName(u"histoHighPriceLabel")
        self.histoHighPriceLabel.setStyleSheet(u"color: #B3AFEB;\n"
"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.histoHighPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.histoHighPriceLabel)


        self.verticalLayout_12.addWidget(self.histoHighPriceFrame)

        self.histoLowPriceFrame = QFrame(self.realtimePriceLabels)
        self.histoLowPriceFrame.setObjectName(u"histoLowPriceFrame")
        self.histoLowPriceFrame.setFrameShape(QFrame.NoFrame)
        self.histoLowPriceFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.histoLowPriceFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.histoLowPriceFrame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.histoLowPriceLabel = QLabel(self.histoLowPriceFrame)
        self.histoLowPriceLabel.setObjectName(u"histoLowPriceLabel")
        self.histoLowPriceLabel.setStyleSheet(u"color: #B3AFEB;\n"
"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.histoLowPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.histoLowPriceLabel)


        self.verticalLayout_12.addWidget(self.histoLowPriceFrame)

        self.histoMarketFrame = QFrame(self.realtimePriceLabels)
        self.histoMarketFrame.setObjectName(u"histoMarketFrame")
        self.histoMarketFrame.setFrameShape(QFrame.NoFrame)
        self.histoMarketFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.histoMarketFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.marketcap = QLabel(self.histoMarketFrame)
        self.marketcap.setObjectName(u"marketcap")
        self.marketcap.setMinimumSize(QSize(68, 0))

        self.horizontalLayout_7.addWidget(self.marketcap, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.histoMarketLabel = QLabel(self.histoMarketFrame)
        self.histoMarketLabel.setObjectName(u"histoMarketLabel")
        self.histoMarketLabel.setStyleSheet(u"color: #B3AFEB;\n"
"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.histoMarketLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.histoMarketLabel)


        self.verticalLayout_12.addWidget(self.histoMarketFrame)

        self.histoVolumeFrame = QFrame(self.realtimePriceLabels)
        self.histoVolumeFrame.setObjectName(u"histoVolumeFrame")
        self.histoVolumeFrame.setFrameShape(QFrame.NoFrame)
        self.histoVolumeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.histoVolumeFrame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.volume = QLabel(self.histoVolumeFrame)
        self.volume.setObjectName(u"volume")
        self.volume.setMinimumSize(QSize(43, 0))

        self.horizontalLayout_8.addWidget(self.volume, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.histoVolumeLabel = QLabel(self.histoVolumeFrame)
        self.histoVolumeLabel.setObjectName(u"histoVolumeLabel")
        self.histoVolumeLabel.setStyleSheet(u"color: #B3AFEB;\n"
"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.histoVolumeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.histoVolumeLabel)


        self.verticalLayout_12.addWidget(self.histoVolumeFrame)


        self.verticalLayout_10.addWidget(self.realtimePriceLabels, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.cryptoHistoDiv)

        self.cryptoPredDiv = QFrame(self.cryptoPage)
        self.cryptoPredDiv.setObjectName(u"cryptoPredDiv")
        self.cryptoPredDiv.setMinimumSize(QSize(0, 0))
        self.cryptoPredDiv.setFrameShape(QFrame.NoFrame)
        self.cryptoPredDiv.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.cryptoPredDiv)
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 20, 20, 20)
        self.cryptoPredFrame = QFrame(self.cryptoPredDiv)
        self.cryptoPredFrame.setObjectName(u"cryptoPredFrame")
        self.cryptoPredFrame.setMaximumSize(QSize(16777215, 16777215))
        self.cryptoPredFrame.setFrameShape(QFrame.NoFrame)
        self.cryptoPredFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.cryptoPredFrame)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.cryptoPredFrame)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 0, 10, 0)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_27)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_27)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_23.addWidget(self.label_13, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_19.addWidget(self.frame_27)

        self.crypto_predPriceButtons = QFrame(self.frame_26)
        self.crypto_predPriceButtons.setObjectName(u"crypto_predPriceButtons")
        self.crypto_predPriceButtons.setStyleSheet(u"* {\n"
"	border-radius: 12px; \n"
"	border-color: #2C313A;\n"
"	font: 13px \"Segoe UI\"; font-weight: bold;\n"
"}\n"
"\n"
"*:hover {\n"
"	color: #259CA5;\n"
"	border-color: 'white';\n"
"}\n"
"\n"
"*:activate, *:focus {\n"
"	color: #259CA5;\n"
"	background: 'white';\n"
"	border-color: 'white';\n"
"}")
        self.crypto_predPriceButtons.setFrameShape(QFrame.NoFrame)
        self.crypto_predPriceButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.crypto_predPriceButtons)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        # self.btn_predPriceClosing = QPushButton(self.crypto_predPriceButtons)
        # self.btn_predPriceClosing.setObjectName(u"btn_predPriceClosing")
        # self.btn_predPriceClosing.setMinimumSize(QSize(86, 25))

        # self.horizontalLayout_21.addWidget(self.btn_predPriceClosing)

        # self.btn_predPriceHigh = QPushButton(self.crypto_predPriceButtons)
        # self.btn_predPriceHigh.setObjectName(u"btn_predPriceHigh")
        # self.btn_predPriceHigh.setMinimumSize(QSize(65, 25))

        # self.horizontalLayout_21.addWidget(self.btn_predPriceHigh)

        # self.btn_predPriceLow = QPushButton(self.crypto_predPriceButtons)
        # self.btn_predPriceLow.setObjectName(u"btn_predPriceLow")
        # self.btn_predPriceLow.setMinimumSize(QSize(65, 25))

        # self.horizontalLayout_21.addWidget(self.btn_predPriceLow)


        self.horizontalLayout_19.addWidget(self.crypto_predPriceButtons, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_26)

        self.crypto_predGraphFrame = QFrame(self.cryptoPredFrame)
        self.crypto_predGraphFrame.setObjectName(u"crypto_predGraphFrame")
        self.crypto_predGraphFrame.setMinimumSize(QSize(0, 0))
        self.crypto_predGraphFrame.setStyleSheet(u"border-radius: 0; background: transparent;")
        self.crypto_predGraphFrame.setFrameShape(QFrame.NoFrame)
        self.crypto_predGraphFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.crypto_predGraphFrame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.crypto_predGraph = PlotWidget(self.crypto_predGraphFrame, axisItems={'bottom': DateAxisItem(orientation='bottom')})
        self.crypto_predGraph.setObjectName(u"crypto_predGraph")
        self.crypto_predGraph.setFrameShape(QFrame.NoFrame)
        self.crypto_predGraph.setBackgroundBrush(brush)

        self.verticalLayout_22.addWidget(self.crypto_predGraph)


        self.verticalLayout_14.addWidget(self.crypto_predGraphFrame)

        self.frame_28 = QFrame(self.cryptoPredFrame)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 10))
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 0, 10, 0)
        self.sliderFrame = QFrame(self.frame_28)
        self.sliderFrame.setObjectName(u"sliderFrame")
        self.sliderFrame.setFrameShape(QFrame.NoFrame)
        self.sliderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.sliderFrame)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.sliderFrame)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_22.addWidget(self.label_14, 0, Qt.AlignVCenter)

        self.crypto_predSlider = QSlider(self.sliderFrame)
        self.crypto_predSlider.setObjectName(u"crypto_predSlider")
        self.crypto_predSlider.setMinimumSize(QSize(220, 0))
        self.crypto_predSlider.setMinimum(2)
        self.crypto_predSlider.setMaximum(14)
        self.crypto_predSlider.setSliderPosition(7)
        self.crypto_predSlider.setOrientation(Qt.Horizontal)
        self.crypto_predSlider.setTickPosition(QSlider.NoTicks)
        self.crypto_predSlider.setTickInterval(0)

        self.horizontalLayout_22.addWidget(self.crypto_predSlider)

        self.crypto_daysValue = QLabel(self.sliderFrame)
        self.crypto_daysValue.setObjectName(u"crypto_daysValue")

        self.horizontalLayout_22.addWidget(self.crypto_daysValue, 0, Qt.AlignVCenter)


        self.horizontalLayout_20.addWidget(self.sliderFrame, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.crypto_predRangeLabelFrame = QFrame(self.frame_28)
        self.crypto_predRangeLabelFrame.setObjectName(u"crypto_predRangeLabelFrame")
        self.crypto_predRangeLabelFrame.setFrameShape(QFrame.NoFrame)
        self.crypto_predRangeLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.crypto_predRangeLabelFrame)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.crypto_predRangeLabel = QLabel(self.crypto_predRangeLabelFrame)
        self.crypto_predRangeLabel.setObjectName(u"crypto_predRangeLabel")
        self.crypto_predRangeLabel.setMinimumSize(QSize(236, 22))
        self.crypto_predRangeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.crypto_predRangeLabel, 0, Qt.AlignRight)


        self.horizontalLayout_20.addWidget(self.crypto_predRangeLabelFrame)


        self.verticalLayout_14.addWidget(self.frame_28)


        self.verticalLayout_13.addWidget(self.cryptoPredFrame)

        self.cryptoPredTableFrame = QFrame(self.cryptoPredDiv)
        self.cryptoPredTableFrame.setObjectName(u"cryptoPredTableFrame")
        self.cryptoPredTableFrame.setMaximumSize(QSize(16777215, 225))
        self.cryptoPredTableFrame.setStyleSheet(u"background: #21252B;\n"
"border-radius: 10px;")
        self.cryptoPredTableFrame.setFrameShape(QFrame.NoFrame)
        self.cryptoPredTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.cryptoPredTableFrame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.cryptoPredTable = QTableWidget(self.cryptoPredTableFrame)
        self.cryptoPredTable.setObjectName(u"cryptoPredTable")
        self.cryptoPredTable.setFrameShape(QFrame.NoFrame)
        self.cryptoPredTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.cryptoPredTable.verticalHeader().setHighlightSections(False)

        self.verticalLayout_21.addWidget(self.cryptoPredTable)


        self.verticalLayout_13.addWidget(self.cryptoPredTableFrame)


        self.horizontalLayout_2.addWidget(self.cryptoPredDiv)

        self.stackedWidget.addWidget(self.cryptoPage)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.content)


        self.horizontalLayout.addWidget(self.contentBox)


        self.verticalLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.crypto_predSlider.valueChanged.connect(self.crypto_daysValue.setNum)
        self.home_predSlider.valueChanged.connect(self.home_daysValue.setNum)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip(QCoreApplication.translate("MainWindow", u"Welcome to CRYPTIC!", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"CRYPTIC", None))
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home.setText("")
#if QT_CONFIG(tooltip)
        self.btn_btc.setToolTip(QCoreApplication.translate("MainWindow", u"Bitcoin", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btc.setText("")
#if QT_CONFIG(tooltip)
        self.btn_eth.setToolTip(QCoreApplication.translate("MainWindow", u"Ethereum", None))
#endif // QT_CONFIG(tooltip)
        self.btn_eth.setText("")
#if QT_CONFIG(tooltip)
        self.btn_doge.setToolTip(QCoreApplication.translate("MainWindow", u"Dogecoin", None))
#endif // QT_CONFIG(tooltip)
        self.btn_doge.setText("")
#if QT_CONFIG(tooltip)
        self.help.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.help.setText("")
#if QT_CONFIG(tooltip)
        self.dateToday.setToolTip(QCoreApplication.translate("MainWindow", u"Today", None))
#endif // QT_CONFIG(tooltip)
        self.dateToday.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"PREDICTED PRICES", None))
        # self.btn_homePredClosing.setText(QCoreApplication.translate("MainWindow", u"CLOSING", None))
        # self.btn_homePredHigh.setText(QCoreApplication.translate("MainWindow", u"HIGH", None))
        # self.btn_homePredLow.setText(QCoreApplication.translate("MainWindow", u"LOW", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"DAYS:", None))
        self.home_daysValue.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(tooltip)
        self.home_predRangeLabel.setToolTip(QCoreApplication.translate("MainWindow", u"Prediction Range", None))
#endif // QT_CONFIG(tooltip)
        self.home_predRangeLabel.setText("")
        self.home_dateToday.setText("")
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<strong>CURRENT</strong><br>Price", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<strong>OPEN</strong><br>Price", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"24h<br><strong>HIGH</strong>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"24h<br><strong>LOW</strong>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"BTC", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Bitcoin", None))
        self.home_btc_currPriceLabel.setText("")
        self.home_btc_openPriceLabel.setText("")
        self.home_btc_highPriceLabel.setText("")
        self.home_btc_lowPriceLabel.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"ETH", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Ethereum", None))
        self.home_eth_currPriceLabel.setText("")
        self.home_eth_openPriceLabel.setText("")
        self.home_eth_highPriceLabel.setText("")
        self.home_eth_lowPriceLabel.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"DOGE", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Dogecoin", None))
        self.home_doge_currPriceLabel.setText("")
        self.home_doge_openPriceLabel.setText("")
        self.home_doge_highPriceLabel.setText("")
        self.home_doge_lowPriceLabel.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"HISTORY", None))
        self.btn_homeHistoClosing.setText(QCoreApplication.translate("MainWindow", u"CLOSING", None))
        self.btn_homeHistoHigh.setText(QCoreApplication.translate("MainWindow", u"HIGH", None))
        self.btn_homeHistoLow.setText(QCoreApplication.translate("MainWindow", u"LOW", None))
#if QT_CONFIG(tooltip)
        # self.btn_home1d.setToolTip(QCoreApplication.translate("MainWindow", u"1 Day", None))
#endif // QT_CONFIG(tooltip)
        # self.btn_home1d.setText(QCoreApplication.translate("MainWindow", u"1D", None))
#if QT_CONFIG(tooltip)
        self.btn_home3d.setToolTip(QCoreApplication.translate("MainWindow", u"3 Days", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home3d.setText(QCoreApplication.translate("MainWindow", u"3D", None))
#if QT_CONFIG(tooltip)
        self.btn_home1w.setToolTip(QCoreApplication.translate("MainWindow", u"1 Week", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home1w.setText(QCoreApplication.translate("MainWindow", u"1W", None))
#if QT_CONFIG(tooltip)
        self.btn_home1m.setToolTip(QCoreApplication.translate("MainWindow", u"1 Month", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home1m.setText(QCoreApplication.translate("MainWindow", u"1M", None))
#if QT_CONFIG(tooltip)
        self.btn_home1y.setToolTip(QCoreApplication.translate("MainWindow", u"1 Year", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home1y.setText(QCoreApplication.translate("MainWindow", u"1Y", None))
        self.cryptocurrency.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"HISTORY", None))
        self.btn_histo_closing.setText(QCoreApplication.translate("MainWindow", u"CLOSING", None))
        self.btn_histo_high.setText(QCoreApplication.translate("MainWindow", u"HIGH", None))
        self.btn_histo_low.setText(QCoreApplication.translate("MainWindow", u"LOW", None))
#if QT_CONFIG(tooltip)
        # self.btn_0.setToolTip(QCoreApplication.translate("MainWindow", u"1 Day", None))
#endif // QT_CONFIG(tooltip)
        # self.btn_0.setText(QCoreApplication.translate("MainWindow", u"1D", None))
#if QT_CONFIG(tooltip)
        self.btn_1.setToolTip(QCoreApplication.translate("MainWindow", u"3 Days", None))
#endif // QT_CONFIG(tooltip)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"3D", None))
#if QT_CONFIG(tooltip)
        self.btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"1 Week", None))
#endif // QT_CONFIG(tooltip)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"1W", None))
#if QT_CONFIG(tooltip)
        self.btn_3.setToolTip(QCoreApplication.translate("MainWindow", u"1 Month", None))
#endif // QT_CONFIG(tooltip)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"1M", None))
#if QT_CONFIG(tooltip)
        self.btn_4.setToolTip(QCoreApplication.translate("MainWindow", u"1 Year", None))
#endif // QT_CONFIG(tooltip)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"1Y", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current Price", None))
        self.histoCurrPriceLabel.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Open Price", None))
        self.histoOpenPriceLabel.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"24h High", None))
        self.histoHighPriceLabel.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"24h Low", None))
        self.histoLowPriceLabel.setText("")
        self.marketcap.setText("")
        self.histoMarketLabel.setText("")
        self.volume.setText("")
        self.histoVolumeLabel.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"PREDICTED PRICES", None))
        # self.btn_predPriceClosing.setText(QCoreApplication.translate("MainWindow", u"CLOSING", None))
        # self.btn_predPriceHigh.setText(QCoreApplication.translate("MainWindow", u"HIGH", None))
        # self.btn_predPriceLow.setText(QCoreApplication.translate("MainWindow", u"LOW", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"DAYS:", None))
        self.crypto_daysValue.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(tooltip)
        self.crypto_predRangeLabel.setToolTip(QCoreApplication.translate("MainWindow", u"Prediction Range", None))
#endif // QT_CONFIG(tooltip)
        self.crypto_predRangeLabel.setText("")
    # retranslateUi

