import sys
import time
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QProgressBar
from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot


class TaskThread(QThread):
    # Using class variables for signals to avoid re-creating them in each instance
    started = pyqtSignal(str)         # Signal emitted when a task starts
    progress_value = pyqtSignal(int)  # Signal for updating progress value
    progress_text = pyqtSignal(str)   # Signal for updating progress text
    finished = pyqtSignal(str)        # Signal emitted when a task finishes

    def __init__(self, task_id=1, sleep_time=0.5):
        super().__init__()
        self.task_id = task_id
        self.sleep_time = sleep_time

    def run(self):
        # Emit signal to notify the start of the task
        self.started.emit(f"Task {self.task_id} **** START.")

        # Simulate work by updating progress signals
        for i in range(100):
            time.sleep(self.sleep_time)
            self.progress_value.emit(i + 1)
            self.progress_text.emit(f"Task {self.task_id} >>> {i + 1}")

        # Emit signal to notify the completion of the task
        self.finished.emit(f"Task {self.task_id} **** END.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI from the .ui file
        self.ui = uic.loadUi('main.ui', self)

        # Dictionary to store task threads
        self.threads = {}

        # Initialize progress bars
        self.progress_bars = [
            self.ui.progressBar,
            self.ui.progressBar_2,
            self.ui.progressBar_3
        ]

        for progress_bar in self.progress_bars:
            progress_bar.setMaximum(100)
            progress_bar.setMinimum(0)
            progress_bar.setValue(0)

        # Initialize start buttons
        self.start_buttons = [
            self.ui.pushButton,
            self.ui.pushButton_2,
            self.ui.pushButton_3
        ]

        self.sleep_times = [1, 0.1, 0.5]

        # Connect signals and slots
        self.init_signal_slot()

    # Connect signals and slots for button clicks
    def init_signal_slot(self):
        for i, start_button in enumerate(self.start_buttons, start=1):
            # Use lambda to capture the index, making it available in the signal handler
            start_button.clicked.connect(lambda _, idx=i: self.start_task(idx))

    # Update status in the list widget
    def update_status(self, text):
        self.ui.listWidget.addItem(text)

    # Update progress in the corresponding progress bar
    def update_progress(self, value, task_id):
        self.progress_bars[task_id - 1].setValue(value)

    # Toggle the state of the start button based on the task state
    def toggle_button(self, task_id, enable=True):
        self.start_buttons[task_id - 1].setDisabled(not enable)

    # Method to start a task
    def start_task(self, task_id):
        sleep_time = self.sleep_times[task_id - 1]
        # Create a TaskThread instance for the selected task
        thread = TaskThread(task_id=task_id, sleep_time=sleep_time)

        # Connect signals and slots for the task
        thread.started.connect(self.update_status)
        thread.started.connect(lambda: self.toggle_button(task_id, enable=False))
        thread.progress_value.connect(lambda value: self.update_progress(value, task_id))
        thread.progress_text.connect(self.update_status)
        thread.finished.connect(self.update_status)
        thread.finished.connect(lambda: self.toggle_button(task_id, enable=True))

        # Store the thread in the dictionary and start it
        self.threads[task_id] = thread
        thread.start()


# Application entry point
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.show()

    # Start the application event loop
    sys.exit(app.exec())






