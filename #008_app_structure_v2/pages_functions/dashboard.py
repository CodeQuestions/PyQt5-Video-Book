from PyQt5.QtWidgets import QWidget

from ui.pages.dashboard_ui import Ui_Form


class Dashboard(QWidget):
    def __init__(self):
        super(Dashboard, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
