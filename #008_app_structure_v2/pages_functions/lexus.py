from PyQt5.QtWidgets import QWidget

from ui.pages.lexus_ui import Ui_Form


class Lexus(QWidget):
    def __init__(self):
        super(Lexus, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
