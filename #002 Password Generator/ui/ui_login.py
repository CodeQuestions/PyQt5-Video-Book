# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1227, 838)
        Form.setStyleSheet(u"/* Set style for app title widget */\n"
"#titleWidget {\n"
"	border-image: url(:/img/img/206954.jpg);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#titleWidget QLabel {\n"
"	color: rgba(255, 255, 255, 0.8);\n"
"	font-family: \"Stencil\";\n"
"}\n"
"\n"
"#titleLabel1 {\n"
"	font-size: 40px;\n"
"}\n"
"\n"
"#titleLabel2 {\n"
"	font-size: 30px;\n"
"}\n"
"\n"
"/* Set style for function widget */\n"
"#funcWidget {\n"
"	background-color: #fff;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	border-top: 2px solid #343434;\n"
"	border-right: 2px solid #343434;\n"
"	border-bottom: 2px solid #343434;\n"
"}\n"
"\n"
"/* Set style for all the QLabel in function widget */\n"
"#funcWidget QLabel {\n"
"	color: #505050;\n"
"}\n"
"\n"
"/* Set style for login label and register label in function widget */\n"
"#loginLabel, #registerLabel {\n"
"	font-family: \"Viner Hand ITC\";\n"
"	font-size: 30px;\n"
"}\n"
"\n"
"/* Set style for all the QLineEdit in functio"
                        "n widget */\n"
"#funcWidget QLineEdit {\n"
"	border: 1px solid #e5ebf0;\n"
"	border-radius: 5px;\n"
"	padding: 5px 10px;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"#funcWidget QLineEdit:focus {\n"
"	border-color: #5500ff;\n"
"}\n"
"\n"
"/* Set style for all the buttons in function widget */\n"
"#funcWidget QPushButton {\n"
"	font-size: 12em;\n"
"	border-radius: 5px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#funcWidget QPushButton:pressed {\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"/* Set style for login and create user button in function widget */\n"
"#loginBtn, #createBtn {\n"
"	background-color: #3554d1;\n"
"}\n"
"\n"
"#loginBtn:hover, #loginBtn:pressed, #createBtn:hover, #createBtn:pressed {\n"
"	background-color: #0000ff;\n"
"}\n"
"\n"
"\n"
"/* Set style for exit button in function widget */\n"
"#exitBtn {\n"
"    background-color: #d10000;\n"
"}\n"
"\n"
"#exitBtn:hover, #exitBtn:pressed {\n"
"	background-color: #910000;\n"
"}\n"
"\n"
"/* Set style for register and back button in function widget */\n"
"#registerBtn, #back"
                        "Btn {\n"
"	background-color: #55aa7f;\n"
"}\n"
"\n"
"#registerBtn:hover, #registerBtn:pressed, #backBtn:hover, #backBtn:pressed {\n"
"	background-color: #3aad00;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = QWidget(Form)
        self.titleWidget.setObjectName(u"titleWidget")
        self.titleWidget.setMinimumSize(QSize(500, 600))
        self.titleWidget.setMaximumSize(QSize(500, 600))
        self.verticalLayout_2 = QVBoxLayout(self.titleWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 224, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel1 = QLabel(self.titleWidget)
        self.titleLabel1.setObjectName(u"titleLabel1")
        self.titleLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel1)

        self.titleLabel2 = QLabel(self.titleWidget)
        self.titleLabel2.setObjectName(u"titleLabel2")
        self.titleLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 224, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.titleWidget, 0, 1, 2, 1)

        self.funcWidget = QStackedWidget(Form)
        self.funcWidget.setObjectName(u"funcWidget")
        self.funcWidget.setMinimumSize(QSize(500, 600))
        self.funcWidget.setMaximumSize(QSize(500, 600))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 129, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(79, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.loginLabel = QLabel(self.page)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setStyleSheet(u"#loginLabel {\n"
"	color: #000;\n"
"}")
        self.loginLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.loginLabel)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 0))
        self.lineEdit.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 0))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.lineEdit_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exitBtn = QPushButton(self.page)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMinimumSize(QSize(0, 30))
        icon = QIcon()
        icon.addFile(u":/icon/icon/x-mark-3-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.exitBtn)

        self.registerBtn = QPushButton(self.page)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setMinimumSize(QSize(0, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/user-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.registerBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.registerBtn)

        self.loginBtn = QPushButton(self.page)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(0, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/login-64.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.loginBtn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.loginBtn)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(79, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.funcWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_6 = QSpacerItem(20, 129, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(79, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.registerLabel = QLabel(self.page_2)
        self.registerLabel.setObjectName(u"registerLabel")
        self.registerLabel.setStyleSheet(u"#registerLabel {\n"
"	color: #000;\n"
"}")
        self.registerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.registerLabel)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_7.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(300, 0))
        self.lineEdit_3.setClearButtonEnabled(True)

        self.verticalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_8.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(300, 0))
        self.lineEdit_4.setEchoMode(QLineEdit.Normal)
        self.lineEdit_4.setClearButtonEnabled(True)

        self.verticalLayout_8.addWidget(self.lineEdit_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.backBtn = QPushButton(self.page_2)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setMinimumSize(QSize(0, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/arrow-80-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.backBtn.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.backBtn)

        self.createBtn = QPushButton(self.page_2)
        self.createBtn.setObjectName(u"createBtn")
        self.createBtn.setMinimumSize(QSize(0, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/check-mark-3-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.createBtn.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.createBtn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.gridLayout_3.addLayout(self.verticalLayout_6, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(79, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.funcWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.funcWidget, 0, 2, 2, 1)

        self.horizontalSpacer = QSpacerItem(111, 835, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(110, 835, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 2, 1)


        self.retranslateUi(Form)

        self.funcWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titleLabel1.setText(QCoreApplication.translate("Form", u"PASSWORD", None))
        self.titleLabel2.setText(QCoreApplication.translate("Form", u"MANAGEMENT AND CREATOR", None))
        self.loginLabel.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password", None))
        self.exitBtn.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.registerBtn.setText(QCoreApplication.translate("Form", u"Register", None))
        self.loginBtn.setText(QCoreApplication.translate("Form", u"Login", None))
        self.registerLabel.setText(QCoreApplication.translate("Form", u"Register", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Password", None))
        self.backBtn.setText(QCoreApplication.translate("Form", u"Back", None))
        self.createBtn.setText(QCoreApplication.translate("Form", u"Create", None))
    # retranslateUi

