import random

from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, \
    QTableWidgetItem, QPushButton, QHeaderView, \
    QAbstractItemView, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QPixmap

from ui.main_window_ui import Ui_MainWindow
from sql_class import connectMySQL


class MainWindow(QMainWindow):
    def __init__(self, user_id):
        super(MainWindow, self).__init__()

        self.USER_ID = user_id
        self.mysql = connectMySQL()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## initialize widget in app
        # menu widget and main window
        self.show_pw_btn = self.ui.pushButton
        self.create_pw_btn = self.ui.pushButton_2
        self.conf_btn = self.ui.pushButton_3

        self.pages = self.ui.stackedWidget

        # show password window
        self.website_show = self.ui.lineEdit_2
        self.username_show = self.ui.lineEdit
        self.pw_table = self.ui.tableWidget

        # password generate window
        self.website_create = self.ui.lineEdit_3
        self.username_create = self.ui.lineEdit_4
        self.password_length = self.ui.spinBox
        self.uppercase_check = self.ui.checkBox
        self.numbers_check = self.ui.checkBox_2
        self.special_check = self.ui.checkBox_3
        self.new_password = self.ui.generatePWLineEdit

        # configuration window
        self.lowercase_le = self.ui.lineEdit_6
        self.uppercase_le = self.ui.lineEdit_7
        self.numbers_le = self.ui.lineEdit_8
        self.special_characters_le = self.ui.lineEdit_9

        # initialize QTableWidget
        self.pw_table.setRowCount(0)
        self.pw_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pw_table.setColumnWidth(0, 20)
        self.pw_table.setColumnWidth(1, 20)

        for i in range(2, 5):
            self.pw_table.setColumnWidth(i, 190)

        # show password list page when start app
        self.pages.setCurrentIndex(0)
        # show password list of this user when login
        self.on_showSearchBtn_clicked()

        ## connect signal and slot
        # change window
        self.show_pw_btn.toggled.connect(
            lambda: self.do_change_page(self.show_pw_btn))
        self.create_pw_btn.toggled.connect(
            lambda: self.do_change_page(self.create_pw_btn))
        self.conf_btn.toggled.connect(
            lambda: self.do_change_page(self.conf_btn))

        # search password list by condition(username and website)
        self.username_show.textChanged.connect(self.on_showSearchBtn_clicked)
        self.website_show.textChanged.connect(self.on_showSearchBtn_clicked)

    # Main window ///////////////////////////////////////////////////////////////
    @pyqtSlot()
    def on_exitBtn_clicked(self):
        """
        function for exit app
        """
        # create QMessageBox
        msgBox = QMessageBox(self)
        msgBox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
        msgBox.setIconPixmap(QPixmap("./static/icon/question-mark-7-48.ico"))
        msgBox.setWindowTitle('Exit?')
        msgBox.setText("Are you sure to EXIT?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        reply = msgBox.exec_()

        if reply == QMessageBox.Yes:
            self.close()
        else:
            return

    def do_change_page(self, btn):
        """
        function for change page
        """
        btn_text = btn.text().strip()
        if btn_text == self.show_pw_btn.text().strip():
            self.pages.setCurrentIndex(0)
            self.on_showSearchBtn_clicked()
        elif btn_text == self.create_pw_btn.text().strip():
            self.pages.setCurrentIndex(1)
        else:
            self.pages.setCurrentIndex(2)
            self.on_confRefreshBtn_clicked()

    ## functions for show password window
    @pyqtSlot()
    def on_showRefreshBtn_clicked(self):
        """
        Reset input lineEdit
        """
        self.username_show.clear()
        self.website_show.clear()

    @pyqtSlot()
    def on_showSearchBtn_clicked(self):
        """
        Function: search all the password data under this user
        """
        search_result = self.search_data()

        self.pw_table.setRowCount(0)

        if search_result:
            for index, item in enumerate(search_result):
                data = [index + 1, item['id'], item['website'], item['user_name'], item['password']]
                self.show_password_list(data=data)

    def search_data(self):
        """
        search password list from database
        """
        website = self.website_show.text().strip()
        username = self.username_show.text().strip()

        search_result = self.mysql.get_password_list(user_id=self.USER_ID,
                                                     search_username=username,
                                                     search_website=website)

        return search_result

    def show_password_list(self, data):
        """
        Show password data in QTableWidget from database
        """
        new_row_count = self.pw_table.rowCount() + 1
        self.pw_table.setRowCount(new_row_count)

        for column, row_item in enumerate(data):
            self.pw_table.setItem(new_row_count - 1, column, QTableWidgetItem(str(row_item)))

        # set a button for delete password
        self.delete_btn = QPushButton("Delete")
        self.delete_btn.setObjectName("delete")
        icon = QIcon("./static/icon/x-mark-2-128.gif")
        self.delete_btn.setIcon(icon)
        self.delete_btn.setFixedWidth(100)
        self.delete_btn.clicked.connect(self.delete)

        layout = QHBoxLayout()
        layout.addWidget(self.delete_btn)
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(layout)

        self.pw_table.setCellWidget(new_row_count - 1, 5, widget)

    def delete(self):
        """
        Delete data from QTableWidget and database
        """
        # Create QMessageBox
        msgBox = QMessageBox(self)
        msgBox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
        msgBox.setIconPixmap(QPixmap("./static/icon/question-mark-7-48.ico"))
        msgBox.setWindowTitle("Delete?")
        msgBox.setText("Are you sure to DELETE?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        reply = msgBox.exec_()
        if reply == QMessageBox.Yes:
            button = self.sender()
            row = None
            if button:
                try:
                    row = self.pw_table.indexAt(button.parent().pos()).row()
                except Exception as E:
                    content = f"Something is wrong: {E}"
                    self.warning_messagebox(context=content)
            if row >= 0:
                id = int(self.pw_table.item(row, 1).text())
                delete_result = self.mysql.delete_password_data(id=id)
                self.on_showSearchBtn_clicked()

        else:
            return

    ## Create password window
    @pyqtSlot()
    def on_generateRestBtn_clicked(self):
        """
        Function for reset button in generate window to reset window
        """
        self.website_create.clear()
        self.username_create.clear()
        self.password_length.setValue(8)
        self.uppercase_check.setChecked(False)
        self.numbers_check.setChecked(False)
        self.special_check.setChecked(False)
        self.new_password.clear()

    @pyqtSlot()
    def on_generateCreateBtn_clicked(self):
        """
        Function for create button in generate window to create a new password
        """
        # get configuration data from database
        configuration_data = self.mysql.check_config_data(user_id=self.USER_ID)
        if not configuration_data:
            self.warning_messagebox("Please go to configuration window to set configuration data.")
            return

        flag = True
        password = ""
        while flag:
            # Create new password
            password = self.create_password(configuration_data)
            # Check new password if it contains all conditions
            result = self.verify_password(password, configuration_data)
            if result == True:
                password = password
                break
            else:
                continue

        # show new password
        self.new_password.setText(password)

    @pyqtSlot()
    def on_generateCopyBtn_clicked(self):
        """
        Function for copy button in generate window to copy the new password
        """
        try:
            if self.new_password.text():
                clipboard = QApplication.clipboard()
                clipboard.setText(self.new_password.text())
                self.warning_messagebox("Copy password successfully", type="Success")
            else:
                self.warning_messagebox("Password id Empty! ")
        except Exception as E:
            self.warning_messagebox(f"Error: {E}")

    @pyqtSlot()
    def on_generateSaveBtn_clicked(self):
        website = self.website_create.text().strip()
        username = self.username_create.text().strip()
        password = self.new_password.text()
        # check if input the username , website and create the new password
        if website and username and password:
            save_result = self.mysql.save_new_password(user_id=self.USER_ID,
                                                       user_name=username,
                                                       website=website,
                                                       password=password)
            if save_result:
                self.warning_messagebox(f"Error: {save_result}")
            else:
                self.warning_messagebox("Successfully save the new password.", type="Success")
        else:
            self.warning_messagebox("Please input website and username, or create new password.")

    def create_password(self, configuration_data):
        """
        Function for creating password
        """
        new_password = ""

        characters = list(configuration_data[0]["lowercase"])
        password_length = int(self.password_length.text())

        if self.uppercase_check.isChecked() is True:
            characters.extend(configuration_data[0]["uppercase"])
        if self.numbers_check.isChecked() is True:
            characters.extend(configuration_data[0]['numbers'])
        if self.special_check.isChecked() is True:
            characters.extend(configuration_data[0]["special_characters"])

        for x in range(password_length):
            new_password += random.choice(characters)

        return new_password

    def verify_password(self, password, configuration_data):
        """
        Function for checking the new password if it contains all the conditions.
        """
        lowercase = list(configuration_data[0]['lowercase'])
        result = list(set(lowercase) & set(password))

        if not result:
            return False

        check_list = []
        if self.uppercase_check.isChecked() is True:
            check_list.append("uppercase")
        if self.numbers_check.isChecked() is True:
            check_list.append("numbers")
        if self.special_check.isChecked() is True:
            check_list.append("special_characters")

        if check_list:
            for check_item in check_list:
                characters_list = list(configuration_data[0][check_item])
                check_result = list(set(characters_list) & set(password))
                if not check_result:
                    return False

        return True

    ## configuration window
    @pyqtSlot()
    def on_confEditBtn_clicked(self):
        """
        Function for edit button in configuration window to make all the lineEdit editable
        """
        self.lowercase_le.setDisabled(False)
        self.uppercase_le.setDisabled(False)
        self.numbers_le.setDisabled(False)
        self.special_characters_le.setDisabled(False)

    @pyqtSlot()
    def on_confRefreshBtn_clicked(self):
        """
        Function for refreshing window and show the new configuration data
        """
        # search configuration data from database
        result = self.mysql.check_config_data(user_id=self.USER_ID)

        if result:
            # show all the configuration data
            self.lowercase_le.setText(result[0]['lowercase'])
            self.uppercase_le.setText(result[0]['uppercase'])
            self.numbers_le.setText(result[0]['numbers'])
            self.special_characters_le.setText(result[0]['special_characters'])
            self.set_configuration_disabled()

    @pyqtSlot()
    def on_confSaveBtn_clicked(self):
        """
        Function for save button in configuration window to save new configuration data
        """
        # get updated configuration data. if not, use placeholder text
        lowercase = self.lowercase_le.text().strip()
        if not lowercase:
            lowercase = self.lowercase_le.placeholderText()

        uppercase = self.uppercase_le.text().strip()
        if not uppercase:
            uppercase = self.uppercase_le.placeholderText()

        numbers = self.numbers_le.text().strip()
        if not numbers:
            numbers = self.numbers_le.placeholderText()

        special_characters = self.special_characters_le.text().strip()
        if not special_characters:
            special_characters = self.special_characters_le.placeholderText()

        result = self.mysql.check_config_data(user_id=self.USER_ID)
        if result:
            # if the configuration data is already in database, update it
            save_result = self.mysql.update_config_data(user_id=self.USER_ID,
                                                        lowercase=lowercase,
                                                        uppercase=uppercase,
                                                        numbers=numbers,
                                                        special_characters=special_characters)
        else:
            # if the configuration data is not in database, insert it.
            save_result = self.mysql.create_config_data(user_id=self.USER_ID,
                                                        lowercase=lowercase,
                                                        uppercase=uppercase,
                                                        numbers=numbers,
                                                        special_characters=special_characters)
        if save_result:
            self.warning_messagebox(f"Error: {save_result}")
        else:
            self.warning_messagebox("Successfully save data.", type="Success")
            # refresh window after save data
            self.on_confRefreshBtn_clicked()

    def set_configuration_disabled(self):
        self.lowercase_le.setDisabled(True)
        self.uppercase_le.setDisabled(True)
        self.numbers_le.setDisabled(True)
        self.special_characters_le.setDisabled(True)

    ## common functions
    def warning_messagebox(self, context, type=None):
        # create QMessageBox
        msgBox = QMessageBox(self)
        msgBox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
        if type == "Success":
            msgBox.setIconPixmap(QPixmap("./static/icon/check-mark-2-48.ico"))
        else:
            msgBox.setIconPixmap(QPixmap("./static/icon/exclamation-48.ico"))
        msgBox.setWindowTitle("Warning")
        msgBox.setText(context)
        msgBox.setStandardButtons(QMessageBox.Close)

        msgBox.exec_()
