# Import necessary libraries for GUI creation, file handling, and system operations
import json
import os
import sys

# Import PyQt6 components for building the application's GUI
from PyQt6.QtCore import QSize, pyqtSignal, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from ui.task_ui import Ui_TaskForm
from ui.main_ui import Ui_MainWindow


# MainWindow class is the main application window
class MainWindow(QMainWindow):
    def __init__(self):    
        super().__init__()        

        # Load the main window UI from the Ui_MainWindow class.        
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)        

        # Assign UI elements to variables for easier access        
        self.list_view = self.ui.task_listView        
        self.add_btn = self.ui.add_btn        
        self.task_input = self.ui.new_task        

        self.list_model = QStandardItemModel()  # Model for the task list        
        self.init_ui()  # Initialize UI components     

        # Path to the file where tasks are stored.           
        self.task_file_path = os.path.join(os.getcwd(), "static/tasks.json")        
        self.task_list = self.get_tasks()  # Retrieve tasks from the file.        
        self.show_tasks(self.task_list)  # Display tasks in the UI.        


 
    # Initialize UI components and connect signals.F        
    def init_ui(self):    
        # Set the model for the list view and customize its appearance.        
        self.list_view.setModel(self.list_model)        
        self.list_view.setSpacing(5)        
        self.list_view.setFocusPolicy(Qt.FocusPolicy.NoFocus)        

        # Set the icon for the add button and connect its clicked signal.        
        self.add_btn.setIcon(QIcon("./static/icons/add-black.min.svg"))        
        self.add_btn.clicked.connect(self.add_new_task)   

    def add_new_task(self):
        # Add a new task based on user input.             
        new_task = self.task_input.text().strip()        
        if new_task:        
            self.task_list.append([new_task, False])            
            self.show_tasks(self.task_list)            
            self.task_input.clear()            

    def remove_item(self, position):
        # Remove the item from the model and the internal task list.        
        self.list_model.removeRow(position)        
        self.task_list.pop(position)        
        self.get_all_tasks()        
        self.show_tasks(self.task_list)  # Refresh the task list from the UI        

    def get_tasks(self):
        # Load tasks from the JSON storage file
        with open(self.task_file_path, "r") as f:        
            tasks_data_str = f.read()            
            if tasks_data_str:            
                tasks = json.loads(tasks_data_str)                
                return tasks["tasks"]                
            else:                
                return list()  # Return an empty list if the file does not exist.                

    def show_tasks(self, task_list):
        # Display tasks in the list view using custom widgets for each task.        
        self.list_model.clear()        
        if task_list:        
            for i, task in enumerate(task_list):            
                item = QStandardItem()                
                self.list_model.appendRow(item)                
                widget = Ui_TaskForm(task[0], task[1], i)                
                widget.closeClicked.connect(self.remove_item)                
                item.setSizeHint(widget.sizeHint())                
                self.list_view.setIndexWidget(self.list_model.indexFromItem(item), widget)                

    def get_all_tasks(self):
        # Update the internal task list to reflect the current state of the UI.        
        self.task_list = []        
        for row in range(self.list_model.rowCount()):        
            item = self.list_model.item(row, 0)            
            widget = self.list_view.indexWidget(item.index())            
            if isinstance(widget, Ui_TaskForm):            
                self.task_list.append([widget.get_checkbox_text(), widget.get_checkbox_state()])                

    # Save the current tasks to a JSON file when the application is closed.
    def closeEvent(self, event):    
        self.get_all_tasks()        
        with open(self.task_file_path, "w") as f:                    
            f.write(json.dumps({"tasks": self.task_list}))


# Run the application if this script is executed as the main program.        
if __name__ == "__main__":
    app = QApplication(sys.argv)    
    window = MainWindow()    
    window.show()    
    sys.exit(app.exec())    

































