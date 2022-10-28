# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dictionary.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QLineEdit,
    QListWidget, QListWidgetItem, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(356, 374)
        Form.setStyleSheet(u"#Form {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(188, 231, 215, 255), stop:1 rgba(122, 215, 255, 255));\n"
"}\n"
"\n"
"#lineEdit { \n"
"	padding: 5px 10px 5px 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#listWidget {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	alternate-background-color: #f4f4f4;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#listWidget::item {\n"
"	padding: 10px;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"")
        self.lineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet(u"")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setAutoScroll(False)
        self.listWidget.setAutoScrollMargin(1)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setWordWrap(True)

        self.verticalLayout.addWidget(self.listWidget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Dictionary", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Search...", None))
    # retranslateUi

