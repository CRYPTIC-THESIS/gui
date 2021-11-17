# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from pyqtgraph import PlotWidget, DateAxisItem, ImageItem, ColorBarItem, PlotItem, ViewBox, mkPen, colormap

from . resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 740)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
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
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb"
                        "(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/Logo.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 7pt \"Segoe UI\"; color: #2AB7CA; } /*rgb(189, 147, 249)*/\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton, #logoutButtonFrame .QPushButton{	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover, #logoutButtonFrame .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}"
                        "\n"
"#topMenu .QPushButton:pressed, #logoutButtonFrame .QPushButton:pressed {	\n"
"	/* background-color: rgb(189, 147, 249); */\n"
"	background-color: rgb(40, 44, 52);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* #bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"} */\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button \n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
""
                        "	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}*/\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab \n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}*/\n"
"\n"
"/* Icon \n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}*/\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close \n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraClos"
                        "eColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }*/\n"
"\n"
"/* Extra Content\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"} */\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { "
                        "background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS*/\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushBu"
                        "tton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"} \n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
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
"    border-bottom: 1px sol"
                        "id rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"/*QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}*/\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    /*border: 1px solid rgb(33, 37, 43);*/\n"
"	background-color: transparent;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"/* QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}*/\n"
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
"/* //////////////////////////////////"
                        "///////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #2AB7CA;\n"
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
"QScrollBar::add-line:horizontal"
                        " {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
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
" QScrollBar::a"
                        "dd-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
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
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, "
                        "49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox #29B3A7*/\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radi"
                        "us: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: #2AB7CA;	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"} \n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	backg"
                        "round-color: rgb(52, 59, 72); \n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: #259CA5; /*rgb(189, 147, 249)*/\n"
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
""
                        "}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #29B3A7;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: #29B3A7;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: #29B3A7;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: #29B3A7;\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	color: #259CA5;\n"
