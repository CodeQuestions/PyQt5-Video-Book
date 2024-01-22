import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from main_ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    # Define constants for placeholder/title text
    USERNAME = "Username"
    PASSWORD = "Password"

    def __init__(self):
        super().__init__()

        # Initialize the main window and setup UI elements
        self.app = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Group UI elements for username and password for organized access
        # Each group contains the line edit, group box, and a string for the placeholder/title
        self.username_group = (self.ui.lineEdit, self.ui.groupBox, self.USERNAME)
        self.password_group = (self.ui.lineEdit_2, self.ui.groupBox_2, self.PASSWORD)

        # Initialize UI settings
        self.init_ui()

    def init_ui(self):
        # Initially set the group box titles to empty
        self.username_group[1].setTitle("")
        self.password_group[1].setTitle("")

        # Get the instance of the application and connect the focus change event to update_content
        self.app = QtWidgets.QApplication.instance()
        self.app.focusChanged.connect(self.update_content)

    def update_content(self, old_widget, now_widget):
        # Handle focus change for both username and password groups
        self.handle_focus_change(self.username_group, old_widget, now_widget)
        self.handle_focus_change(self.password_group, old_widget, now_widget)

    @staticmethod
    def handle_focus_change(group, old_widget, now_widget):
        # Extract elements from the group tuple
        line_edit, group_box, title = group

        # Clear or set placeholders and titles based on focus change
        if old_widget == line_edit and line_edit.text().strip() == "":
            line_edit.setPlaceholderText(title)
            group_box.setTitle("")

        if now_widget == line_edit:
            line_edit.setPlaceholderText("")
            group_box.setTitle(title)

if __name__ == '__main__':
    #
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
