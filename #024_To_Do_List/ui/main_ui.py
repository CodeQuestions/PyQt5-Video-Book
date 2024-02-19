import sys
import os
import json
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Load and apply CSS styles from a file to the main window.
        with open("./static/style.qss", "r") as style_file:
            style_str = style_file.read()
            MainWindow.setStyleSheet(style_str)

        # Set the initial size of the main window and basic properties.
        MainWindow.resize(1000, 700)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("To Do List")

        # Set the application's main window icon.
        window_icon = QtGui.QIcon("./static/icons/list.min.svg")
        MainWindow.setWindowIcon(window_icon)

        # Create and set the central widget of the main window.
        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)

        # Create the main layout for the central widget.
        self.main_verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.main_verticalLayout.setContentsMargins(80, 50, 80, 50)
        self.main_verticalLayout.setSpacing(20)
   
        # Create a frame for the title section.
        self.title_frame = QtWidgets.QFrame(parent=self.centralWidget)
        self.title_frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.title_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_frame.setObjectName("title_frame")

        # Layout for the title section, including an icon and a label.
        self.title_horizontalLayout = QtWidgets.QHBoxLayout(self.title_frame)
        self.title_horizontalLayout.setContentsMargins(10, 10, 10, 10)

        # Icon label in the title section.
        self.icon_label = QtWidgets.QLabel(parent=self.title_frame)
        self.icon_label.setMinimumSize(QtCore.QSize(40, 40))
        self.icon_label.setMaximumSize(QtCore.QSize(40, 40))
        self.icon_label.setPixmap(QtGui.QPixmap("./static/icons/list.min.svg"))
        self.icon_label.setScaledContents(True)
        self.icon_label.setObjectName("icon_label")

        # Add the icon to the title layout.
        self.title_horizontalLayout.addWidget(self.icon_label)

        # Label displaying the application's title.
        self.title_label = QtWidgets.QLabel(parent=self.title_frame)
        self.title_label.setText("To-Do List")
        self.title_label.setMinimumSize(QtCore.QSize(150, 40))
        self.title_label.setObjectName("title_label")

        # Add the title label to the title layout.
        self.title_horizontalLayout.addWidget(self.title_label)

        # Create a frame for the task list.
        self.task_frame = QtWidgets.QFrame(parent=self.centralWidget)
        self.task_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.task_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.task_frame.setObjectName("task_frame")

        # Layout for tasks within the task frame.
        self.task_verticalLayout = QtWidgets.QVBoxLayout(self.task_frame)
        self.task_verticalLayout.setContentsMargins(10, 15, 10, 15)

        # ListView for displaying tasks.
        self.task_listView = QtWidgets.QListView(parent=self.task_frame)
        self.task_listView.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.task_listView.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.task_listView.setDragDropMode(
            QtWidgets.QAbstractItemView.DragDropMode.DragOnly 
        )
        self.task_listView.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.NoSelection
        )
        self.task_listView.setMovement(QtWidgets.QListView.Movement.Free)
        self.task_listView.setObjectName("task_listView")

        # Add the task list view to the task layout.
        self.task_verticalLayout.addWidget(self.task_listView)

        # Create a frame for adding new tasks.
        self.add_task_frame = QtWidgets.QFrame(parent=self.centralWidget)
        self.add_task_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.add_task_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.add_task_frame.setObjectName("add_task_frame")

        # Layout for the "add task" section, including a text input and a button.
        self.add_horizontalLayout = QtWidgets.QHBoxLayout(self.add_task_frame)
        self.add_horizontalLayout.setContentsMargins(30, 0, 0, 0)
        self.add_horizontalLayout.setSpacing(0)

        # Text input for entering a new task.
        self.new_task = QtWidgets.QLineEdit(parent=self.add_task_frame)
        self.new_task.setObjectName("new_task")

        # Add the text input to the "add task" layout.
        self.add_horizontalLayout.addWidget(self.new_task)

        # Button for adding a new task.
        self.add_btn = QtWidgets.QPushButton(parent=self.add_task_frame)
        self.add_btn.setText("Add")
        font = QtGui.QFont()
        font.setBold(True)
        self.add_btn.setFont(font)
        self.add_btn.setIcon(QtGui.QIcon("./static/icons/add-black.min.svg"))
        self.add_btn.setIconSize(QtCore.QSize(30, 30))
        self.add_btn.setObjectName("add_btn")

        # Add the button to the "add task" layout.
        self.add_horizontalLayout.addWidget(self.add_btn)

        # Add the title, task list, and "add task" frames to the main layout.
        self.main_verticalLayout.addWidget(self.title_frame)
        self.main_verticalLayout.addWidget(self.task_frame)
        self.main_verticalLayout.addWidget(self.add_task_frame)
