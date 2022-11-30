# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1144, 593)
        icon = QIcon()
        icon.addFile(u":/icon/icon/key-6-128.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#logoFrame {\n"
"	image: url(:/icon/icon/key-48.ico);\n"
"	border-bottom: 1px solid #fff;\n"
"}\n"
"\n"
"/* Style for menu widget  */\n"
"#menuWidget {\n"
"	background-color: #353535;\n"
"}\n"
"\n"
"/* Style for QPushButton in menu widget  */\n"
"#menuWidget QPushButton {\n"
"	text-align: left;\n"
"	padding-left: 15px;\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	font-size: 14px;\n"
"	border: 5px solid #353535;\n"
"	height: 25px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"#menuWidget QPushButton:hover {\n"
"	background-color: #e3e3e3;\n"
"}\n"
"\n"
"\n"
"#menuWidget QPushButton:checked {\n"
"	background-color: #0055ff;\n"
"	color: #fff;\n"
"}\n"
"\n"
"/* Style for main widget */\n"
"#stackedWidget {\n"
"	background-color: #f4f5f8;\n"
"}\n"
"\n"
"/* Style for QLabel in main widget */\n"
"#stackedWidget QLabel {\n"
"	font-size: 14px;\n"
"	font-family: \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"/* Style for QLineEdit and QSpinBox in main widget */\n"
"#stackedWidget QLineEdit, #stackedWidget QSpinBox {\n"
"	borde"
                        "r: 1px solid #353535;\n"
"	border-radius: 3px;\n"
"	padding: 5px 10px;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"/* style for  QSpinBox*/\n"
"#stackedWidget QSpinBox::up-arrow {\n"
"	image: url(:/icon/icon/arrow-146-48.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"#stackedWidget QSpinBox::down-arrow {\n"
"	image: url(:/icon/icon/arrow-208-48.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"#stackedWidget QSpinBox::down-button, \n"
"#stackedWidget QSpinBox::up-button {\n"
"	border: none;\n"
"	width: 30px;\n"
"}\n"
"\n"
"#stackedWidget QSpinBox::down-button:hover, \n"
"#stackedWidget QSpinBox::up-button:hover {\n"
"	background-color: rgb(176, 176, 176);\n"
"}\n"
"\n"
"#stackedWidget QSpinBox::down-button:pressed, \n"
"#stackedWidget QSpinBox::up-button:pressed {\n"
"	background-color: rgb(78, 88, 121);\n"
"}\n"
"\n"
"/* Style for QPushButton in main widget */\n"
"#stackedWidget QPushButton {\n"
"	border: none;\n"
"	font-size: 16px;\n"
"	border-radius: 3px;\n"
"	color: #fff;\n"
"	paddi"
                        "ng: 5px 10px;\n"
"}\n"
"\n"
"#stackedWidget QPushButton:pressed {\n"
"    padding-left: 20px;\n"
"}\n"
"\n"
"/* Style for sepcial QPushButton in main widget */\n"
"#confEditBtn,\n"
"#generateCopyBtn, \n"
"#generateRestBtn,\n"
"#showSearchBtn\n"
"{\n"
"	background-color: #3554d1;\n"
"}\n"
"\n"
"#confEditBtn:hover, #confEditBtn:pressed, \n"
"#generateCopyBtn:hover,  #generateCopyBtn:pressed, \n"
"#generateRestBtn:hover,  #generateRestBtn:pressed, \n"
"#showSearchBtn:hover,  #showSearchBtn:pressed \n"
"{\n"
"	background-color: #0000ff;\n"
"}\n"
"\n"
"#confSaveBtn,\n"
"#generateSaveBtn, \n"
"#generateCreateBtn\n"
"{\n"
"    background-color: #00aa7f;\n"
"}\n"
"\n"
"#confSaveBtn:hover, #confSaveBtn:pressed, \n"
"#generateSaveBtn:hover, #generateSaveBtn:pressed,\n"
"#generateCreateBtn:hover, #generateCreateBtn:pressed \n"
"{\n"
"	background-color: #00aa00;\n"
"}\n"
"\n"
"#confRefreshBtn,\n"
" #showRefreshBtn\n"
"{\n"
"    background-color: #E59866;\n"
"}\n"
"\n"
"\n"
"#confRefreshBtn:hover, #confRefreshBtn:pressed, "
                        "\n"
"#showRefreshBtn:hover, #showRefreshBtn:pressed\n"
"{\n"
"	background-color: #DC7633;\n"
"}\n"
"\n"
"/* Style for QCheckBox in main widget */\n"
"QCheckBox {\n"
"	spacing: 10px;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	image: url(:/icon/icon/checkbox_unchecked.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/icon/icon/checkbox_checked.ico);\n"
"}\n"
"\n"
"\n"
"/* Style for QFrame */\n"
"#resultFrame {\n"
"	border-radius: 5px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"/* Style for QTableWidget */\n"
"#tableWidget QHeaderView, #tableWidget   {\n"
"	border:0px;\n"
"	background-color:  #fff;\n"
"	border-radius:5px;\n"
"	text-align:left;\n"
"}\n"
"\n"
"#tableWidget QHeaderView::section{\n"
"	font-family:\"Times New Roman\", \"Times\", \"serif\";\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	text-align:left;\n"
"	border-radius:14px;\n"
"	border-bottom:1px solid #353535;\n"
""
                        "	border-top:1px solid #353535;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"#tableWidget::item:selected {\n"
"	background-color: #55aaff;\n"
"}\n"
"\n"
"#tableWidget::item{\n"
"	border-bottom:1px solid #d0c6ff;\n"
"	padding-left: 10px;\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.menuWidget = QWidget(self.centralwidget)
        self.menuWidget.setObjectName(u"menuWidget")
        self.menuWidget.setMinimumSize(QSize(200, 0))
        self.menuWidget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.menuWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.logoFrame = QFrame(self.menuWidget)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setMinimumSize(QSize(0, 50))
        self.logoFrame.setMaximumSize(QSize(16777215, 50))
        self.logoFrame.setFrameShape(QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.logoFrame)

        self.pushButton = QPushButton(self.menuWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setMaximumSize(QSize(16777215, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/key-4-128.gif", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icon/icon/key-4-48-checked.ico", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.menuWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        self.pushButton_2.setMaximumSize(QSize(16777215, 35))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/generic-text-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon/icon/generic-text-48-checked.ico", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.menuWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setMaximumSize(QSize(16777215, 35))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/data-configuration-128.gif", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon/icon/data-configuratio-checkedn-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 574, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.exitBtn = QPushButton(self.menuWidget)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMinimumSize(QSize(0, 40))
        self.exitBtn.setMaximumSize(QSize(16777215, 35))
        self.exitBtn.setStyleSheet(u"#exitBtn {\n"
"	color: #943e3e;\n"
"	text-align: center;\n"
"	padding-left: 0;\n"
"}\n"
"\n"
"#exitBtn:pressed {\n"
"	padding-left: 10px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/logout-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.exitBtn.setIcon(icon4)

        self.verticalLayout.addWidget(self.exitBtn)


        self.gridLayout.addWidget(self.menuWidget, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(15)
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.showRefreshBtn = QPushButton(self.page)
        self.showRefreshBtn.setObjectName(u"showRefreshBtn")
        self.showRefreshBtn.setMinimumSize(QSize(150, 30))
        self.showRefreshBtn.setMaximumSize(QSize(150, 32))
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/redo-5-128.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.showRefreshBtn.setIcon(icon5)

        self.gridLayout_3.addWidget(self.showRefreshBtn, 0, 2, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.showSearchBtn = QPushButton(self.page)
        self.showSearchBtn.setObjectName(u"showSearchBtn")
        self.showSearchBtn.setMinimumSize(QSize(150, 30))
        self.showSearchBtn.setMaximumSize(QSize(150, 32))
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/search-7-128.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.showSearchBtn.setIcon(icon6)

        self.gridLayout_3.addWidget(self.showSearchBtn, 1, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.resultFrame = QFrame(self.page)
        self.resultFrame.setObjectName(u"resultFrame")
        self.resultFrame.setFrameShape(QFrame.StyledPanel)
        self.resultFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.resultFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(self.resultFrame)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.NoPen)
        self.tableWidget.setRowCount(2)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.resultFrame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(20)
        self.gridLayout_6.setContentsMargins(100, 50, 100, -1)
        self.generateRestBtn = QPushButton(self.page_2)
        self.generateRestBtn.setObjectName(u"generateRestBtn")
        self.generateRestBtn.setMinimumSize(QSize(0, 32))
        self.generateRestBtn.setMaximumSize(QSize(16777215, 32))
        self.generateRestBtn.setIcon(icon5)

        self.gridLayout_6.addWidget(self.generateRestBtn, 2, 0, 1, 1)

        self.generateCopyBtn = QPushButton(self.page_2)
        self.generateCopyBtn.setObjectName(u"generateCopyBtn")
        self.generateCopyBtn.setMinimumSize(QSize(0, 32))
        self.generateCopyBtn.setMaximumSize(QSize(16777215, 32))
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/copy-128.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.generateCopyBtn.setIcon(icon7)

        self.gridLayout_6.addWidget(self.generateCopyBtn, 4, 0, 1, 1)

        self.generatePWLineEdit = QLineEdit(self.page_2)
        self.generatePWLineEdit.setObjectName(u"generatePWLineEdit")
        self.generatePWLineEdit.setStyleSheet(u"#generatePWLineEdit {\n"
"	background-color: #fff;\n"
"	font-size: 30px;\n"
"	border: none;\n"
"}")
        self.generatePWLineEdit.setAlignment(Qt.AlignCenter)
        self.generatePWLineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.generatePWLineEdit, 3, 0, 1, 2)

        self.generateCreateBtn = QPushButton(self.page_2)
        self.generateCreateBtn.setObjectName(u"generateCreateBtn")
        self.generateCreateBtn.setMinimumSize(QSize(0, 32))
        self.generateCreateBtn.setMaximumSize(QSize(16777215, 32))
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/pressure-128.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.generateCreateBtn.setIcon(icon8)

        self.gridLayout_6.addWidget(self.generateCreateBtn, 2, 1, 1, 1)

        self.generateSaveBtn = QPushButton(self.page_2)
        self.generateSaveBtn.setObjectName(u"generateSaveBtn")
        self.generateSaveBtn.setMinimumSize(QSize(0, 32))
        self.generateSaveBtn.setMaximumSize(QSize(16777215, 32))
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/save-128.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.generateSaveBtn.setIcon(icon9)

        self.gridLayout_6.addWidget(self.generateSaveBtn, 4, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox = QCheckBox(self.page_2)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.page_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.page_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout.addWidget(self.checkBox_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_6.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(15)
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_5.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 2, 0, 1, 1)

        self.spinBox = QSpinBox(self.page_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(8)

        self.gridLayout_5.addWidget(self.spinBox, 2, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(744, 426, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 5, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_8 = QGridLayout(self.page_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setVerticalSpacing(20)
        self.gridLayout_8.setContentsMargins(100, 50, 100, -1)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(10)
        self.gridLayout_7.setVerticalSpacing(20)
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.page_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_7.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.page_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_7.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 2, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.page_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_7.addWidget(self.lineEdit_8, 2, 1, 1, 1)

        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 3, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.page_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_7.addWidget(self.lineEdit_9, 3, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 3)

        self.confEditBtn = QPushButton(self.page_3)
        self.confEditBtn.setObjectName(u"confEditBtn")
        self.confEditBtn.setMinimumSize(QSize(0, 32))
        self.confEditBtn.setMaximumSize(QSize(16777215, 32))
        icon10 = QIcon()
        icon10.addFile(u":/icon/icon/edit-property-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.confEditBtn.setIcon(icon10)

        self.gridLayout_8.addWidget(self.confEditBtn, 1, 0, 1, 1)

        self.confRefreshBtn = QPushButton(self.page_3)
        self.confRefreshBtn.setObjectName(u"confRefreshBtn")
        self.confRefreshBtn.setMinimumSize(QSize(0, 32))
        self.confRefreshBtn.setMaximumSize(QSize(16777215, 32))
        self.confRefreshBtn.setIcon(icon5)

        self.gridLayout_8.addWidget(self.confRefreshBtn, 1, 1, 1, 1)

        self.confSaveBtn = QPushButton(self.page_3)
        self.confSaveBtn.setObjectName(u"confSaveBtn")
        self.confSaveBtn.setMinimumSize(QSize(0, 32))
        self.confSaveBtn.setMaximumSize(QSize(16777215, 32))
        self.confSaveBtn.setIcon(icon9)

        self.gridLayout_8.addWidget(self.confSaveBtn, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 508, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Creator", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Password Saved", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.showRefreshBtn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.showSearchBtn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Website", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Operation", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"2", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.generateRestBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.generateCopyBtn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.generatePWLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.generateCreateBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.generateSaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Uppercase", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Special Characters", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Lowercase", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"abcdefghijklmnopqrstuvwxyz", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Uppercase", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ABCDEFGHIJKLMNOPQRSTUVWXYZ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234567890", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Special Characters", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"@#$%&^!", None))
        self.confEditBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.confRefreshBtn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.confSaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

