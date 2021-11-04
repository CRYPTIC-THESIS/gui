# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Login_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(380, 580)
        self.login = QWidget(MainWindow)
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.login)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.login)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: 10px;\n"
"border-radius: 10px;\n"
"background-color: #21252B;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.frame)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setStyleSheet(u"/* Buttons */\n"
"QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"QPushButton:focus { border: none; outline: none; }")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 0)
        self.btn_close = QPushButton(self.contentTopBg)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(24, 24))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_close, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.content = QStackedWidget(self.frame)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"* {\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	font: 10pt \"Segoe UI\";\n"
"	background: #2C313A;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QPushButton */\n"
"#loginInput QPushButton, #signupInput QPushButton{\n"
"	font: 10pt \"Segoe UI Semibold\";\n"
"	color: rgb(33, 37, 43);\n"
"	background: #259CA5;\n"
"}\n"
"\n"
"#loginInput QPushButton:hover, #loginInput QPushButton:pressed,\n"
"#signupInput QPushButton:hover, #signupInput QPushButton:pre"
                        "ssed {\n"
"	background: #2AB7CA;\n"
"}\n"
"\n"
"#toSignup QPushButton, #toLogin QPushButton {\n"
"	color: #259CA5;\n"
"	font: 10pt \"Segoe UI BOLD\";\n"
"}\n"
"\n"
"#toSignup QPushButton:hover, #toSignup QPushButton:pressed,\n"
"#toLogin QPushButton:hover, #toLogin QPushButton:pressed {\n"
"	color: #DDDDDD;\n"
"}")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.verticalLayout_3 = QVBoxLayout(self.loginPage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(45, 26, 45, 60)
        self.loginLogo = QFrame(self.loginPage)
        self.loginLogo.setObjectName(u"loginLogo")
        self.loginLogo.setMinimumSize(QSize(0, 139))
        self.loginLogo.setStyleSheet(u"background-image: url(:/images/images/images/app-logo.png);")
        self.loginLogo.setFrameShape(QFrame.NoFrame)
        self.loginLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.loginLogo, 0, Qt.AlignTop)

        self.loginFrame = QFrame(self.loginPage)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setFrameShape(QFrame.NoFrame)
        self.loginFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.loginFrame)
        self.verticalLayout_4.setSpacing(19)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.loginFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(24)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 11pt;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.loginInput = QFrame(self.frame_4)
        self.loginInput.setObjectName(u"loginInput")
        self.loginInput.setStyleSheet(u"")
        self.loginInput.setFrameShape(QFrame.NoFrame)
        self.loginInput.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.loginInput)
        self.verticalLayout_7.setSpacing(13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.username_login = QLineEdit(self.loginInput)
        self.username_login.setObjectName(u"username_login")
        self.username_login.setMinimumSize(QSize(0, 37))

        self.verticalLayout_7.addWidget(self.username_login)

        self.pass_login = QLineEdit(self.loginInput)
        self.pass_login.setObjectName(u"pass_login")
        self.pass_login.setMinimumSize(QSize(0, 37))

        self.verticalLayout_7.addWidget(self.pass_login)

        self.btn_login = QPushButton(self.loginInput)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(0, 37))

        self.verticalLayout_7.addWidget(self.btn_login)


        self.verticalLayout_5.addWidget(self.loginInput)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.toSignup = QFrame(self.loginFrame)
        self.toSignup.setObjectName(u"toSignup")
        self.toSignup.setMaximumSize(QSize(16777215, 20))
        self.toSignup.setStyleSheet(u"")
        self.toSignup.setFrameShape(QFrame.NoFrame)
        self.toSignup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.toSignup)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(45, 0, 0, 0)
        self.label = QLabel(self.toSignup)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignRight)

        self.btn_toSignup = QPushButton(self.toSignup)
        self.btn_toSignup.setObjectName(u"btn_toSignup")
        self.btn_toSignup.setMinimumSize(QSize(0, 20))
        self.btn_toSignup.setStyleSheet(u"border: none;")

        self.horizontalLayout.addWidget(self.btn_toSignup, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.toSignup)


        self.verticalLayout_3.addWidget(self.loginFrame)

        self.content.addWidget(self.loginPage)
        self.signupPage = QWidget()
        self.signupPage.setObjectName(u"signupPage")
        self.verticalLayout_12 = QVBoxLayout(self.signupPage)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(45, 26, 45, 60)
        self.signupLogo = QFrame(self.signupPage)
        self.signupLogo.setObjectName(u"signupLogo")
        self.signupLogo.setMinimumSize(QSize(0, 139))
        self.signupLogo.setStyleSheet(u"background-image: url(:/images/images/images/app-logo.png);")
        self.signupLogo.setFrameShape(QFrame.NoFrame)
        self.signupLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.signupLogo, 0, Qt.AlignTop)

        self.signupFrame = QFrame(self.signupPage)
        self.signupFrame.setObjectName(u"signupFrame")
        self.signupFrame.setFrameShape(QFrame.NoFrame)
        self.signupFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.signupFrame)
        self.verticalLayout_8.setSpacing(19)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.signupFrame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setSpacing(24)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 11pt;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_3)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.signupInput = QFrame(self.frame_11)
        self.signupInput.setObjectName(u"signupInput")
        self.signupInput.setStyleSheet(u"")
        self.signupInput.setFrameShape(QFrame.NoFrame)
        self.signupInput.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.signupInput)
        self.verticalLayout_11.setSpacing(13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.username_signup = QLineEdit(self.signupInput)
        self.username_signup.setObjectName(u"username_signup")
        self.username_signup.setMinimumSize(QSize(0, 37))

        self.verticalLayout_11.addWidget(self.username_signup)

        self.pass_signup = QLineEdit(self.signupInput)
        self.pass_signup.setObjectName(u"pass_signup")
        self.pass_signup.setMinimumSize(QSize(0, 37))

        self.verticalLayout_11.addWidget(self.pass_signup)

        self.confirmPass = QLineEdit(self.signupInput)
        self.confirmPass.setObjectName(u"confirmPass")
        self.confirmPass.setMinimumSize(QSize(0, 37))

        self.verticalLayout_11.addWidget(self.confirmPass)

        self.btn_signup = QPushButton(self.signupInput)
        self.btn_signup.setObjectName(u"btn_signup")
        self.btn_signup.setMinimumSize(QSize(0, 37))

        self.verticalLayout_11.addWidget(self.btn_signup)


        self.verticalLayout_9.addWidget(self.signupInput)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.toLogin = QFrame(self.signupFrame)
        self.toLogin.setObjectName(u"toLogin")
        self.toLogin.setMaximumSize(QSize(16777215, 20))
        self.toLogin.setStyleSheet(u"")
        self.toLogin.setFrameShape(QFrame.NoFrame)
        self.toLogin.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.toLogin)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(37, 0, 0, 0)
        self.label_4 = QLabel(self.toLogin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4, 0, Qt.AlignRight)

        self.btn_toLogin = QPushButton(self.toLogin)
        self.btn_toLogin.setObjectName(u"btn_toLogin")
        self.btn_toLogin.setMinimumSize(QSize(0, 20))
        self.btn_toLogin.setStyleSheet(u"border: none;")

        self.horizontalLayout_3.addWidget(self.btn_toLogin, 0, Qt.AlignLeft)


        self.verticalLayout_8.addWidget(self.toLogin)


        self.verticalLayout_12.addWidget(self.signupFrame)

        self.content.addWidget(self.signupPage)

        self.verticalLayout_2.addWidget(self.content)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.login)

        self.retranslateUi(MainWindow)

        self.content.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_close.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Login to CRYPTIC", None))
        self.username_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.pass_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"No account yet?", None))
        self.btn_toSignup.setText(QCoreApplication.translate("MainWindow", u"Signup", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Signup to CRYPTIC", None))
        self.username_signup.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.pass_signup.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.confirmPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.btn_signup.setText(QCoreApplication.translate("MainWindow", u"SIGNUP", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.btn_toLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

