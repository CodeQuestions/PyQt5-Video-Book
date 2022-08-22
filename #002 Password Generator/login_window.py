from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap

from ui.login_ui import Ui_Form
from main_window import MainWindow


class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._startPos = None
        self._endPos = None
        self._tracking = False

        ## show login window when start app
        self.ui.funcWidget.setCurrentIndex(0)

        ## hide the frame and background of the app
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


    @pyqtSlot()
    def on_exitBtn_clicked(self):
        """
        function for exit button
        """
        msgBox = QMessageBox(self)
        msgBox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
        msgBox.setIconPixmap(QPixmap("./static/icon/question-mark-7-48.ico"))
        msgBox.setWindowTitle("Exit?")
        msgBox.setText("Are you sure to EXIT???")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        reply = msgBox.exec_()

        if reply == QMessageBox.Yes:
            self.close()
        else:
            return

    @pyqtSlot()
    def on_registerBtn_clicked(self):
        """
        function for going to register page
        """
        self.ui.funcWidget.setCurrentIndex(1)

    @pyqtSlot()
    def on_loginBtn_clicked(self):
        """
        function for login app
        """
        main_window = MainWindow()
        main_window.show()

        self.close()


    @pyqtSlot()
    def on_backBtn_clicked(self):
        """
        function for going back to login page from register page
        """
        self.ui.funcWidget.setCurrentIndex(0)

    ## TODO: make the window movable after hide window frame
    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if self._tracking:
            self._endPos = a0.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._startPos = QPoint(a0.x(), a0.y())
            self._tracking = True

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None













