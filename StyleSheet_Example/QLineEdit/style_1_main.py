import sys

from PyQt6.QtWidgets import QApplication, QMainWindow,QLineEdit
from PyQt6.QtGui import QIcon, QAction

from style_1_main_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.username_label = self.ui.label_2
        self.password_label = self.ui.label_3

        self.username_label.setText("")
        self.password_label.setText("")

        self.username_input = self.ui.lineEdit
        self.password_input = self.ui.lineEdit_2

        # Set placeholder text for QLineEdit
        self.username_input.setPlaceholderText("Username")
        self.password_input.setPlaceholderText("Password")

        # Set echo mode for QLineEdit
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Set clear button for QLineEdit
        self.username_input.setClearButtonEnabled(True)
        self.password_input.setClearButtonEnabled(True)

        # Change default icon of clear button
        icon = QIcon("static/cross-script.png")
        self.username_input.findChildren(QAction)[0].setIcon(icon)
        self.password_input.findChildren(QAction)[0].setIcon(icon)

        # show label when QLineEdit text changed
        self.username_input.textChanged.connect(self.do_username_label)
        self.password_input.textChanged.connect(self.do_password_label)


    def do_username_label(self, text):
        if text:
            self.username_label.setText("Username")
        else:
            self.username_label.setText("")

    def do_password_label(self, text):
        if text:
            self.password_label.setText("Password")
        else:
            self.password_label.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())




