"	font: 13px \"Segoe UI\"; font-weight: bold;\n"
"	/* border: 2px solid rgb(52, 59, 72); */\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"	color: #DDDDDD;\n"
"}"
                        "\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	color: #DDDDDD;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(187, 0))
        self.leftMenuBg.setMaximumSize(QSize(187, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(12, 5, 42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 100, 20))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.titleLeftApp.setFont(font)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(7)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftDescription.setFont(font1)

        self.verticalLayout_2.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 236))
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.topMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_dash = QPushButton(self.topMenu)
        self.btn_dash.setObjectName(u"btn_dash")
        self.btn_dash.setMinimumSize(QSize(0, 59))
        self.btn_dash.setStyleSheet(u"background-image: url(:/icons/images/icons/dash-icon.png);")

        self.verticalLayout_4.addWidget(self.btn_dash)

        self.btn_train = QPushButton(self.topMenu)
        self.btn_train.setObjectName(u"btn_train")
        self.btn_train.setMinimumSize(QSize(0, 59))
        self.btn_train.setStyleSheet(u"background-image: url(:/icons/images/icons/train-icon.png);")

        self.verticalLayout_4.addWidget(self.btn_train)

        self.btn_test = QPushButton(self.topMenu)
        self.btn_test.setObjectName(u"btn_test")
        self.btn_test.setMinimumSize(QSize(0, 59))
        self.btn_test.setStyleSheet(u"background-image: url(:/icons/images/icons/test-icon.png);")

        self.verticalLayout_4.addWidget(self.btn_test)

        self.btn_deploy = QPushButton(self.topMenu)
        self.btn_deploy.setObjectName(u"btn_deploy")
        self.btn_deploy.setMinimumSize(QSize(0, 59))
        self.btn_deploy.setStyleSheet(u"background-image: url(:/icons/images/icons/deploy-icon.png);")

        self.verticalLayout_4.addWidget(self.btn_deploy)


        self.verticalLayout_3.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.logoutButtonFrame = QFrame(self.leftMenuFrame)
        self.logoutButtonFrame.setObjectName(u"logoutButtonFrame")
        self.logoutButtonFrame.setFrameShape(QFrame.NoFrame)
        self.logoutButtonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.logoutButtonFrame)
        self.verticalLayout_116.setSpacing(0)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.btn_logout = QPushButton(self.logoutButtonFrame)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(0, 59))
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/logout-icon.png);")

        self.verticalLayout_116.addWidget(self.btn_logout)


        self.verticalLayout_3.addWidget(self.logoutButtonFrame, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.leftMenuFrame)


        self.horizontalLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.contentBox)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")

        self.horizontalLayout_3.addWidget(self.titleRightInfo, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon1)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.closeAppBtn)


        self.horizontalLayout_2.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.content)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.dash = QWidget()
        self.dash.setObjectName(u"dash")
        self.verticalLayout_8 = QVBoxLayout(self.dash)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.dashHeader = QFrame(self.dash)
        self.dashHeader.setObjectName(u"dashHeader")
        self.dashHeader.setStyleSheet(u"")
        self.dashHeader.setFrameShape(QFrame.NoFrame)
        self.dashHeader.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.dashHeader)
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 0, 10, 10)
        self.frame = QFrame(self.dashHeader)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.cryptocurrency = QLabel(self.frame_4)
        self.cryptocurrency.setObjectName(u"cryptocurrency")
        self.cryptocurrency.setStyleSheet(u"font: 26px \"Segoe UI\"; font-weight: bold;")
        self.cryptocurrency.setFrameShadow(QFrame.Plain)
        self.cryptocurrency.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.cryptocurrency, 0, Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.dateEditFrame = QFrame(self.frame)
        self.dateEditFrame.setObjectName(u"dateEditFrame")
        self.dateEditFrame.setFrameShape(QFrame.NoFrame)
        self.dateEditFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.dateEditFrame)
        self.horizontalLayout_18.setSpacing(12)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.dateEditLabel = QLabel(self.dateEditFrame)
        self.dateEditLabel.setObjectName(u"dateEditLabel")

        self.horizontalLayout_18.addWidget(self.dateEditLabel)

        self.dateEdit = QDateEdit(self.dateEditFrame, calendarPopup=True)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(160, 0))
        self.dateEdit.setStyleSheet(u"font: 15px \"Segoe UI Semibold\"; \n"
"background-color: #DDDDDD;\n"
"color: #2C313A;\n"
"border-radius: 7px;")
        self.dateEdit.setMinimumDate(QDate(2020, 1, 1))
        self.dateEdit.setMaximumDate(QDate.currentDate())
        self.dateEdit.setDate(QDate.currentDate())

        self.horizontalLayout_18.addWidget(self.dateEdit)


        self.horizontalLayout_7.addWidget(self.dateEditFrame, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.frame)

        self.frame_3 = QFrame(self.dashHeader)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.cryptoButtons = QFrame(self.frame_3)
        self.cryptoButtons.setObjectName(u"cryptoButtons")
        self.cryptoButtons.setStyleSheet(u"QPushButton {	\n"
"    background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	border-radius: 18px;\n"
"	width: 49px;\n"
"	height: 49px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: transparent;\n"
"	border-color: #2AB7CA;\n"
"}")
        self.cryptoButtons.setFrameShape(QFrame.NoFrame)
        self.cryptoButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.cryptoButtons)
        self.horizontalLayout_9.setSpacing(17)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_all = QPushButton(self.cryptoButtons)
        self.btn_all.setObjectName(u"btn_all")
        self.btn_all.setMinimumSize(QSize(0, 0))
        self.btn_all.setStyleSheet(u"background-image: url(:/images/images/images/btnDashAll.png);")
        self.btn_all.setIconSize(QSize(45, 45))

        self.horizontalLayout_9.addWidget(self.btn_all)

        self.btn_btc = QPushButton(self.cryptoButtons)
        self.btn_btc.setObjectName(u"btn_btc")
        self.btn_btc.setMinimumSize(QSize(0, 0))
        self.btn_btc.setStyleSheet(u"background-image: url(:/images/images/images/btnBitcoin.png);")
        self.btn_btc.setIconSize(QSize(45, 45))

        self.horizontalLayout_9.addWidget(self.btn_btc)

        self.btn_eth = QPushButton(self.cryptoButtons)
        self.btn_eth.setObjectName(u"btn_eth")
        self.btn_eth.setMinimumSize(QSize(0, 0))
        self.btn_eth.setStyleSheet(u"background-image: url(:/images/images/images/btnEthereum.png);")
        self.btn_eth.setIconSize(QSize(45, 45))

        self.horizontalLayout_9.addWidget(self.btn_eth)

        self.btn_doge = QPushButton(self.cryptoButtons)
        self.btn_doge.setObjectName(u"btn_doge")
        self.btn_doge.setMinimumSize(QSize(0, 0))
        self.btn_doge.setStyleSheet(u"background-image: url(:/images/images/images/btnDogecoin.png);")
        self.btn_doge.setIconSize(QSize(45, 45))

        self.horizontalLayout_9.addWidget(self.btn_doge)


        self.horizontalLayout_8.addWidget(self.cryptoButtons, 0, Qt.AlignLeft)

        self.selected_dateLabelFrame = QFrame(self.frame_3)
        self.selected_dateLabelFrame.setObjectName(u"selected_dateLabelFrame")
        self.selected_dateLabelFrame.setFrameShape(QFrame.NoFrame)
        self.selected_dateLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.selected_dateLabelFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, -1, 0, 0)
        self.selected_dateLabel = QLabel(self.selected_dateLabelFrame)
        self.selected_dateLabel.setObjectName(u"selected_dateLabel")
        self.selected_dateLabel.setMinimumSize(QSize(170, 36))
        self.selected_dateLabel.setStyleSheet(u"font: 20px \"Segoe UI Semibold\";")

        self.verticalLayout_12.addWidget(self.selected_dateLabel)


        self.horizontalLayout_8.addWidget(self.selected_dateLabelFrame, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.frame_3)


        self.verticalLayout_8.addWidget(self.dashHeader)

        self.dashContent = QFrame(self.dash)
        self.dashContent.setObjectName(u"dashContent")
        self.dashContent.setMinimumSize(QSize(0, 486))
        self.dashContent.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#dashFrame .QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#dashFrame .QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#dashFrame .QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"")
        self.dashContent.setFrameShape(QFrame.NoFrame)
        self.dashContent.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.dashContent)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.predictedTableFrame = QFrame(self.dashContent)
        self.predictedTableFrame.setObjectName(u"predictedTableFrame")#2C313A
        self.predictedTableFrame.setStyleSheet(u"background: #21252B;\n"
"border-radius: 10px;\n"
"border: 2px solid #21252B;")
        self.predictedTableFrame.setFrameShape(QFrame.NoFrame)
        self.predictedTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.predictedTableFrame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.predictedTable = QTableWidget(self.predictedTableFrame)
        self.predictedTable.setObjectName(u"predictedTable")
        self.predictedTable.setStyleSheet(u"border: none;")
        self.predictedTable.setFrameShape(QFrame.NoFrame)
        self.predictedTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.predictedTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.predictedTable.horizontalHeader().setDefaultSectionSize(152)
        self.predictedTable.horizontalHeader().setStretchLastSection(True)
        self.predictedTable.verticalHeader().setVisible(False)

        self.verticalLayout_15.addWidget(self.predictedTable)


        self.gridLayout.addWidget(self.predictedTableFrame, 1, 1, 1, 1)

        self.predPriceFrame = QFrame(self.dashContent)
        self.predPriceFrame.setObjectName(u"predPriceFrame")
        self.predPriceFrame.setMinimumSize(QSize(0, 312))
        self.predPriceFrame.setStyleSheet(u"background: #2C313A;\n"
"border-radius: 10px;")
        self.predPriceFrame.setFrameShape(QFrame.NoFrame)
        self.predPriceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.predPriceFrame)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(15, 13, 15, 13)
        self.frame_10 = QFrame(self.predPriceFrame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 0, 10, 0)
        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_16)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_23.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_19.addWidget(self.frame_16)

        self.predPriceButtons = QFrame(self.frame_10)
        self.predPriceButtons.setObjectName(u"predPriceButtons")
        self.predPriceButtons.setStyleSheet(u"* {\n"
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
        self.predPriceButtons.setFrameShape(QFrame.NoFrame)
        self.predPriceButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.predPriceButtons)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        # self.btn_pred_closing = QPushButton(self.predPriceButtons)
        # self.btn_pred_closing.setObjectName(u"btn_pred_closing")
        # self.btn_pred_closing.setMinimumSize(QSize(86, 25))

        # self.horizontalLayout_21.addWidget(self.btn_pred_closing)

        # self.btn_pred_high = QPushButton(self.predPriceButtons)
        # self.btn_pred_high.setObjectName(u"btn_pred_high")
        # self.btn_pred_high.setMinimumSize(QSize(65, 25))

        # self.horizontalLayout_21.addWidget(self.btn_pred_high)

        # self.btn_pred_low = QPushButton(self.predPriceButtons)
        # self.btn_pred_low.setObjectName(u"btn_pred_low")
        # self.btn_pred_low.setMinimumSize(QSize(65, 25))

        # self.horizontalLayout_21.addWidget(self.btn_pred_low)


        self.horizontalLayout_19.addWidget(self.predPriceButtons, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.predGraphFrame = QFrame(self.predPriceFrame)
        self.predGraphFrame.setObjectName(u"predGraphFrame")
        self.predGraphFrame.setMinimumSize(QSize(528, 240))
        self.predGraphFrame.setStyleSheet(u"border-radius: 0; background: transparent;")
        self.predGraphFrame.setFrameShape(QFrame.NoFrame)
        self.predGraphFrame.setFrameShadow(QFrame.Raised)
        
        self.predGraph = PlotWidget(self.predGraphFrame, axisItems={'bottom': DateAxisItem(orientation='bottom')})
        brush = QBrush(QColor(44, 49, 58, 1))
        brush.setStyle(Qt.NoBrush)
        self.predGraph.setBackgroundBrush(brush)
        self.predGraph.addLegend()
        # self.predGraph = MatplotlibWidget(width=3, height=3)

        self.verticalLayout_22 = QVBoxLayout(self.predGraphFrame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_22.addWidget(self.predGraph)

        self.verticalLayout_11.addWidget(self.predGraphFrame)

        self.frame_15 = QFrame(self.predPriceFrame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 15))
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 0, 10, 0)
        self.sliderFrame = QFrame(self.frame_15)
        self.sliderFrame.setObjectName(u"sliderFrame")
        self.sliderFrame.setFrameShape(QFrame.NoFrame)
        self.sliderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.sliderFrame)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.sliderFrame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_22.addWidget(self.label, 0, Qt.AlignVCenter)

        self.horizontalSlider = QSlider(self.sliderFrame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(170, 0))
        self.horizontalSlider.setMinimum(2)
        self.horizontalSlider.setMaximum(14)
        self.horizontalSlider.setSliderPosition(7)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(0)

        self.horizontalLayout_22.addWidget(self.horizontalSlider)

        self.daysValue = QLabel(self.sliderFrame)
        self.daysValue.setObjectName(u"daysValue")

        self.horizontalLayout_22.addWidget(self.daysValue, 0, Qt.AlignVCenter)


        self.horizontalLayout_20.addWidget(self.sliderFrame, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.predictedRangeLabelFrame = QFrame(self.frame_15)
        self.predictedRangeLabelFrame.setObjectName(u"predictedRangeLabelFrame")
        self.predictedRangeLabelFrame.setFrameShape(QFrame.NoFrame)
        self.predictedRangeLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.predictedRangeLabelFrame)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.predictedRangeLabel = QLabel(self.predictedRangeLabelFrame)
        self.predictedRangeLabel.setObjectName(u"predictedRangeLabel")
        self.predictedRangeLabel.setMinimumSize(QSize(236, 12))
        self.predictedRangeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.predictedRangeLabel, 0, Qt.AlignRight)


        self.horizontalLayout_20.addWidget(self.predictedRangeLabelFrame)


        self.verticalLayout_11.addWidget(self.frame_15)


        self.gridLayout.addWidget(self.predPriceFrame, 0, 1, 1, 1)

        self.historyFrame = QFrame(self.dashContent)
        self.historyFrame.setObjectName(u"historyFrame")
        self.historyFrame.setMinimumSize(QSize(0, 0))
        self.historyFrame.setMaximumSize(QSize(453, 16777215))
        self.historyFrame.setStyleSheet(u"background: #2C313A;\n"
"border-radius: 10px;\n"
"")
        self.historyFrame.setFrameShape(QFrame.NoFrame)
        self.historyFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.historyFrame)
        self.verticalLayout_13.setSpacing(13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(15, 13, 15, 13)
        self.currPriceFrame = QFrame(self.historyFrame)
        self.currPriceFrame.setObjectName(u"currPriceFrame")
        self.currPriceFrame.setFrameShape(QFrame.NoFrame)
        self.currPriceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.currPriceFrame)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.currPriceFrame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 0, 10, 0)
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.horizontalLayout_10.addWidget(self.label_3, 0, Qt.AlignLeft)


        self.verticalLayout_14.addWidget(self.frame_13)

        self.currPriceCards = QFrame(self.currPriceFrame)
        self.currPriceCards.setObjectName(u"currPriceCards")
        self.currPriceCards.setMinimumSize(QSize(0, 124))
        self.currPriceCards.setStyleSheet(u"")
        self.currPriceCards.setFrameShape(QFrame.NoFrame)
        self.currPriceCards.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.currPriceCards)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btc_card = QFrame(self.currPriceCards)
        self.btc_card.setObjectName(u"btc_card")
        self.btc_card.setStyleSheet(u"background: #41464E;\n"
"border-radius: 10px;")
        self.btc_card.setFrameShape(QFrame.NoFrame)
        self.btc_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.btc_card)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(10, 10, 10, 10)
        self.frame_7 = QFrame(self.btc_card)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_7)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_21)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_21)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_108.addWidget(self.label_33)

        self.label_21 = QLabel(self.frame_21)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_108.addWidget(self.label_21)


        self.horizontalLayout_35.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_7)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"background-image: url(:/images/images/images/btc-logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right top;")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_35.addWidget(self.frame_22)


        self.verticalLayout_80.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.btcCurrPriceLabelFrame = QFrame(self.btc_card)
        self.btcCurrPriceLabelFrame.setObjectName(u"btcCurrPriceLabelFrame")
        self.btcCurrPriceLabelFrame.setFrameShape(QFrame.NoFrame)
        self.btcCurrPriceLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.btcCurrPriceLabelFrame)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.btcCurrPriceLabel = QLabel(self.btcCurrPriceLabelFrame)
        self.btcCurrPriceLabel.setObjectName(u"btcCurrPriceLabel")
        self.btcCurrPriceLabel.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.btcCurrPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_113.addWidget(self.btcCurrPriceLabel)


        self.verticalLayout_80.addWidget(self.btcCurrPriceLabelFrame)


        self.horizontalLayout_13.addWidget(self.btc_card)

        self.eth_card = QFrame(self.currPriceCards)
        self.eth_card.setObjectName(u"eth_card")
        self.eth_card.setStyleSheet(u"background: #41464E;\n"
"border-radius: 10px;")
        self.eth_card.setFrameShape(QFrame.NoFrame)
        self.eth_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.eth_card)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(10, 10, 10, 10)
        self.frame_26 = QFrame(self.eth_card)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_28)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_28)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_110.addWidget(self.label_34)

        self.label_36 = QLabel(self.frame_28)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_110.addWidget(self.label_36)


        self.horizontalLayout_57.addWidget(self.frame_28)

        self.frame_33 = QFrame(self.frame_26)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"background-image: url(:/images/images/images/eth-logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right top;")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_57.addWidget(self.frame_33)


        self.verticalLayout_109.addWidget(self.frame_26, 0, Qt.AlignTop)

        self.ethCurrPriceLabelFrame = QFrame(self.eth_card)
        self.ethCurrPriceLabelFrame.setObjectName(u"ethCurrPriceLabelFrame")
        self.ethCurrPriceLabelFrame.setFrameShape(QFrame.NoFrame)
        self.ethCurrPriceLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.ethCurrPriceLabelFrame)
        self.verticalLayout_114.setSpacing(0)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.ethCurrPriceLabel = QLabel(self.ethCurrPriceLabelFrame)
        self.ethCurrPriceLabel.setObjectName(u"ethCurrPriceLabel")
        self.ethCurrPriceLabel.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.ethCurrPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_114.addWidget(self.ethCurrPriceLabel)


        self.verticalLayout_109.addWidget(self.ethCurrPriceLabelFrame)


        self.horizontalLayout_13.addWidget(self.eth_card)

        self.doge_card = QFrame(self.currPriceCards)
        self.doge_card.setObjectName(u"doge_card")
        self.doge_card.setStyleSheet(u"background: #41464E;\n"
"border-radius: 10px;")
        self.doge_card.setFrameShape(QFrame.NoFrame)
        self.doge_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.doge_card)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(10, 10, 10, 10)
        self.frame_35 = QFrame(self.doge_card)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_35)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_49)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_49)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_112.addWidget(self.label_38)

        self.label_42 = QLabel(self.frame_49)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_112.addWidget(self.label_42)


        self.horizontalLayout_58.addWidget(self.frame_49)

        self.frame_51 = QFrame(self.frame_35)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"background-image: url(:/images/images/images/doge-logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right top;")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_58.addWidget(self.frame_51)


        self.verticalLayout_111.addWidget(self.frame_35, 0, Qt.AlignTop)

        self.dogeCurrPriceLabelFrame = QFrame(self.doge_card)
        self.dogeCurrPriceLabelFrame.setObjectName(u"dogeCurrPriceLabelFrame")
        self.dogeCurrPriceLabelFrame.setFrameShape(QFrame.NoFrame)
        self.dogeCurrPriceLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.dogeCurrPriceLabelFrame)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.dogeCurrPriceLabel = QLabel(self.dogeCurrPriceLabelFrame)
        self.dogeCurrPriceLabel.setObjectName(u"dogeCurrPriceLabel")
        self.dogeCurrPriceLabel.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.dogeCurrPriceLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_115.addWidget(self.dogeCurrPriceLabel)


        self.verticalLayout_111.addWidget(self.dogeCurrPriceLabelFrame)


        self.horizontalLayout_13.addWidget(self.doge_card)


        self.verticalLayout_14.addWidget(self.currPriceCards)


        self.verticalLayout_13.addWidget(self.currPriceFrame)

        self.daysButtonsFrame = QFrame(self.historyFrame)
        self.daysButtonsFrame.setObjectName(u"daysButtonsFrame")
        self.daysButtonsFrame.setFrameShape(QFrame.NoFrame)
        self.daysButtonsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.daysButtonsFrame)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.daysButtonsFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 0, 10, 0)
        self.frame_18 = QFrame(self.frame_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_18)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_18)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_18.addWidget(self.label_4)


        self.horizontalLayout_11.addWidget(self.frame_18, 0, Qt.AlignLeft)

        self.histoPriceFrame = QFrame(self.frame_2)
        self.histoPriceFrame.setObjectName(u"histoPriceFrame")
        self.histoPriceFrame.setStyleSheet(u"* {\n"
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
        self.histoPriceFrame.setFrameShape(QFrame.NoFrame)
        self.histoPriceFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.histoPriceFrame)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btn_histo_closing = QPushButton(self.histoPriceFrame)
        self.btn_histo_closing.setObjectName(u"btn_histo_closing")
        self.btn_histo_closing.setMinimumSize(QSize(86, 25))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI BOLD"])
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_histo_closing.setFont(font2)
        self.btn_histo_closing.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.btn_histo_closing)

        self.btn_histo_high = QPushButton(self.histoPriceFrame)
        self.btn_histo_high.setObjectName(u"btn_histo_high")
        self.btn_histo_high.setMinimumSize(QSize(65, 25))
        self.btn_histo_high.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.btn_histo_high)

        self.btn_histo_low = QPushButton(self.histoPriceFrame)
        self.btn_histo_low.setObjectName(u"btn_histo_low")
        self.btn_histo_low.setMinimumSize(QSize(65, 25))
        self.btn_histo_low.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.btn_histo_low)


        self.horizontalLayout_11.addWidget(self.histoPriceFrame, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.frame_2)

        self.histoGraphFrame = QFrame(self.daysButtonsFrame)
        self.histoGraphFrame.setObjectName(u"histoGraphFrame")
        self.histoGraphFrame.setMinimumSize(QSize(423, 269))
        self.histoGraphFrame.setFrameShape(QFrame.NoFrame)
        self.histoGraphFrame.setFrameShadow(QFrame.Raised)
        
        self.histoGraph = PlotWidget(self.histoGraphFrame, axisItems={'bottom': DateAxisItem(orientation='bottom')})
        # brush = QBrush(QColor(44, 49, 58, 1))
        # brush.setStyle(Qt.NoBrush)
        self.histoGraph.setBackgroundBrush(brush)
        self.histoGraph.addLegend()
        # self.histoGraph = MatplotlibWidget(width=4.6, height=2.35)
        
        self.verticalLayout_17 = QVBoxLayout(self.histoGraphFrame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_17.addWidget(self.histoGraph)

        self.verticalLayout_16.addWidget(self.histoGraphFrame)

        self.daysButtons = QFrame(self.daysButtonsFrame)
        self.daysButtons.setObjectName(u"daysButtons")
        self.daysButtons.setStyleSheet(u"* {\n"
"	border-radius: 0;\n"
"	border: 0;\n"
"	color: 'white';\n"
"	font: 13px \"Segoe UI Semibold\";\n"
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
"}")
        self.daysButtons.setFrameShape(QFrame.NoFrame)
        self.daysButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.daysButtons)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 0, 0, 0)
        # self.btn_0 = QPushButton(self.daysButtons)
        # self.btn_0.setObjectName(u"btn_0")
        # self.btn_0.setStyleSheet(u"")

        # self.horizontalLayout_14.addWidget(self.btn_0)

        self.btn_1 = QPushButton(self.daysButtons)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.btn_1)

        self.btn_2 = QPushButton(self.daysButtons)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.btn_2)

        self.btn_3 = QPushButton(self.daysButtons)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.btn_3)

        self.btn_4 = QPushButton(self.daysButtons)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.btn_4)


        self.verticalLayout_16.addWidget(self.daysButtons, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.daysButtonsFrame)


        self.gridLayout.addWidget(self.historyFrame, 0, 2, 2, 1)


        self.verticalLayout_8.addWidget(self.dashContent)

        self.stackedWidget.addWidget(self.dash)
        self.train = QWidget()
        self.train.setObjectName(u"train")
        self.verticalLayout_19 = QVBoxLayout(self.train)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, 0, 10, 0)
        self.trainHeader = QFrame(self.train)
        self.trainHeader.setObjectName(u"trainHeader")
        self.trainHeader.setStyleSheet(u"")
        self.trainHeader.setFrameShape(QFrame.NoFrame)
        self.trainHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.trainHeader)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(10, 0, 10, 0)
        self.frame_6 = QFrame(self.trainHeader)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"font: 26px \"Segoe UI\"; font-weight: bold;")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_6)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_20.addWidget(self.label_5, 0, Qt.AlignTop)


        self.horizontalLayout_15.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.frame_20 = QFrame(self.trainHeader)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(234, 35))
        self.frame_20.setStyleSheet(u"")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 20, 0)
        self.btn_startTraining = QPushButton(self.frame_20)
        self.btn_startTraining.setObjectName(u"btn_startTraining")
        self.btn_startTraining.setMinimumSize(QSize(204, 35))
        self.btn_startTraining.setMaximumSize(QSize(234, 35))
        self.btn_startTraining.setLayoutDirection(Qt.RightToLeft)
        self.btn_startTraining.setStyleSheet(u"background-image: url(:/images/images/images/next-cyan.png);\n"
"background-position: right center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-right: 25px solid transparent;\n"
"background-color: transparent;\n"
"text-align: right;\n"
"padding-left: 70px;\n"
"font: 15px \"Segoe UI\"; font-weight: bold;\n"
"")

        self.horizontalLayout_45.addWidget(self.btn_startTraining)


        self.horizontalLayout_15.addWidget(self.frame_20, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_19.addWidget(self.trainHeader)

        self.trainContent = QStackedWidget(self.train)
        self.trainContent.setObjectName(u"trainContent")
        self.trainContent.setStyleSheet(u"")
        self.trainContent.setFrameShape(QFrame.NoFrame)
        self.trainContent.setFrameShadow(QFrame.Raised)
        self.getDataPage = QWidget()
        self.getDataPage.setObjectName(u"getDataPage")
        self.horizontalLayout_16 = QHBoxLayout(self.getDataPage)
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 20, 10, 10)
        self.getDataCard = QFrame(self.getDataPage)
        self.getDataCard.setObjectName(u"getDataCard")
        self.getDataCard.setMinimumSize(QSize(317, 548))
        self.getDataCard.setMaximumSize(QSize(317, 16777215))
        self.getDataCard.setStyleSheet(u"background: #2C313A;\n"
"border-radius: 10px;")
        self.getDataCard.setFrameShape(QFrame.NoFrame)
        self.getDataCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.getDataCard)
        self.verticalLayout_21.setSpacing(13)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(15, 13, 15, 13)
        self.frame_24 = QFrame(self.getDataCard)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 26))
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_24)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(10, 0, 0, 0)
        self.label_6 = QLabel(self.frame_24)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_25.addWidget(self.label_6, 0, Qt.AlignLeft)


        self.verticalLayout_21.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.getDataCard)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 418))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_25)
        self.gridLayout_2.setSpacing(25)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.trainCryptoFrame = QFrame(self.frame_25)
        self.trainCryptoFrame.setObjectName(u"trainCryptoFrame")
        self.trainCryptoFrame.setFrameShape(QFrame.NoFrame)
        self.trainCryptoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.trainCryptoFrame)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.trainCryptoFrame)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 33))
        self.frame_32.setStyleSheet(u"background: #41464E;\n"
"	border-radius: 10px;")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_32)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(15, 8, 15, 8)
        self.label_8 = QLabel(self.frame_32)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_30.addWidget(self.label_8)


        self.verticalLayout_29.addWidget(self.frame_32)

        self.frame_31 = QFrame(self.trainCryptoFrame)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_31)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(15, 0, 15, 0)
        self.cryptoCheckBox = QFrame(self.frame_31)
        self.cryptoCheckBox.setObjectName(u"cryptoCheckBox")
        self.cryptoCheckBox.setFrameShape(QFrame.NoFrame)
        self.cryptoCheckBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.cryptoCheckBox)
        self.verticalLayout_35.setSpacing(8)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.checkBox_btc = QCheckBox(self.cryptoCheckBox)
        self.checkBox_btc.setObjectName(u"checkBox_btc")

        self.verticalLayout_35.addWidget(self.checkBox_btc)

        self.checkBox_eth = QCheckBox(self.cryptoCheckBox)
        self.checkBox_eth.setObjectName(u"checkBox_eth")

        self.verticalLayout_35.addWidget(self.checkBox_eth)

        self.checkBox_doge = QCheckBox(self.cryptoCheckBox)
        self.checkBox_doge.setObjectName(u"checkBox_doge")

        self.verticalLayout_35.addWidget(self.checkBox_doge)


        self.verticalLayout_36.addWidget(self.cryptoCheckBox, 0, Qt.AlignLeft)


        self.verticalLayout_29.addWidget(self.frame_31)


        self.gridLayout_2.addWidget(self.trainCryptoFrame, 1, 0, 1, 1)

        self.trainTimeFrameFrame = QFrame(self.frame_25)
        self.trainTimeFrameFrame.setObjectName(u"trainTimeFrameFrame")
        self.trainTimeFrameFrame.setFrameShape(QFrame.NoFrame)
        self.trainTimeFrameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.trainTimeFrameFrame)
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.divHeader = QFrame(self.trainTimeFrameFrame)
        self.divHeader.setObjectName(u"divHeader")
        self.divHeader.setMaximumSize(QSize(16777215, 33))
        self.divHeader.setStyleSheet(u"background: #41464E;\n"
"	border-radius: 10px;")
        self.divHeader.setFrameShape(QFrame.NoFrame)
        self.divHeader.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.divHeader)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(15, 8, 15, 8)
        self.label_7 = QLabel(self.divHeader)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.label_7)


        self.verticalLayout_27.addWidget(self.divHeader)

        self.frame_30 = QFrame(self.trainTimeFrameFrame)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_30)
        self.verticalLayout_37.setSpacing(8)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(15, 0, 15, 0)
        self.frame_36 = QFrame(self.frame_30)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_36)
        self.verticalLayout_38.setSpacing(8)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.trainFromDateEditFrame = QFrame(self.frame_36)
        self.trainFromDateEditFrame.setObjectName(u"trainFromDateEditFrame")
        self.trainFromDateEditFrame.setFrameShape(QFrame.NoFrame)
        self.trainFromDateEditFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.trainFromDateEditFrame)
        self.horizontalLayout_24.setSpacing(15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.trainFromDateEditFrame)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_24.addWidget(self.label_10)

        self.trainFromDateEdit = QDateEdit(self.trainFromDateEditFrame, calendarPopup=True)
        self.trainFromDateEdit.setObjectName(u"trainFromDateEdit")
        self.trainFromDateEdit.setMinimumSize(QSize(160, 0))
        self.trainFromDateEdit.setStyleSheet(u"font: 15px \"Segoe UI Semibold\"; \n"
"background-color: #21252B;\n"
"border-radius: 7px;")

        self.trainFromDateEdit.setMinimumDate(QDate(2020, 1, 1))
        self.trainFromDateEdit.setMaximumDate(QDate(2021, 10, 31))
        self.trainFromDateEdit.setDate(QDate(2020, 1, 1))

        self.horizontalLayout_24.addWidget(self.trainFromDateEdit)


        self.verticalLayout_38.addWidget(self.trainFromDateEditFrame)

        self.trainUntilDateEditFrame = QFrame(self.frame_36)
        self.trainUntilDateEditFrame.setObjectName(u"trainUntilDateEditFrame")
        self.trainUntilDateEditFrame.setFrameShape(QFrame.NoFrame)
        self.trainUntilDateEditFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.trainUntilDateEditFrame)
        self.horizontalLayout_25.setSpacing(15)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.trainUntilDateEditFrame)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_25.addWidget(self.label_11)

        self.trainUntilDateEdit = QDateEdit(self.trainUntilDateEditFrame, calendarPopup=True)
        self.trainUntilDateEdit.setObjectName(u"trainUntilDateEdit")
        self.trainUntilDateEdit.setMinimumSize(QSize(160, 0))
        self.trainUntilDateEdit.setStyleSheet(u"font: 15px \"Segoe UI Semibold\"; \n"
"background-color: #21252B;\n"
"border-radius: 7px;")

        self.trainUntilDateEdit.setMinimumDate(QDate(2020, 1, 1))
        self.trainUntilDateEdit.setMaximumDate(QDate(2021, 10, 31))
        self.trainUntilDateEdit.setDate(QDate(2021, 10, 31))

        self.horizontalLayout_25.addWidget(self.trainUntilDateEdit)


        self.verticalLayout_38.addWidget(self.trainUntilDateEditFrame)


        self.verticalLayout_37.addWidget(self.frame_36, 0, Qt.AlignLeft)


        self.verticalLayout_27.addWidget(self.frame_30)


        self.gridLayout_2.addWidget(self.trainTimeFrameFrame, 0, 0, 1, 1)

        self.trainSourceFrame = QFrame(self.frame_25)
        self.trainSourceFrame.setObjectName(u"trainSourceFrame")
        self.trainSourceFrame.setFrameShape(QFrame.NoFrame)
        self.trainSourceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.trainSourceFrame)
        self.verticalLayout_31.setSpacing(10)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.trainSourceFrame)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 33))
        self.frame_34.setStyleSheet(u"background: #41464E;\n"
"border-radius: 10px;")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_34)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(15, 8, 15, 8)
        self.label_9 = QLabel(self.frame_34)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_32.addWidget(self.label_9)


        self.verticalLayout_31.addWidget(self.frame_34)

        self.sourceCheckBoxFrame = QFrame(self.trainSourceFrame)
        self.sourceCheckBoxFrame.setObjectName(u"sourceCheckBoxFrame")
        self.sourceCheckBoxFrame.setFrameShape(QFrame.NoFrame)
        self.sourceCheckBoxFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.sourceCheckBoxFrame)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(15, 0, 15, 0)
        self.sourceCheckBox = QFrame(self.sourceCheckBoxFrame)
        self.sourceCheckBox.setObjectName(u"sourceCheckBox")
        self.sourceCheckBox.setFrameShape(QFrame.NoFrame)
        self.sourceCheckBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.sourceCheckBox)
        self.verticalLayout_34.setSpacing(8)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        
        self.radioButton_histo = QRadioButton(self.sourceCheckBox)
        self.radioButton_histo.setObjectName(u"radioButton_histo")
        # self.checkBox_histo.setCheckState(Qt.Checked)
        # self.checkBox_histo.setEnabled(False)

        self.verticalLayout_34.addWidget(self.radioButton_histo)

        self.radioButton_histo_trends = QRadioButton(self.sourceCheckBox)
        self.radioButton_histo_trends.setObjectName(u"radioButton_histo_trends")
        # self.radioButton_histo_trends.setCheckState(Qt.Checked)
        # self.radioButton_histo_trends.setEnabled(False)

        self.verticalLayout_34.addWidget(self.radioButton_histo_trends)

        # self.checkBox_reddit = QCheckBox(self.sourceCheckBox)
        # self.checkBox_reddit.setObjectName(u"checkBox_reddit")
        # self.checkBox_reddit.setCheckState(Qt.Checked)
        # self.checkBox_reddit.setEnabled(False)

        # self.verticalLayout_34.addWidget(self.checkBox_reddit)

        # self.checkBox_gtrends = QCheckBox(self.sourceCheckBox)
        # self.checkBox_gtrends.setObjectName(u"checkBox_gtrends")
        # self.checkBox_gtrends.setCheckState(Qt.Checked)
        # self.checkBox_gtrends.setEnabled(False)

        # self.verticalLayout_34.addWidget(self.checkBox_gtrends)


        self.verticalLayout_33.addWidget(self.sourceCheckBox, 0, Qt.AlignLeft|Qt.AlignTop)


        self.RadioGroup = QButtonGroup()
        self.RadioGroup.addButton(self.radioButton_histo)
        self.RadioGroup.addButton(self.radioButton_histo_trends)


        self.verticalLayout_31.addWidget(self.sourceCheckBoxFrame)


        self.gridLayout_2.addWidget(self.trainSourceFrame, 2, 0, 1, 1)


        self.verticalLayout_21.addWidget(self.frame_25)

        self.frame_29 = QFrame(self.getDataCard)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 71))
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.getDataButtons = QFrame(self.frame_29)
        self.getDataButtons.setObjectName(u"getDataButtons")
        self.getDataButtons.setStyleSheet(u"* {\n"
"	color: #259CA5;\n"
"	font: 13px \"Segoe UI\"; font-weight: bold;\n"
"}")
        self.getDataButtons.setFrameShape(QFrame.NoFrame)
        self.getDataButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.getDataButtons)
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.btn_cancel = QPushButton(self.getDataButtons)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(80, 35))
        self.btn_cancel.setStyleSheet(u"*:hover, *:pressed {\n"
"	color: #DDDDDD;\n"
"	background: #E74C53;\n"
"	border-color: #E74C53;\n"
"}")

        self.horizontalLayout_23.addWidget(self.btn_cancel)

        self.btn_proceed = QPushButton(self.getDataButtons)
        self.btn_proceed.setObjectName(u"btn_proceed")
        self.btn_proceed.setMinimumSize(QSize(90, 35))
        self.btn_proceed.setStyleSheet(u"*{\n"
"	background: rgb(33, 37, 43);\n"
"}\n"
"\n"
"*:hover, *:pressed {\n"
"	color: #DDDDDD;\n"
"	background: #008A66;\n"
"	border-color: #008A66;\n"
"}")

        self.horizontalLayout_23.addWidget(self.btn_proceed)


        self.horizontalLayout_17.addWidget(self.getDataButtons, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_29)


        self.horizontalLayout_16.addWidget(self.getDataCard)

        self.trainDatasetCard = QFrame(self.getDataPage)
        self.trainDatasetCard.setObjectName(u"trainDatasetCard")
        self.trainDatasetCard.setStyleSheet(u"background: #2C313A;\n"
"border-radius: 10px;")
        self.trainDatasetCard.setFrameShape(QFrame.NoFrame)
        self.trainDatasetCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.trainDatasetCard)
        self.verticalLayout_26.setSpacing(13)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(15, 13, 15, 13)
        self.frame_38 = QFrame(self.trainDatasetCard)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(16777215, 26))
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(10, 0, 0, 0)
        self.label_12 = QLabel(self.frame_38)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.horizontalLayout_26.addWidget(self.label_12, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_26.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.trainDatasetCard)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 500))
        self.frame_39.setMaximumSize(QSize(16777215, 500))
        self.frame_39.setStyleSheet(u"background: #2C313A;\n"
"border-radius: 10px;\n"
"border: 2px solid #21252B;")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_39)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.trainTable = QTableWidget(self.frame_39)
        self.trainTable.setObjectName(u"trainTable")
        self.trainTable.setStyleSheet(u"border: none;")
        self.trainTable.setFrameShape(QFrame.NoFrame)
        self.trainTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.trainTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.trainTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.trainTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.trainTable.horizontalHeader().setDefaultSectionSize(152)
        self.trainTable.horizontalHeader().setStretchLastSection(True)
        self.trainTable.verticalHeader().setVisible(False)

        self.verticalLayout_39.addWidget(self.trainTable)


        self.verticalLayout_26.addWidget(self.frame_39)


        self.horizontalLayout_16.addWidget(self.trainDatasetCard)

        self.trainContent.addWidget(self.getDataPage)
        self.startTrainingPage = QWidget()
        self.startTrainingPage.setObjectName(u"startTrainingPage")
        self.verticalLayout_40 = QVBoxLayout(self.startTrainingPage)
        self.verticalLayout_40.setSpacing(20)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(10, 20, 10, 10)
        self.frame_40 = QFrame(self.startTrainingPage)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(900, 465))
        self.frame_40.setMaximumSize(QSize(16777215, 16777215))
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_40)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(10, 10, 10, 10)
        self.trainTerminal = QPlainTextEdit(self.frame_40)
        self.trainTerminal.setObjectName(u"trainTerminal")
        self.trainTerminal.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.trainTerminal.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.trainTerminal.setReadOnly(True)

        self.verticalLayout_41.addWidget(self.trainTerminal)


        self.verticalLayout_40.addWidget(self.frame_40, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.trainContent.addWidget(self.startTrainingPage)

        self.verticalLayout_19.addWidget(self.trainContent)

        self.stackedWidget.addWidget(self.train)
        self.test = QWidget()
        self.test.setObjectName(u"test")
        self.verticalLayout_73 = QVBoxLayout(self.test)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(10, 0, 10, 0)
        self.testHeader = QFrame(self.test)
        self.testHeader.setObjectName(u"testHeader")
        self.testHeader.setStyleSheet(u"")
        self.testHeader.setFrameShape(QFrame.NoFrame)
        self.testHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.testHeader)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(10, 0, 10, 0)
        self.frame_41 = QFrame(self.testHeader)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"font: 26px \"Segoe UI\"; font-weight: bold;")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_41)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_41)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_42.addWidget(self.label_13)


        self.horizontalLayout_27.addWidget(self.frame_41, 0, Qt.AlignLeft)

        self.frame_42 = QFrame(self.testHeader)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(254, 35))
        self.frame_42.setStyleSheet(u"")
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_42)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 20, 0)
        self.btn_viewDataAnalysis = QPushButton(self.frame_42)
        self.btn_viewDataAnalysis.setObjectName(u"btn_viewDataAnalysis")
        self.btn_viewDataAnalysis.setMinimumSize(QSize(204, 35))
        self.btn_viewDataAnalysis.setMaximumSize(QSize(254, 35))
        self.btn_viewDataAnalysis.setLayoutDirection(Qt.RightToLeft)
        self.btn_viewDataAnalysis.setStyleSheet(u"background-image: url(:/images/images/images/next-cyan.png);\n"
"background-position: right center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-right: 25px solid transparent;\n"
"background-color: transparent;\n"
"text-align: right;\n"
"padding-left: 70px;\n"
"font: 15px \"Segoe UI\"; font-weight: bold;\n"
"")

        self.verticalLayout_85.addWidget(self.btn_viewDataAnalysis)


        self.horizontalLayout_27.addWidget(self.frame_42, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_73.addWidget(self.testHeader)

        self.testContent = QStackedWidget(self.test)
        self.testContent.setObjectName(u"testContent")
        self.testContent.setStyleSheet(u"")
        self.testContent.setFrameShape(QFrame.NoFrame)
        self.testContent.setFrameShadow(QFrame.Raised)
        self.testingPage = QWidget()
        self.testingPage.setObjectName(u"testingPage")
        self.horizontalLayout_28 = QHBoxLayout(self.testingPage)
        self.horizontalLayout_28.setSpacing(20)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(10, 20, 10, 10)
        self.testDatasetCard = QFrame(self.testingPage)
        self.testDatasetCard.setObjectName(u"testDatasetCard")
        self.testDatasetCard.setMinimumSize(QSize(317, 548))
        self.testDatasetCard.setMaximumSize(QSize(317, 16777215))
        self.testDatasetCard.setStyleSheet(u"background: #2C313A;\n"
"border-radius: 10px;")
        self.testDatasetCard.setFrameShape(QFrame.NoFrame)
        self.testDatasetCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.testDatasetCard)
        self.verticalLayout_43.setSpacing(13)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(15, 13, 15, 13)
        self.frame_44 = QFrame(self.testDatasetCard)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(0, 26))
        self.frame_44.setMaximumSize(QSize(16777215, 26))
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_44)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(10, 0, 0, 0)
        self.label_14 = QLabel(self.frame_44)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_44.addWidget(self.label_14, 0, Qt.AlignLeft)


        self.verticalLayout_43.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.testDatasetCard)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 418))
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_45)
        self.gridLayout_3.setSpacing(25)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.testCryptoFrame = QFrame(self.frame_45)
        self.testCryptoFrame.setObjectName(u"testCryptoFrame")
        self.testCryptoFrame.setFrameShape(QFrame.NoFrame)
        self.testCryptoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.testCryptoFrame)
        self.verticalLayout_45.setSpacing(10)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.testCryptoFrame)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(16777215, 33))
        self.frame_47.setStyleSheet(u"background: #41464E;\n"
"	border-radius: 10px;")
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_47)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(15, 8, 15, 8)
        self.label_15 = QLabel(self.frame_47)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_46.addWidget(self.label_15)


        self.verticalLayout_45.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.testCryptoFrame)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMaximumSize(QSize(16777215, 79))
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_48)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(15, 0, 15, 0)
        self.testCryptoListFrame = QFrame(self.frame_48)
        self.testCryptoListFrame.setObjectName(u"testCryptoListFrame")
        self.testCryptoListFrame.setFrameShape(QFrame.NoFrame)
        self.testCryptoListFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.testCryptoListFrame)
        self.verticalLayout_48.setSpacing(8)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.testCryptoList = QListWidget(self.testCryptoListFrame)
        self.testCryptoList.setObjectName(u"testCryptoList")
        self.testCryptoList.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_48.addWidget(self.testCryptoList)


        self.verticalLayout_47.addWidget(self.testCryptoListFrame, 0, Qt.AlignLeft)


        self.verticalLayout_45.addWidget(self.frame_48)


        self.gridLayout_3.addWidget(self.testCryptoFrame, 1, 0, 1, 1)

        self.testTimeFrameFrame = QFrame(self.frame_45)
        self.testTimeFrameFrame.setObjectName(u"testTimeFrameFrame")
        self.testTimeFrameFrame.setFrameShape(QFrame.NoFrame)
        self.testTimeFrameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.testTimeFrameFrame)
        self.verticalLayout_49.setSpacing(10)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.divHeader_2 = QFrame(self.testTimeFrameFrame)
        self.divHeader_2.setObjectName(u"divHeader_2")
        self.divHeader_2.setMaximumSize(QSize(16777215, 33))
        self.divHeader_2.setStyleSheet(u"background: #41464E;\n"
"	border-radius: 10px;")
        self.divHeader_2.setFrameShape(QFrame.NoFrame)
        self.divHeader_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.divHeader_2)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(15, 8, 15, 8)
        self.label_16 = QLabel(self.divHeader_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"")

        self.verticalLayout_50.addWidget(self.label_16)


        self.verticalLayout_49.addWidget(self.divHeader_2)

        self.frame_50 = QFrame(self.testTimeFrameFrame)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(16777215, 52))
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_50)
        self.verticalLayout_51.setSpacing(8)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(15, 0, 15, 0)
        self.testTimeFrameListFrame = QFrame(self.frame_50)
        self.testTimeFrameListFrame.setObjectName(u"testTimeFrameListFrame")
        self.testTimeFrameListFrame.setFrameShape(QFrame.NoFrame)
        self.testTimeFrameListFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.testTimeFrameListFrame)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.testTimeFrameList = QListWidget(self.testTimeFrameListFrame)
        self.testTimeFrameList.setObjectName(u"testTimeFrameList")
        self.testTimeFrameList.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_52.addWidget(self.testTimeFrameList)


        self.verticalLayout_51.addWidget(self.testTimeFrameListFrame, 0, Qt.AlignLeft)


        self.verticalLayout_49.addWidget(self.frame_50)


        self.gridLayout_3.addWidget(self.testTimeFrameFrame, 0, 0, 1, 1)

        self.testSourceFrame = QFrame(self.frame_45)
        self.testSourceFrame.setObjectName(u"testSourceFrame")
        self.testSourceFrame.setFrameShape(QFrame.NoFrame)
        self.testSourceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.testSourceFrame)
        self.verticalLayout_53.setSpacing(10)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.testSourceFrame)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMaximumSize(QSize(16777215, 33))
        self.frame_55.setStyleSheet(u"background: #41464E;\n"
"border-radius: 10px;")
        self.frame_55.setFrameShape(QFrame.NoFrame)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_55)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(15, 8, 15, 8)
        self.label_23 = QLabel(self.frame_55)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_66.addWidget(self.label_23)


        self.verticalLayout_53.addWidget(self.frame_55)

        self.frame_73 = QFrame(self.testSourceFrame)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMaximumSize(QSize(16777215, 108))
        self.frame_73.setFrameShape(QFrame.NoFrame)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_73)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(15, 0, 15, 0)
        self.testSourceListFrame = QFrame(self.frame_73)
        self.testSourceListFrame.setObjectName(u"testSourceListFrame")
        self.testSourceListFrame.setFrameShape(QFrame.NoFrame)
        self.testSourceListFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.testSourceListFrame)
        self.verticalLayout_68.setSpacing(8)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.testSourceList = QListWidget(self.testSourceListFrame)
        self.testSourceList.setObjectName(u"testSourceList")
        self.testSourceList.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_68.addWidget(self.testSourceList)


        self.verticalLayout_67.addWidget(self.testSourceListFrame, 0, Qt.AlignLeft)


        self.verticalLayout_53.addWidget(self.frame_73)


        self.gridLayout_3.addWidget(self.testSourceFrame, 2, 0, 1, 1)


        self.verticalLayout_43.addWidget(self.frame_45)

        self.frame_52 = QFrame(self.testDatasetCard)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 71))
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.testDatasetButtons = QFrame(self.frame_52)
        self.testDatasetButtons.setObjectName(u"testDatasetButtons")
        self.testDatasetButtons.setStyleSheet(u"")
        self.testDatasetButtons.setFrameShape(QFrame.NoFrame)
        self.testDatasetButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.testDatasetButtons)
        self.horizontalLayout_30.setSpacing(20)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.btn_getData = QPushButton(self.testDatasetButtons)
        self.btn_getData.setObjectName(u"btn_getData")
        self.btn_getData.setMinimumSize(QSize(90, 35))

        self.horizontalLayout_30.addWidget(self.btn_getData)

        self.btn_startTesting = QPushButton(self.testDatasetButtons)
        self.btn_startTesting.setObjectName(u"btn_startTesting")
        self.btn_startTesting.setMinimumSize(QSize(135, 35))
        self.btn_startTesting.setStyleSheet(u"* { background: rgb(33, 37, 43);}")

        self.horizontalLayout_30.addWidget(self.btn_startTesting)


        self.horizontalLayout_29.addWidget(self.testDatasetButtons, 0, Qt.AlignRight)


        self.verticalLayout_43.addWidget(self.frame_52)


        self.horizontalLayout_28.addWidget(self.testDatasetCard)

        self.testingDataCard = QFrame(self.testingPage)
        self.testingDataCard.setObjectName(u"testingDataCard")
        self.testingDataCard.setStyleSheet(u"background: #2C313A;\n"
"border-radius: 10px;")
        self.testingDataCard.setFrameShape(QFrame.NoFrame)
        self.testingDataCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.testingDataCard)
        self.verticalLayout_69.setSpacing(13)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(15, 13, 15, 13)
        self.frame_76 = QFrame(self.testingDataCard)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(0, 26))
        self.frame_76.setMaximumSize(QSize(16777215, 26))
        self.frame_76.setFrameShape(QFrame.NoFrame)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(10, 0, 0, 0)
        self.label_24 = QLabel(self.frame_76)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.horizontalLayout_37.addWidget(self.label_24, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_69.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.testingDataCard)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(0, 500))
        self.frame_77.setMaximumSize(QSize(16777215, 500))
        self.frame_77.setFrameShape(QFrame.NoFrame)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_77)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.testTerminalFrame = QFrame(self.frame_77)
        self.testTerminalFrame.setObjectName(u"testTerminalFrame")
        self.testTerminalFrame.setMinimumSize(QSize(0, 465))
        self.testTerminalFrame.setMaximumSize(QSize(16777215, 16777215))
        self.testTerminalFrame.setFrameShape(QFrame.NoFrame)
        self.testTerminalFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.testTerminalFrame)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.testTerminal = QPlainTextEdit(self.testTerminalFrame)
        self.testTerminal.setObjectName(u"testTerminal")
        self.testTerminal.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.testTerminal.setFrameShape(QFrame.NoFrame)
        self.testTerminal.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.testTerminal.setReadOnly(True)

        self.verticalLayout_74.addWidget(self.testTerminal)


        self.verticalLayout_70.addWidget(self.testTerminalFrame, 0, Qt.AlignTop)


        self.verticalLayout_69.addWidget(self.frame_77)


        self.horizontalLayout_28.addWidget(self.testingDataCard)

        self.testContent.addWidget(self.testingPage)
        self.dataAnalysisPage = QWidget()
        self.dataAnalysisPage.setObjectName(u"dataAnalysisPage")
        self.verticalLayout_86 = QVBoxLayout(self.dataAnalysisPage)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(10, 20, 10, 10)
        self.testDataAnalysisCard = QFrame(self.dataAnalysisPage)
        self.testDataAnalysisCard.setObjectName(u"testDataAnalysisCard")
        self.testDataAnalysisCard.setStyleSheet(u"background: #2C313A;\n"
"border-radius: 10px;")
        self.testDataAnalysisCard.setFrameShape(QFrame.NoFrame)
        self.testDataAnalysisCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.testDataAnalysisCard)
        self.verticalLayout_87.setSpacing(13)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(15, 13, 15, 13)
        self.frame_8 = QFrame(self.testDataAnalysisCard)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 35))
        self.frame_8.setMaximumSize(QSize(16777215, 35))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(10, 0, 10, 0)
        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_11)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_11)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_88.addWidget(self.label_30, 0, Qt.AlignLeft)


        self.horizontalLayout_46.addWidget(self.frame_11)

        self.testCryptoComboFrame = QFrame(self.frame_8)
        self.testCryptoComboFrame.setObjectName(u"testCryptoComboFrame")
        self.testCryptoComboFrame.setFrameShape(QFrame.NoFrame)
        self.testCryptoComboFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.testCryptoComboFrame)
        self.horizontalLayout_47.setSpacing(13)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.testCryptoComboFrame)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_47.addWidget(self.label_31)

        self.testCryptoCombo = QComboBox(self.testCryptoComboFrame)
        self.testCryptoCombo.setObjectName(u"testCryptoCombo")
        self.testCryptoCombo.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_47.addWidget(self.testCryptoCombo)


        self.horizontalLayout_46.addWidget(self.testCryptoComboFrame, 0, Qt.AlignRight)


        self.verticalLayout_87.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.testDataAnalysisCard)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_9)
        self.verticalLayout_89.setSpacing(20)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 380))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_17)
        self.verticalLayout_91.setSpacing(10)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(10, 10, 10, 10)
        self.frame_14 = QFrame(self.frame_17)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 26))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(10, 0, 10, 0)
        self.label_32 = QLabel(self.frame_14)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_48.addWidget(self.label_32)


        self.verticalLayout_91.addWidget(self.frame_14, 0, Qt.AlignRight)

        self.corrAnalysisGraphFrame = QFrame(self.frame_17)
        self.corrAnalysisGraphFrame.setObjectName(u"corrAnalysisGraphFrame")
        self.corrAnalysisGraphFrame.setFrameShape(QFrame.NoFrame)
        self.corrAnalysisGraphFrame.setFrameShadow(QFrame.Raised)

        # self.corrAnalysisGraph = PlotWidget(self.corrAnalysisGraphFrame)
        # brush = QBrush(QColor(44, 49, 58, 1))
        # brush.setStyle(Qt.NoBrush)
        # self.corrAnalysisGraph.setBackgroundBrush(brush)
        # # self.predGraph = MatplotlibWidget(width=3, height=3)

        self.corrAnalysisGraph = QLabel(self.corrAnalysisGraphFrame)
        self.verticalLayout_corr = QVBoxLayout(self.corrAnalysisGraphFrame)
        self.verticalLayout_corr.setSpacing(0)
        self.verticalLayout_corr.setObjectName(u"verticalLayout_corr")
        self.verticalLayout_corr.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_corr.addWidget(self.corrAnalysisGraph)

        self.verticalLayout_91.addWidget(self.corrAnalysisGraphFrame)


        self.horizontalLayout_5.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_12)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_19)
        self.verticalLayout_92.setSpacing(10)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(10, 10, 10, 10)
        self.frame_27 = QFrame(self.frame_19)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 26))
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(10, 0, 10, 0)
        self.label_35 = QLabel(self.frame_27)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_49.addWidget(self.label_35)


        self.verticalLayout_92.addWidget(self.frame_27, 0, Qt.AlignRight)

        self.conMatrixGraphFrame = QFrame(self.frame_19)
        self.conMatrixGraphFrame.setObjectName(u"conMatrixGraphFrame")
        self.conMatrixGraphFrame.setFrameShape(QFrame.NoFrame)
        self.conMatrixGraphFrame.setFrameShadow(QFrame.Raised)

        # self.conMatrixGraph = PlotWidget(self.conMatrixGraphFrame)
        # brush = QBrush(QColor(44, 49, 58, 1))
        # brush.setStyle(Qt.NoBrush)
        # self.conMatrixGraph.setBackgroundBrush(brush)
        # # self.predGraph = MatplotlibWidget(width=3, height=3)

        self.conMatrixGraph = QLabel(self.conMatrixGraphFrame)
        self.verticalLayout_conf = QVBoxLayout(self.conMatrixGraphFrame)
        self.verticalLayout_conf.setSpacing(0)
        self.verticalLayout_conf.setObjectName(u"verticalLayout_conf")
        self.verticalLayout_conf.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_conf.addWidget(self.conMatrixGraph, alignment=Qt.AlignCenter)

        self.verticalLayout_92.addWidget(self.conMatrixGraphFrame)


        self.horizontalLayout_5.addWidget(self.frame_19)


        self.verticalLayout_89.addWidget(self.frame_12)

        self.dataAnalysisTableFrame = QFrame(self.frame_9)
        self.dataAnalysisTableFrame.setObjectName(u"dataAnalysisTableFrame")
        self.dataAnalysisTableFrame.setStyleSheet(u"background: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.dataAnalysisTableFrame.setFrameShape(QFrame.NoFrame)
        self.dataAnalysisTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.dataAnalysisTableFrame)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.dataAnalysisTable = QTableWidget(self.dataAnalysisTableFrame)
        self.dataAnalysisTable.setObjectName(u"dataAnalysisTable")
        self.dataAnalysisTable.setFrameShape(QFrame.NoFrame)
        self.dataAnalysisTable.setStyleSheet(u"color: #2AB7CA;")
        self.dataAnalysisTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.dataAnalysisTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.dataAnalysisTable.verticalHeader().setVisible(False)

        self.verticalLayout_90.addWidget(self.dataAnalysisTable)


        self.verticalLayout_89.addWidget(self.dataAnalysisTableFrame)


        self.verticalLayout_87.addWidget(self.frame_9)


        self.verticalLayout_86.addWidget(self.testDataAnalysisCard)

        self.testContent.addWidget(self.dataAnalysisPage)

        self.verticalLayout_73.addWidget(self.testContent)

        self.stackedWidget.addWidget(self.test)
        self.deploy = QWidget()
        self.deploy.setObjectName(u"deploy")
        self.verticalLayout_54 = QVBoxLayout(self.deploy)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(10, 0, 10, 0)
        self.frame_56 = QFrame(self.deploy)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"")
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(10, 0, 10, 0)
        self.frame_58 = QFrame(self.frame_56)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_58)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_58)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 26px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_55.addWidget(self.label_17)


        self.horizontalLayout_31.addWidget(self.frame_58, 0, Qt.AlignLeft)

        self.frame_59 = QFrame(self.frame_56)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_31.addWidget(self.frame_59)


        self.verticalLayout_54.addWidget(self.frame_56)

        self.deployContent = QFrame(self.deploy)
        self.deployContent.setObjectName(u"deployContent")
        self.deployContent.setStyleSheet(u"")
        self.deployContent.setFrameShape(QFrame.NoFrame)
        self.deployContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.deployContent)
        self.horizontalLayout_34.setSpacing(20)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(10, 20, 10, 10)
        self.deployDatasetCard = QFrame(self.deployContent)
        self.deployDatasetCard.setObjectName(u"deployDatasetCard")
        self.deployDatasetCard.setMinimumSize(QSize(317, 548))
        self.deployDatasetCard.setMaximumSize(QSize(317, 16777215))
        self.deployDatasetCard.setStyleSheet(u"background: #2C313A;\n"
"border-radius: 10px;")
        self.deployDatasetCard.setFrameShape(QFrame.NoFrame)
        self.deployDatasetCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.deployDatasetCard)
        self.verticalLayout_56.setSpacing(13)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(15, 13, 15, 13)
        self.frame_60 = QFrame(self.deployDatasetCard)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 26))
        self.frame_60.setMaximumSize(QSize(16777215, 26))
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_60)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(10, 0, 0, 0)
        self.label_18 = QLabel(self.frame_60)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_57.addWidget(self.label_18, 0, Qt.AlignLeft)


        self.verticalLayout_56.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.deployDatasetCard)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(0, 418))
        self.frame_61.setFrameShape(QFrame.NoFrame)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_61)
        self.gridLayout_4.setSpacing(25)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.deployCryptoFrame = QFrame(self.frame_61)
        self.deployCryptoFrame.setObjectName(u"deployCryptoFrame")
        self.deployCryptoFrame.setFrameShape(QFrame.NoFrame)
        self.deployCryptoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.deployCryptoFrame)
        self.verticalLayout_58.setSpacing(10)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_63 = QFrame(self.deployCryptoFrame)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMaximumSize(QSize(16777215, 33))
        self.frame_63.setStyleSheet(u"background: #41464E;\n"
"	border-radius: 10px;")
        self.frame_63.setFrameShape(QFrame.NoFrame)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_63)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(15, 8, 15, 8)
        self.label_19 = QLabel(self.frame_63)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_59.addWidget(self.label_19)


        self.verticalLayout_58.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.deployCryptoFrame)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMaximumSize(QSize(16777215, 79))
        self.frame_64.setFrameShape(QFrame.NoFrame)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_64)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(15, 0, 15, 0)
        self.deployCryptoListFrame = QFrame(self.frame_64)
        self.deployCryptoListFrame.setObjectName(u"deployCryptoListFrame")
        self.deployCryptoListFrame.setFrameShape(QFrame.NoFrame)
        self.deployCryptoListFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.deployCryptoListFrame)
        self.verticalLayout_61.setSpacing(8)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.deployCryptoList = QListWidget(self.deployCryptoListFrame)
        self.deployCryptoList.setObjectName(u"deployCryptoList")
        self.deployCryptoList.setFrameShape(QFrame.NoFrame)
        self.deployCryptoList.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_61.addWidget(self.deployCryptoList)


        self.verticalLayout_60.addWidget(self.deployCryptoListFrame, 0, Qt.AlignLeft)


        self.verticalLayout_58.addWidget(self.frame_64)


        self.gridLayout_4.addWidget(self.deployCryptoFrame, 1, 0, 1, 1)

        self.deployTimeFrameFrame = QFrame(self.frame_61)
        self.deployTimeFrameFrame.setObjectName(u"deployTimeFrameFrame")
        self.deployTimeFrameFrame.setFrameShape(QFrame.NoFrame)
        self.deployTimeFrameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.deployTimeFrameFrame)
        self.verticalLayout_62.setSpacing(10)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.divHeader_3 = QFrame(self.deployTimeFrameFrame)
        self.divHeader_3.setObjectName(u"divHeader_3")
        self.divHeader_3.setMaximumSize(QSize(16777215, 33))
        self.divHeader_3.setStyleSheet(u"background: #41464E;\n"
"	border-radius: 10px;")
        self.divHeader_3.setFrameShape(QFrame.NoFrame)
        self.divHeader_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.divHeader_3)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(15, 8, 15, 8)
        self.label_20 = QLabel(self.divHeader_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"")

        self.verticalLayout_63.addWidget(self.label_20)


        self.verticalLayout_62.addWidget(self.divHeader_3)

        self.frame_66 = QFrame(self.deployTimeFrameFrame)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMaximumSize(QSize(16777215, 52))
        self.frame_66.setFrameShape(QFrame.NoFrame)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_66)
        self.verticalLayout_64.setSpacing(8)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(15, 0, 15, 0)
        self.deployTimeFrameListFrame = QFrame(self.frame_66)
        self.deployTimeFrameListFrame.setObjectName(u"deployTimeFrameListFrame")
        self.deployTimeFrameListFrame.setFrameShape(QFrame.NoFrame)
        self.deployTimeFrameListFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.deployTimeFrameListFrame)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.deployTimeFrameList = QListWidget(self.deployTimeFrameListFrame)
        self.deployTimeFrameList.setObjectName(u"deployTimeFrameList")
        self.deployTimeFrameList.setFrameShape(QFrame.NoFrame)
        self.deployTimeFrameList.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_65.addWidget(self.deployTimeFrameList)


        self.verticalLayout_64.addWidget(self.deployTimeFrameListFrame, 0, Qt.AlignLeft)


        self.verticalLayout_62.addWidget(self.frame_66)


        self.gridLayout_4.addWidget(self.deployTimeFrameFrame, 0, 0, 1, 1)

        self.deploySourceFrame = QFrame(self.frame_61)
        self.deploySourceFrame.setObjectName(u"deploySourceFrame")
        self.deploySourceFrame.setFrameShape(QFrame.NoFrame)
        self.deploySourceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.deploySourceFrame)
        self.verticalLayout_76.setSpacing(10)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.frame_69 = QFrame(self.deploySourceFrame)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMaximumSize(QSize(16777215, 33))
        self.frame_69.setStyleSheet(u"background: #41464E;\n"
"border-radius: 10px;")
        self.frame_69.setFrameShape(QFrame.NoFrame)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_69)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(15, 8, 15, 8)
        self.label_26 = QLabel(self.frame_69)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_77.addWidget(self.label_26)


        self.verticalLayout_76.addWidget(self.frame_69)

        self.frame_74 = QFrame(self.deploySourceFrame)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMaximumSize(QSize(16777215, 108))
        self.frame_74.setFrameShape(QFrame.NoFrame)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_74)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(15, 0, 15, 0)
        self.deploySourceListFrame = QFrame(self.frame_74)
        self.deploySourceListFrame.setObjectName(u"deploySourceListFrame")
        self.deploySourceListFrame.setFrameShape(QFrame.NoFrame)
        self.deploySourceListFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.deploySourceListFrame)
        self.verticalLayout_79.setSpacing(8)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.deploySourceList = QListWidget(self.deploySourceListFrame)
        self.deploySourceList.setObjectName(u"deploySourceList")
        self.deploySourceList.setFrameShape(QFrame.NoFrame)
        self.deploySourceList.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_79.addWidget(self.deploySourceList)


        self.verticalLayout_78.addWidget(self.deploySourceListFrame, 0, Qt.AlignLeft)


        self.verticalLayout_76.addWidget(self.frame_74)


        self.gridLayout_4.addWidget(self.deploySourceFrame, 2, 0, 1, 1)


        self.verticalLayout_56.addWidget(self.frame_61)

        self.frame_70 = QFrame(self.deployDatasetCard)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(0, 71))
        self.frame_70.setFrameShape(QFrame.NoFrame)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.deployButtonFrame = QFrame(self.frame_70)
        self.deployButtonFrame.setObjectName(u"deployButtonFrame")
        self.deployButtonFrame.setStyleSheet(u"")
        self.deployButtonFrame.setFrameShape(QFrame.NoFrame)
        self.deployButtonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.deployButtonFrame)
        self.horizontalLayout_33.setSpacing(20)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.btn_reset = QPushButton(self.deployButtonFrame)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMinimumSize(QSize(80, 35))
        self.btn_reset.setStyleSheet(u"*:hover, *:pressed {\n"
"	color: #DDDDDD;\n"
"	background: #E74C53;\n"
"	border-color: #E74C53;\n"
"}")

        self.horizontalLayout_33.addWidget(self.btn_reset)

        self.btn_deployDeploy = QPushButton(self.deployButtonFrame)
        self.btn_deployDeploy.setObjectName(u"btn_deployDeploy")
        self.btn_deployDeploy.setMinimumSize(QSize(80, 35))
        self.btn_deployDeploy.setStyleSheet(u"*{\n"
"	background: rgb(33, 37, 43);\n"
"}\n"
"\n"
"*:hover, *:pressed {\n"
"	color: #DDDDDD;\n"
"	background: #008A66;\n"
"	border-color: #008A66;\n"
"}")

        self.horizontalLayout_33.addWidget(self.btn_deployDeploy)


        self.horizontalLayout_32.addWidget(self.deployButtonFrame, 0, Qt.AlignRight)


        self.verticalLayout_56.addWidget(self.frame_70)


        self.horizontalLayout_34.addWidget(self.deployDatasetCard)

        self.deployPredCard = QFrame(self.deployContent)
        self.deployPredCard.setObjectName(u"deployPredCard")
        self.deployPredCard.setStyleSheet(u"* {\n"
"	background: #2C313A;\n"
"	border-radius: 10px;\n"
"}")
        self.deployPredCard.setFrameShape(QFrame.NoFrame)
        self.deployPredCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.deployPredCard)
        self.verticalLayout_71.setSpacing(13)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(15, 13, 15, 15)
        self.frame_5 = QFrame(self.deployPredCard)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 35))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_41.setSpacing(10)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.filterFrame = QFrame(self.frame_5)
        self.filterFrame.setObjectName(u"filterFrame")
        self.filterFrame.setStyleSheet(u"")
        self.filterFrame.setFrameShape(QFrame.NoFrame)
        self.filterFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.filterFrame)
        self.horizontalLayout_36.setSpacing(10)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(10, 0, 10, 0)
        self.deployDateEditFrame = QFrame(self.filterFrame)
        self.deployDateEditFrame.setObjectName(u"deployDateEditFrame")
        self.deployDateEditFrame.setFrameShape(QFrame.NoFrame)
        self.deployDateEditFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.deployDateEditFrame)
        self.horizontalLayout_38.setSpacing(10)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
