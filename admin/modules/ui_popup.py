# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popupMXtHMo.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_Popup(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(380, 170)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 80))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.error_message = QLabel(self.frame_2)
        self.error_message.setObjectName(u"error_message")
        self.error_message.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        # font.setWeight(75)
        self.error_message.setFont(font)
        self.error_message.setStyleSheet(u"color: #DDDDDD;")
        self.error_message.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.error_message)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"QPushButton {\n"
"	color: #259CA5;\n"
"	font: 13px \"Segoe UI\";\n"
"	font-weight: bold;\n"
"	/* border: 2px solid rgb(52, 59, 72); */\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"	color: #DDDDDD;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	color: #DDDDDD;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ok = QPushButton(self.frame_3)
        self.ok.setObjectName(u"ok")
        self.ok.setMinimumSize(QSize(90, 30))
        self.ok.setMaximumSize(QSize(90, 30))
        self.ok.setStyleSheet(u"border: 2px solid #54B9CA;")

        self.horizontalLayout.addWidget(self.ok)

        self.cancel = QPushButton(self.frame_3)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(90, 30))
        self.cancel.setMaximumSize(QSize(90, 30))

        self.horizontalLayout.addWidget(self.cancel)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.error_message.setText(QCoreApplication.translate("Dialog", u"Error Message", None))
        self.ok.setText("")
        self.cancel.setText("")
    # retranslateUi

