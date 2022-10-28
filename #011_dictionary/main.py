import sys
import json

from PyQt5.QtWidgets import QWidget, QApplication, QCompleter

from dictionary_ui import Ui_Form


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.init_completer()

    def init_completer(self):
        with open("data.json", "r") as f:
            self.data = json.load(f)

        words_list = self.data.keys()

        completer = QCompleter(words_list)
        self.ui.lineEdit.setCompleter(completer)

    def on_lineEdit_textChanged(self, text):

        defination = self.data.get(text)

        self.ui.listWidget.clear()

        if defination:
            for i, item in enumerate(defination):
                self.ui.listWidget.addItem(f"{i + 1}. {item}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

