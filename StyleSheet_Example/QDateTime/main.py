import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, Qt, QEvent, pyqtSignal, QDateTime

# Assuming Ui_MainWindow and Ui_Form are your custom UI classes
from main_ui import Ui_MainWindow
from dropdown_ui import Ui_Dialog


class DropDown(QDialog):
    # Signal emitted when date and time are changed in the dropdown
    dateTimeChanged_str = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Ensure only one of the buttons can be checked at a time
        self.ui.pm_btn.setAutoExclusive(True)
        self.ui.am_btn.setAutoExclusive(True)

        # Set initial selection in the list widgets
        self.ui.listWidget.setCurrentRow(0)
        self.ui.listWidget_2.setCurrentRow(1)

        # Connect signals of UI elements to custom methods
        self.ui.calendarWidget.selectionChanged.connect(self.emit_signal)
        self.ui.listWidget.itemSelectionChanged.connect(self.emit_signal)
        self.ui.listWidget_2.itemSelectionChanged.connect(self.emit_signal)
        self.ui.pm_btn.clicked.connect(self.emit_signal)
        self.ui.am_btn.clicked.connect(self.emit_signal)

    def emit_signal(self):
        # Get selected date, time, and AM/PM from UI elements
        date = self.ui.calendarWidget.selectedDate()
        time_hour = self.ui.listWidget.currentItem().text()
        time_min = self.ui.listWidget_2.currentItem().text()

        # Determine if it's AM or PM
        pm_am_str = "PM" if self.ui.pm_btn.isChecked() else "AM"

        # Emit signal with formatted date and time
        self.dateTimeChanged_str.emit(f"{date.month()},{date.day()},{date.year()},{time_hour},{time_min},{pm_am_str}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dropdown = DropDown()

        # Setup appearance and behavior of the date time edit field
        self.date_time = self.ui.dateTimeEdit_2
        self.date_time.setMinimumWidth(250)
        font = QFont()
        font.setPointSize(14)
        self.date_time.setFont(font)

        # Setup calendar button appearance and behavior
        self.calendar_btn = self.ui.pushButton
        self.calendar_btn.setText("")
        self.calendar_btn.setIcon(QIcon("./calendar.svg"))
        self.calendar_btn.setIconSize(QSize(40, 40))
        self.calendar_btn.setCheckable(True)
        self.calendar_btn.setChecked(False)
        self.calendar_btn.clicked.connect(self.open_dropdown)

        self.date_time_frame = self.ui.frame
        self.dropdown.installEventFilter(self)

        # Connect dropdown signal to method that updates date time edit field
        self.dropdown.dateTimeChanged_str.connect(self.set_new_date_time)

    def set_new_date_time(self, date_str):
        # Extract date and time components from the formatted string
        data_list = date_str.split(",")

        am_pm_str = data_list.pop()

        month, day, year, hour, minute = map(int, data_list)

        # Adjust hour for PM
        if am_pm_str == "PM":
            hour += 12

        # Create QDateTime object and set it to the date time edit field
        date_time = QDateTime(year, month, day, hour, minute)
        self.date_time.setDateTime(date_time)

    def open_dropdown(self, state):
        if state and not self.dropdown.isVisible():
            # Position the dropdown below the date time edit field
            self.dropdown.move(self.pos().x() + self.date_time_frame.pos().x(),
                               self.pos().y() + self.date_time_frame.pos().y() + self.date_time_frame.height() + 40)
            self.dropdown.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            self.dropdown.show()
        else:
            self.dropdown.close()

    def closeEvent(self, event):
        # Close the dropdown when the main window is closed
        self.dropdown.close()

    def eventFilter(self, obj, event):
        # Close the dropdown if it loses focus
        if self.calendar_btn.isChecked() and obj == self.dropdown and event.type() == QEvent.WindowDeactivate:
            self.dropdown.close()
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
