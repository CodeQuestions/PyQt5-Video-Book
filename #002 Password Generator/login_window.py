from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap

from ui.login_ui import Ui_Form
from main_window import MainWindow
from sql_class import connectMySQL


class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._startPos = None
        self._endPos = None
        self._tracking = False

        self.mysql = connectMySQL()

        ## initialize QPushButtons in the login window.
        self.ui.backBtn.setFocusPolicy(Qt.NoFocus)
        self.ui.createBtn.setFocusPolicy(Qt.NoFocus)
        self.ui.exitBtn.setFocusPolicy(Qt.NoFocus)
        self.ui.registerBtn.setFocusPolicy(Qt.NoFocus)
        self.ui.loginBtn.setFocusPolicy(Qt.NoFocus)

        ## show login window when start app 
        self.ui.funcWidget.setCurrentIndex(0)

        ## hide the frame and background of the app 
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


    ## Make the window movable after hide window frame ///////////////////////////
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
    ## ============================================================================


    ## login window //////////////////////////////////////////////////////////////
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


    ## register window ///////////////////////////////////////////////////////////
    @pyqtSlot()
    def on_backBtn_clicked(self):
        """
        function for going back to login page from register page
        """
        self.ui.funcWidget.setCurrentIndex(0)

    @pyqtSlot()
    def on_loginBtn_clicked(self):
        """
        function for login app
        """
        username = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text().strip()

        ## check if input username and password.
        if not username and not password:
            self.warning_messagebox("Please input username and password")
            return

        ## Search and check the input account information in database.
        result = self.mysql.check_username(username=username)
        if result and len(result) == 1:
            if result[0]["password"] == password:
                user_id = result[0]["user_id"]
                # pass the user_id to main window and show it.
                main_window = MainWindow(user_id=user_id)
                main_window.show()
                self.close()
            else:
                self.warning_messagebox("Password is wrong. Please try again.")
                self.ui.lineEdit_2.clear()
        else:
            self.warning_messagebox("Username is wrong. Please try again.")
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()


    @pyqtSlot()
    def on_createBtn_clicked(self):
        """
        Create a login account.
        """
        user_name = self.ui.lineEdit_3.text().strip()
        password = self.ui.lineEdit_4.text().strip()

        if user_name and password:
            ## check the username if exist in database.
            result = self.mysql.check_username(username=user_name)
            if result:
                self.warning_messagebox(content="The username is already in database. Please try another one.")
            else:
                result = self.mysql.create_login_account(user_name=user_name, password=password)
                if result:
                    content = f"Something is wrong: {result}. Please try again"
                    self.warning_messagebox(content=content)
                else:
                    ## Successfully create login account. clear input and go back to login window
                    self.warning_messagebox(content="Successfully create login account.")

                    self.ui.lineEdit_3.clear()
                    self.ui.lineEdit_4.clear()
                    self.ui.funcWidget.setCurrentIndex(0)

                    ## Create default configuaration data for the new account
                    # get user_id
                    result_1 = self.mysql.check_username(username=user_name)
                    user_id = result_1[0]["user_id"]
                    result_2 = self.mysql.check_config_data(user_id=user_id)
                    if not result_2:
                        result_3 = self.mysql.create_config_data(user_id=user_id)
                        if result_3:
                            content = f"Something is wrong: {result_3}. Please create configuration data after login."
                            self.warning_messagebox(content=content)



    def warning_messagebox(self, content):
        """
        Common messagebox function
        """
        ## Create QMessageBox
        msgBox = QMessageBox(self)
        msgBox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
        msgBox.setIconPixmap(QPixmap("./static/icon/exclamation-48.ico"))
        msgBox.setWindowTitle("Warning")
        msgBox.setText(content)
        msgBox.setStandardButtons(QMessageBox.Close)

        msgBox.exec_()







