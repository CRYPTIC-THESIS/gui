# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingkXFvxM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(493, 275)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: #21252B;\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.logo = QFrame(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(16777215, 60))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.logo)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 10, 30, 0)
        self.frame_2 = QFrame(self.logo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(60, 55))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"background: url(:/images/images/images/Logo.png);\n"
"background-repeat: no reapeat;\n"
"background-position: center;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.label = QLabel(self.logo)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        # font = QFont()
        # font.setFamily(u"Segoe UI")
        # font.setPointSize(20)
        # font.setBold(True)
        # # font.setWeight(75)
        # self.label.setFont(font)
        self.label.setStyleSheet(u"color: #FFFFFF; font: 20pt \"Segoe UI\"; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.logo, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 30, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.frame_5)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(16)
        self.title.setFont(font1)
        self.title.setStyleSheet(u"color: #DDDDDD;")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.title)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 0, 20, 0)
        self.loadingBar = QProgressBar(self.frame_6)
        self.loadingBar.setObjectName(u"loadingBar")
        self.loadingBar.setMinimumSize(QSize(0, 28))
        self.loadingBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: #2C313A;\n"
"	color: #9B9D9F;\n"
"	border-style: none;\n"
"	border: 10px solid transparent; \n"
"	border-radius: 20px;\n"
"	text-align: center;\n"
"	margin-right: 12;\n"
"	\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 #2AB7CA, stop:1 #8C88BF);\n"
"}")
        self.loadingBar.setMinimum(0)
        self.loadingBar.setMaximum(1)
        self.loadingBar.setValue(1)
        self.loadingBar.setAlignment(Qt.AlignCenter)
        self.loadingBar.setTextVisible(False)
        self.loadingBar.setInvertedAppearance(False)

        self.verticalLayout_5.addWidget(self.loadingBar)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.subtitle = QLabel(self.frame_4)
        self.subtitle.setObjectName(u"subtitle")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(10)
        self.subtitle.setFont(font2)
        self.subtitle.setStyleSheet(u"color: #9B9D9F;")
        self.subtitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.subtitle)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"CRYPTIC", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"<strong>APP</strong> DESCRIPTION", None))
        self.loadingBar.setFormat("")
        self.subtitle.setText(QCoreApplication.translate("Dialog", u"Please Wait...", None))
    # retranslateUi

