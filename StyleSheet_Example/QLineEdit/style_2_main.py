import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtGui import QIcon, QAction

from style_2_main_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.username_le = self.ui.lineEdit
        self.password_le = self.ui.lineEdit_2

        self.username_le.addAction(QIcon("static/businessman-24.ico"), QLineEdit.ActionPosition.LeadingPosition)
        self.password_le.addAction(QIcon("static/key-24.ico"), QLineEdit.ActionPosition.LeadingPosition)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
