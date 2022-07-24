from PyQt5.QtWidgets import QWidget

from ui.pages.home_ui import Ui_Form


class Home(QWidget):
    def __init__(self):
        super(Home, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


