from PyQt5.QtWidgets import QWidget

from ui.pages.tumbr_ui import Ui_Form


class Tumbr(QWidget):
    def __init__(self):
        super(Tumbr, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
