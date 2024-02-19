# Import necessary libraries for GUI creation, file handling, and system operations
import json  # Used for storing and retrieving task data in JSON format
import os  # Used to handle file paths
import sys  # Used for system-specific parameters and functions

# Import PyQt6 components for building the application's GUI
from PyQt6.QtCore import QSize, pyqtSignal, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import uic  # For loading UI files created with Qt Designer


# TaskItem class represents a single task in the task list
class TaskItem(QWidget):
    # Signal to indicate when the task's close button is clicked
    closeClicked = pyqtSignal(int)

    # CSS styles for checked and unchecked tasks
    checked_style = "text-decoration: line-through;"
    unchecked_style = "text-decoration: none;"

    def __init__(self, text, state, position, *args, **kwargs):
        super().__init__()
        self.position = position  # Position of the task in the list, used for deletion

        # Load the task item UI and apply task-specific styles
        self.ui = uic.loadUi("./ui/task.ui", self)
        with open("./static/style_task.qss", "r") as f:
            style_str = f.read()
            self.setStyleSheet(style_str)

        # Initialize the task checkbox with provided text and completion state
        self.task = self.ui.checkBox_3
        self.task.setText(text)
        self.task.setChecked(state)
        if state:
            self.task.setStyleSheet(self.checked_style)

        # Connect the checkbox state change to the style update method
        self.task.stateChanged.connect(self.update_style)

        # Initialize and configure the close button
        self.close_btn = self.ui.pushButton_4
        self.close_btn.setText("")  # Removing default text
        self.close_btn.setIcon(QIcon("./static/icons/close.svg"))
        self.close_btn.clicked.connect(self.emitCloseSignal)

    # Update the task's visual style based on its completion state
    def update_style(self, state):
        self.task.setStyleSheet(self.checked_style if state else self.unchecked_style)

    # Retrieve the current state and text of the task
    def get_checkbox_state(self):
        return self.task.isChecked()

    def get_checkbox_text(self):
        return self.task.text()

    # Emit a signal indicating the task should be closed, passing its position
    def emitCloseSignal(self):
        self.closeClicked.emit(self.position)


# MainWindow class is the main application window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Load the main window UI
        self.ui = uic.loadUi("./ui/main.ui", self)

        # Assign UI elements to variables for easier access
        self.list_view = self.ui.listView
        self.add_btn = self.ui.add_btn
        self.task_input = self.ui.lineEdit

        self.list_model = QStandardItemModel()  # Model for the task list
        self.init_ui()  # Initialize UI components

        self.task_file_path = os.path.join(os.getcwd(), "static/tasks.json")  # Task storage file
        self.task_list = self.get_tasks()  # Load tasks from storage
        self.show_tasks(self.task_list)  # Display tasks in the UI

    # Initialize UI components and connect signals
    def init_ui(self):
        self.list_view.setModel(self.list_model)
        self.list_view.setSpacing(5)
        self.list_view.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.add_btn.setIcon(QIcon("./static/icons/add-black.min.svg"))
        self.add_btn.clicked.connect(self.add_new_task)

    # Remove a task item from the list
    def remove_item(self, position):
        self.list_model.removeRow(position)
        self.task_list.pop(position)
        self.get_all_tasks()  # Refresh the task list from the UI
        self.show_tasks(self.task_list)

    # Load tasks from the JSON storage file
    def get_tasks(self):
        with open(self.task_file_path, "r") as f:
            tasks = json.load(f)
            return tasks["tasks"]

    # Display tasks in the list view using custom widgets
    def show_tasks(self, task_list):
        self.list_model.clear()
        for i, task in enumerate(task_list):
            item = QStandardItem()
            self.list_model.appendRow(item)
            widget = TaskItem(task[0], task[1], i)
            widget.closeClicked.connect(self.remove_item)
            item.setSizeHint(widget.sizeHint())
            self.list_view.setIndexWidget(self.list_model.indexFromItem(item), widget)

    # Add a new task based on user input
    def add_new_task(self):
        new_task = self.task_input.text().strip()
        if new_task:
            self.task_list.append([new_task, False])
            self.show_tasks(self.task_list)
            self.task_input.clear()

    # Update the task list based on the current UI state
    def get_all_tasks(self):
        self.task_list = []
        for row in range(self.list_model.rowCount()):
            item = self.list_model.item(row, 0)
            widget = self.list_view.indexWidget(item.index())
            if isinstance(widget, TaskItem):
                self.task_list.append([widget.get_checkbox_text(), widget.get_checkbox_state()])

    # Save the current tasks to a JSON file when the application is closed.
    def closeEvent(self, event):
        self.get_all_tasks()
        with open(self.task_file_path, "w") as f:
            f.write(json.dumps({"tasks": self.task_list}))


# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("./static/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())



