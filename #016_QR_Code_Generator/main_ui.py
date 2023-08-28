# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(813, 615)
        MainWindow.setMaximumSize(QSize(813, 615))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.setting_frame = QFrame(self.centralwidget)
        self.setting_frame.setObjectName(u"setting_frame")
        self.setting_frame.setMaximumSize(QSize(301, 16777215))
        self.setting_frame.setStyleSheet(u"")
        self.setting_frame.setFrameShape(QFrame.StyledPanel)
        self.setting_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.setting_frame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.setting_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.input_frame = QFrame(self.setting_frame)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setMinimumSize(QSize(0, 50))
        self.input_frame.setMaximumSize(QSize(16777215, 80))
        self.input_frame.setStyleSheet(u"")
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.input_frame)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.textEdit = QTextEdit(self.input_frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.input_frame)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.setting_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.setting_frame)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_6 = QLabel(self.setting_frame)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setItalic(True)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"Color: grey;")

        self.verticalLayout_3.addWidget(self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSlider = QSlider(self.setting_frame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setMaximum(40)
        self.horizontalSlider.setPageStep(2)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.horizontalSlider)

        self.label_4 = QLabel(self.setting_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(15, 0))

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.setting_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_9 = QLabel(self.setting_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"Color: grey;")

        self.verticalLayout_4.addWidget(self.label_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSlider_2 = QSlider(self.setting_frame)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setStyleSheet(u"")
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setPageStep(2)
        self.horizontalSlider_2.setValue(10)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider_2)

        self.label_8 = QLabel(self.setting_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(15, 0))

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.setting_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_10)

        self.label_11 = QLabel(self.setting_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"Color: grey;")

        self.verticalLayout_5.addWidget(self.label_11)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSlider_3 = QSlider(self.setting_frame)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setStyleSheet(u"")
        self.horizontalSlider_3.setMinimum(1)
        self.horizontalSlider_3.setMaximum(40)
        self.horizontalSlider_3.setPageStep(2)
        self.horizontalSlider_3.setValue(3)
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.horizontalSlider_3)

        self.label_5 = QLabel(self.setting_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(15, 0))

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_12 = QLabel(self.setting_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_12)

        self.label_13 = QLabel(self.setting_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"Color: grey;")

        self.verticalLayout_6.addWidget(self.label_13)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.setting_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.lineEdit = QLineEdit(self.setting_frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_14 = QLabel(self.setting_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_14)

        self.label_15 = QLabel(self.setting_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"Color: grey;")

        self.verticalLayout_7.addWidget(self.label_15)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_2 = QPushButton(self.setting_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.lineEdit_2 = QLineEdit(self.setting_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.setting_frame, 0, 0, 2, 1)

        self.output_frame = QFrame(self.centralwidget)
        self.output_frame.setObjectName(u"output_frame")
        self.output_frame.setMinimumSize(QSize(500, 500))
        self.output_frame.setMaximumSize(QSize(500, 500))
        self.output_frame.setStyleSheet(u"")
        self.output_frame.setFrameShape(QFrame.StyledPanel)
        self.output_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.output_frame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.result_label = QLabel(self.output_frame)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setPixmap(QPixmap(u"result version 1.png"))
        self.result_label.setScaledContents(True)

        self.gridLayout_3.addWidget(self.result_label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.output_frame, 0, 1, 1, 1)

        self.function_frame = QFrame(self.centralwidget)
        self.function_frame.setObjectName(u"function_frame")
        self.function_frame.setMaximumSize(QSize(16777215, 100))
        self.function_frame.setFrameShape(QFrame.StyledPanel)
        self.function_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.function_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.generate_btn = QPushButton(self.function_frame)
        self.generate_btn.setObjectName(u"generate_btn")
        font3 = QFont()
        font3.setPointSize(10)
        self.generate_btn.setFont(font3)

        self.horizontalLayout_7.addWidget(self.generate_btn)

        self.save_btn = QPushButton(self.function_frame)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setFont(font3)

        self.horizontalLayout_7.addWidget(self.save_btn)


        self.gridLayout.addWidget(self.function_frame, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.horizontalSlider_2.valueChanged.connect(self.label_8.setNum)
        self.horizontalSlider_3.valueChanged.connect(self.label_5.setNum)
        self.horizontalSlider.valueChanged.connect(self.label_4.setNum)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QR Code Generator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Content of the QR Code", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"QR Code Settings ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"controls the size of the QR Code", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Box Size", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"controls how many pixels in each box", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Border Size", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"controls how many boxes thick the border should be", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Fill Color", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Painting color for the QR", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Select Color", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"#000000", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Background Color", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Background color for the QR", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Select Color", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"#ffffff", None))
        self.result_label.setText("")
        self.generate_btn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

