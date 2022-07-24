from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.main_window_ui import Ui_MainWindow

from pages_functions.home import Home
from pages_functions.dashboard import Dashboard
from pages_functions.lexus import Lexus
from pages_functions.mazda import Mazda
from pages_functions.toyota import Toyota
from pages_functions.tumbr import Tumbr
from pages_functions.youtube import Youtube


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## =======================================================================================================
        ## Get all the objects in windows
        ## =======================================================================================================
        self.home_btn = self.ui.pushButton
        self.dashboard_btn = self.ui.pushButton_2
        self.toyota_btn = self.ui.pushButton_3
        self.lexus_btn = self.ui.pushButton_4
        self.mazda_btn = self.ui.pushButton_5
        self.youtube_btn = self.ui.pushButton_6
        self.tumbr_btn = self.ui.pushButton_7

        ## =======================================================================================================
        ## Create dict for menu buttons and tab windows
        ## =======================================================================================================
        self.menu_btns_list = {
            self.home_btn: Home(),
            self.dashboard_btn: Dashboard(),
            self.toyota_btn: Toyota(),
            self.lexus_btn: Lexus(),
            self.mazda_btn: Mazda(),
            self.youtube_btn: Youtube(),
            self.tumbr_btn: Tumbr(),
        }

        ## =======================================================================================================
        ## Show home window when start app
        ## =======================================================================================================
        self.show_home_window()

        ## =======================================================================================================
        ## Connect signal and slot
        ## =======================================================================================================
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.home_btn.clicked.connect(self.show_selected_window)
        self.dashboard_btn.clicked.connect(self.show_selected_window)
        self.toyota_btn.clicked.connect(self.show_selected_window)
        self.lexus_btn.clicked.connect(self.show_selected_window)
        self.mazda_btn.clicked.connect(self.show_selected_window)
        self.youtube_btn.clicked.connect(self.show_selected_window)
        self.tumbr_btn.clicked.connect(self.show_selected_window)

    def show_home_window(self):
        """
        Function for showing home window
        :return:
        """
        result = self.open_tab_flag(self.home_btn.text())
        self.set_btn_checked(self.home_btn)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = self.home_btn.text()
            curIndex = self.ui.tabWidget.addTab(Home(), title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def show_selected_window(self):
        """
        Function for showing selected window
        :return:
        """
        button = self.sender()

        result = self.open_tab_flag(button.text())
        self.set_btn_checked(button)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = button.text()
            curIndex = self.ui.tabWidget.addTab(self.menu_btns_list[button], title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def close_tab(self, index):
        """
        Function for close tab in tabWidget
        :param index: index of tab
        :return:
        """
        self.ui.tabWidget.removeTab(index)

        if self.ui.tabWidget.count() == 0:
            self.ui.toolBox.setCurrentIndex(0)
            self.show_home_window()

    def open_tab_flag(self, tab):
        """
        Check if selected window showed or not
        :param tab: tab title
        :return: bool and index
        """
        open_tab_count = self.ui.tabWidget.count()

        for i in range(open_tab_count):
            tab_name = self.ui.tabWidget.tabText(i)
            if tab_name == tab:
                return True, i
            else:
                continue

        return False,

    def set_btn_checked(self, btn):
        """
        Set the status of selected button checked and set other buttons' status unchecked
        :param btn: button object
        :return:
        """
        for button in self.menu_btns_list.keys():
            if button != btn:
                button.setChecked(False)
            else:
                button.setChecked(True)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())
