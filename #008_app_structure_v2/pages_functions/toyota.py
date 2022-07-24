from PyQt5.QtWidgets import QWidget

from ui.pages.toyota_ui import Ui_Form


class Toyota(QWidget):
    def __init__(self):
        super(Toyota, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
