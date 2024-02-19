import sys
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TaskForm(QtWidgets.QWidget):
    # Signal to indicate when the task's close button is clicked.
    # An integer parameter is used to pass the position of the task in the list.
    closeClicked = QtCore.pyqtSignal(int)

    # CSS styles for checked and unchecked tasks.
    # These styles are applied based on the task's completion state.
    checked_style = "text-decoration: line-through;"
    unchecked_style = "text-decoration: none;"

    def __init__(self, text, state, position, *args, **kwargs):
        super().__init__()
        # Position of the task in the list, used for identifying tasks, especially for deletion.
        self.position = position

        # Initialize the UI components.
        self.init_ui()

        # Set the initial state and text of the task based on provided parameters.
        self.task_check_box.setText(text)
        self.task_check_box.setChecked(state)

        # Apply the appropriate style based on the initial state.
        if state:
            self.task_check_box.setStyleSheet(self.checked_style)

        # Connect signals to their corresponding slots.
        # When the task's state changes, update its style.
        self.task_check_box.stateChanged.connect(self.update_style)
        # When the remove button is clicked, emit a signal to indicate that this task should be closed.
        self.reomve_btn.clicked.connect(self.emitCloseSignal)

    def init_ui(self):
        # Set the geometry of the task widget.
        self.setGeometry(0, 0, 1000, 100)  # x, y, width, height

        # Load and apply the CSS style from a file.
        with open("./static/style_task.qss", "r") as style_file:
            style_str = style_file.read()
            self.setStyleSheet(style_str)

        # Create a grid layout for the widget.
        self.gridLayout = QtWidgets.QGridLayout(self)        
        self.gridLayout.setContentsMargins(0, 0, 0, 0)        
        self.gridLayout.setSpacing(0)        
  

        # Create the main task widget and its horizontal layout.
        self.task_widget = QtWidgets.QWidget(parent=self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.task_widget)

        # Add a checkbox for marking the task's completion state.  
        self.task_check_box = QtWidgets.QCheckBox(self.task_widget)
        self.horizontalLayout.addWidget(self.task_check_box)

        # Add a button for removing the task.
        self.reomve_btn = QtWidgets.QPushButton(self.task_widget)
        self.reomve_btn.setIcon(QtGui.QIcon("./static/icons/close.svg"))
        self.reomve_btn.setIconSize(QtCore.QSize(20, 20))
        self.horizontalLayout.addWidget(self.reomve_btn)

        # Add the task widget to the grid layout.
        self.gridLayout.addWidget(self.task_widget, 0, 0, 1, 1)

    # Update the task's visual style based on its completion state.
    def update_style(self, state):
        self.task_check_box.setStyleSheet(
            self.checked_style if state else self.unchecked_style
        )

    # Emit a signal indicating the task should be closed,
    # passing its position as an argument.
    def emitCloseSignal(self):
        self.closeClicked.emit(self.position)

    # Retrieve the current state and text of the task
    # for processing outside this class.
    def get_checkbox_state(self):
        return self.task_check_box.isChecked()

    def get_checkbox_text(self):
        return self.task_check_box.text()