#         self.label_22 = QLabel(self.deployDateEditFrame)
#         self.label_22.setObjectName(u"label_22")

#         self.horizontalLayout_38.addWidget(self.label_22)

#         self.deployDateEdit = QDateEdit(self.deployDateEditFrame, calendarPopup=True)
#         self.deployDateEdit.setObjectName(u"deployDateEdit")
#         self.deployDateEdit.setMinimumSize(QSize(110, 0))
#         self.deployDateEdit.setStyleSheet(u"font: 15px \"Segoe UI\"; \n"
# "background-color: #21252B;\n"
# "border-radius: 7px;")

#         self.deployDateEdit.setMinimumDate(QDate(2020, 1, 1))
#         self.deployDateEdit.setMaximumDate(QDate.currentDate())
#         self.deployDateEdit.setDate(QDate.currentDate())

#         self.horizontalLayout_38.addWidget(self.deployDateEdit)


        self.horizontalLayout_36.addWidget(self.deployDateEditFrame)

        self.deployCryptoComboFrame = QFrame(self.filterFrame)
        self.deployCryptoComboFrame.setObjectName(u"deployCryptoComboFrame")
        self.deployCryptoComboFrame.setFrameShape(QFrame.NoFrame)
        self.deployCryptoComboFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.deployCryptoComboFrame)
        self.horizontalLayout_39.setSpacing(10)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.deployCryptoComboFrame)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_39.addWidget(self.label_25)

        self.deployCryptoCombo = QComboBox(self.deployCryptoComboFrame)
        self.deployCryptoCombo.setObjectName(u"deployCryptoCombo")
        self.deployCryptoCombo.setMinimumSize(QSize(145, 0))

        self.horizontalLayout_39.addWidget(self.deployCryptoCombo)


        self.horizontalLayout_36.addWidget(self.deployCryptoComboFrame)

        self.deployPriceComboFrame = QFrame(self.filterFrame)
        self.deployPriceComboFrame.setObjectName(u"deployPriceComboFrame")
        self.deployPriceComboFrame.setFrameShape(QFrame.StyledPanel)
        self.deployPriceComboFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.deployPriceComboFrame)
        self.horizontalLayout_40.setSpacing(10)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        # self.label_27 = QLabel(self.deployPriceComboFrame)
        # self.label_27.setObjectName(u"label_27")

        # self.horizontalLayout_40.addWidget(self.label_27)

        # self.deployPriceCombo = QComboBox(self.deployPriceComboFrame)
        # self.deployPriceCombo.setObjectName(u"deployPriceCombo")
        # self.deployPriceCombo.setMinimumSize(QSize(110, 0))

        # self.horizontalLayout_40.addWidget(self.deployPriceCombo)


        self.horizontalLayout_36.addWidget(self.deployPriceComboFrame)


        self.horizontalLayout_41.addWidget(self.filterFrame, 0, Qt.AlignRight)


        self.verticalLayout_71.addWidget(self.frame_5)

        self.deployPredFrame = QFrame(self.deployPredCard)
        self.deployPredFrame.setObjectName(u"deployPredFrame")
        self.deployPredFrame.setMinimumSize(QSize(0, 0))
        self.deployPredFrame.setMaximumSize(QSize(16777215, 16777215))
        self.deployPredFrame.setStyleSheet(u"border: 4px solid #41464E;\n"
"background-color: rgb(40, 44, 52);")
        self.deployPredFrame.setFrameShape(QFrame.NoFrame)
        self.deployPredFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.deployPredFrame)
        self.verticalLayout_72.setSpacing(10)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(10, 10, 10, 10)
        self.frame_71 = QFrame(self.deployPredFrame)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMaximumSize(QSize(16777215, 26))
        self.frame_71.setStyleSheet(u"border: 0;")
        self.frame_71.setFrameShape(QFrame.NoFrame)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(10, 0, 10, 0)
        self.frame_90 = QFrame(self.frame_71)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setFrameShape(QFrame.NoFrame)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_90)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_90)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 15px \"Segoe UI\"; font-weight: bold;")

        self.verticalLayout_81.addWidget(self.label_29)


        self.horizontalLayout_43.addWidget(self.frame_90)

        self.deploySliderFrame = QFrame(self.frame_71)
        self.deploySliderFrame.setObjectName(u"deploySliderFrame")
        self.deploySliderFrame.setFrameShape(QFrame.NoFrame)
        self.deploySliderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.deploySliderFrame)
        self.horizontalLayout_42.setSpacing(15)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        # self.label_28 = QLabel(self.deploySliderFrame)
        # self.label_28.setObjectName(u"label_28")

        # self.horizontalLayout_42.addWidget(self.label_28, 0, Qt.AlignVCenter)

        # self.deploySlider = QSlider(self.deploySliderFrame)
        # self.deploySlider.setObjectName(u"deploySlider")
        # self.deploySlider.setMinimumSize(QSize(185, 0))
        # self.deploySlider.setMinimum(1)
        # self.deploySlider.setMaximum(14)
        # self.deploySlider.setOrientation(Qt.Horizontal)
        # self.deploySlider.setTickPosition(QSlider.NoTicks)
        # self.deploySlider.setTickInterval(0)

        # self.horizontalLayout_42.addWidget(self.deploySlider)

        # self.deployDaysValue = QLabel(self.deploySliderFrame)
        # self.deployDaysValue.setObjectName(u"deployDaysValue")

        # self.horizontalLayout_42.addWidget(self.deployDaysValue, 0, Qt.AlignVCenter)


        self.horizontalLayout_43.addWidget(self.deploySliderFrame, 0, Qt.AlignRight)


        self.verticalLayout_72.addWidget(self.frame_71)

        self.frame_80 = QFrame(self.deployPredFrame)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setStyleSheet(u"border: 0;")
        self.frame_80.setFrameShape(QFrame.NoFrame)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_80)
        self.verticalLayout_75.setSpacing(20)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_86 = QFrame(self.frame_80)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.NoFrame)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_86)
        self.verticalLayout_83.setSpacing(5)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.deployGraphFrame = QFrame(self.frame_86)
        self.deployGraphFrame.setObjectName(u"deployGraphFrame")
        self.deployGraphFrame.setMinimumSize(QSize(636, 223))
        self.deployGraphFrame.setStyleSheet(u"border-radius: 0; background: transparent;")
        self.deployGraphFrame.setFrameShape(QFrame.NoFrame)
        self.deployGraphFrame.setFrameShadow(QFrame.Raised)

        self.deployGraph = PlotWidget(self.deployGraphFrame, axisItems={'bottom': DateAxisItem(orientation='bottom')})
        # brush = QBrush(QColor(44, 49, 58, 1))
        # brush.setStyle(Qt.NoBrush)
        self.deployGraph.setBackgroundBrush(brush)
        self.deployGraph.addLegend()

        self.verticalLayout_84 = QVBoxLayout(self.deployGraphFrame)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_84.addWidget(self.deployGraph)

        self.verticalLayout_83.addWidget(self.deployGraphFrame)

        self.deployGraphDateFrame = QFrame(self.frame_86)
        self.deployGraphDateFrame.setObjectName(u"deployGraphDateFrame")
        self.deployGraphDateFrame.setFrameShape(QFrame.NoFrame)
        self.deployGraphDateFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.deployGraphDateFrame)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(10, 0, 10, 0)
        self.deployGraphDateLabel = QLabel(self.deployGraphDateFrame)
        self.deployGraphDateLabel.setObjectName(u"deployGraphDateLabel")
        self.deployGraphDateLabel.setMinimumSize(QSize(249, 17))

        self.horizontalLayout_44.addWidget(self.deployGraphDateLabel)


        self.verticalLayout_83.addWidget(self.deployGraphDateFrame, 0, Qt.AlignRight)


        self.verticalLayout_75.addWidget(self.frame_86)

        self.deployTableFrame = QFrame(self.frame_80)
        self.deployTableFrame.setObjectName(u"deployTableFrame")
        self.deployTableFrame.setMaximumSize(QSize(16777215, 180))
        self.deployTableFrame.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #21252B;")
        self.deployTableFrame.setFrameShape(QFrame.NoFrame)
        self.deployTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.deployTableFrame)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.deployTable = QTableWidget(self.deployTableFrame)
        self.deployTable.setObjectName(u"deployTable")
        self.deployTable.setStyleSheet(u"border: none;")
        self.deployTable.setFrameShape(QFrame.NoFrame)
        self.deployTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.deployTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.deployTable.horizontalHeader().setVisible(True)
        self.deployTable.horizontalHeader().setCascadingSectionResizes(False)
        self.deployTable.horizontalHeader().setDefaultSectionSize(153)
        self.deployTable.horizontalHeader().setStretchLastSection(True)
        self.deployTable.verticalHeader().setVisible(False)
        self.deployTable.verticalHeader().setCascadingSectionResizes(False)
        self.deployTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_82.addWidget(self.deployTable)


        self.verticalLayout_75.addWidget(self.deployTableFrame)


        self.verticalLayout_72.addWidget(self.frame_80)


        self.verticalLayout_71.addWidget(self.deployPredFrame)


        self.horizontalLayout_34.addWidget(self.deployPredCard)


        self.verticalLayout_54.addWidget(self.deployContent)

        self.stackedWidget.addWidget(self.deploy)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.horizontalLayout_6.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_5.addWidget(self.contentBottom)


        self.horizontalLayout.addWidget(self.contentBox)


        self.verticalLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged.connect(self.daysValue.setNum)
        # self.deploySlider.valueChanged.connect(self.deployDaysValue.setNum)

        self.stackedWidget.setCurrentIndex(3)
        self.trainContent.setCurrentIndex(0)
        self.testContent.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"CRYPTIC", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Crypto Forecasting Tool", None))
        self.btn_dash.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btn_train.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.btn_deploy.setText(QCoreApplication.translate("MainWindow", u"Deploy", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Welcome to CRYPTIC! A system made to forecast cryptocurrency prices.", None))
        self.minimizeAppBtn.setText("")
        self.closeAppBtn.setText("")
        self.cryptocurrency.setText(QCoreApplication.translate("MainWindow", u"CRYPTOCURRENCY", None))
        self.dateEditLabel.setText(QCoreApplication.translate("MainWindow", u"FILTER DATE:", None))
        self.btn_all.setText("")
        self.btn_btc.setText("")
        self.btn_eth.setText("")
        self.btn_doge.setText("")
        self.selected_dateLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PREDICTED PRICES", None))
        # self.btn_pred_closing.setText(QCoreApplication.translate("MainWindow", u"CLOSING", None))
        # self.btn_pred_high.setText(QCoreApplication.translate("MainWindow", u"HIGH", None))
        # self.btn_pred_low.setText(QCoreApplication.translate("MainWindow", u"LOW", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DAYS:", None))
        self.daysValue.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.predictedRangeLabel.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CURRENT PRICE", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"BTC", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Bitcoin", None))
        self.btcCurrPriceLabel.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"ETH", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Ethereum", None))
        self.ethCurrPriceLabel.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"DOGE", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Dogecoin", None))
        self.dogeCurrPriceLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"HISTORY", None))
        self.btn_histo_closing.setText(QCoreApplication.translate("MainWindow", u"CLOSING", None))
        self.btn_histo_high.setText(QCoreApplication.translate("MainWindow", u"HIGH", None))
        self.btn_histo_low.setText(QCoreApplication.translate("MainWindow", u"LOW", None))
        # self.btn_0.setText(QCoreApplication.translate("MainWindow", u"1D", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"3D", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"1W", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"1M", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"1Y", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.btn_startTraining.setText(QCoreApplication.translate("MainWindow", u"START TRAINING", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"GET DATA", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.checkBox_btc.setText(QCoreApplication.translate("MainWindow", u"Bitcoin (BTC)", None))
        self.checkBox_eth.setText(QCoreApplication.translate("MainWindow", u"Ethereum (ETH)", None))
        self.checkBox_doge.setText(QCoreApplication.translate("MainWindow", u"Dogecoin (DOGE)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Time Frame", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"FROM:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"UNTIL:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.radioButton_histo.setText(QCoreApplication.translate("MainWindow", u"Historical Data", None))
        self.radioButton_histo_trends.setText(QCoreApplication.translate("MainWindow", u"Historical Data + Internet Trends", None))
        # self.checkBox_reddit.setText(QCoreApplication.translate("MainWindow", u"Reddit Volume", None))
        # self.checkBox_gtrends.setText(QCoreApplication.translate("MainWindow", u"GoogleTrends", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.btn_proceed.setText(QCoreApplication.translate("MainWindow", u"PROCEED", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"DATASET", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TEST", None))
        self.btn_viewDataAnalysis.setText(QCoreApplication.translate("MainWindow", u"VIEW DATA ANALYSIS", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"DATASET", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Time Frame", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.btn_getData.setText(QCoreApplication.translate("MainWindow", u"GET DATA", None))
        self.btn_startTesting.setText(QCoreApplication.translate("MainWindow", u"START TESTING", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"TESTING DATA...", None))
        self.testTerminal.setPlainText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"DATA ANALYSIS", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"CRYPTOCURRENCY:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"CORRELATION ANALYSIS", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"CONFUSION MATRIX", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"DEPLOY", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"DATASET", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Time Frame", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.btn_deployDeploy.setText(QCoreApplication.translate("MainWindow", u"DEPLOY", None))
        # self.label_22.setText(QCoreApplication.translate("MainWindow", u"FILTER DATE:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"CRYPTOCURRENCY:", None))
        # self.label_27.setText(QCoreApplication.translate("MainWindow", u"PRICES:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"PREDICTED PRICES", None))
        # self.label_28.setText(QCoreApplication.translate("MainWindow", u"DAYS:", None))
        # self.deployDaysValue.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.deployGraphDateLabel.setText("")

        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
    # retranslateUi