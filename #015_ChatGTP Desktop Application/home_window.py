from PyQt5.QtWidgets import QWidget

from widgets.home_window_ui import Ui_Form as Home_Form


class HomeWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.home_ui = Home_Form()
        self.home_ui.setupUi(self)
