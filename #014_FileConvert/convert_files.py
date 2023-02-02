import os
import sys
import subprocess

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QListWidgetItem, QListView
from PyQt5.QtCore import pyqtSlot, QSize, QStringListModel
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem

from convert_files_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## datas for commands and command versions /////////////////////////////
        self.commands = {
            "PyQt5": ["pyuic5", "pyrcc5"],
            "PyQt6": ["pyuic6", ""],
            "PySide2": ["pyside2-uic", "pyside2-rcc"],
            "PySide6": ["pyside6-uic", "pyside6-rcc"],
        }

        ## Get all objects on the window /////////////////////////////////////
        self.folder_path = self.ui.lineEdit
        self.version = self.ui.comboBox
        self.ui_file = self.ui.checkBox
        self.resource_file = self.ui.checkBox_2
        self.select_btn = self.ui.pushButton
        self.reset_btn = self.ui.pushButton_3
        self.start_btn = self.ui.pushButton_4

        self.warning_label = self.ui.label
        self.warning_frame = self.ui.warning_frame

        ## Hide the warning frame when start application /////////////////////
        self.warning_frame.hide()

        ## Create signal and slot when start application /////////////////////
        self.init_signal_slot()

    def init_signal_slot(self):
        """
            Create signal and slot for objects
        """
        self.select_btn.clicked.connect(self.get_folder_path)
        self.start_btn.clicked.connect(self.start_convert)
        self.reset_btn.clicked.connect(self.reset_settings)

        self.folder_path.textChanged.connect(self.hide_warning_frame)
        self.ui_file.stateChanged.connect(self.hide_warning_frame)
        self.resource_file.stateChanged.connect(self.hide_warning_frame)

    def on_comboBox_currentTextChanged(self, text):
        """
            Hide convert resource file selection when the version is PyQt6
        """
        self.hide_warning_frame()

        if text == "PyQt6":
            self.resource_file.hide()
            self.resource_file.setChecked(False)
        else:
            self.resource_file.show()

    def get_folder_path(self):
        """
            Get folder path by QFileDialog and show it on the window
        """
        self.hide_warning_frame()

        folder_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.folder_path.setText(folder_path)

    def start_convert(self):
        """
            Function for converting files type
        """

        folder_path = self.folder_path.text().strip()
        version = self.version.currentText()

        self.hide_warning_frame()

        if folder_path and version in self.commands.keys():

            result_dict = {}  # dictionary for save result data

            ## Get command for special version ///////////////////////////////////////////
            ui_command = self.commands.get(version)[0]
            rc_command = self.commands.get(version)[1]

            try:
                ## Traverse all files and folders in the specified directory ////////////
                file_list = os.walk(folder_path)
                for root, dirs, files in file_list:
                    for file in files:
                        file_path = os.path.join(root, file)

                        if file.endswith(".ui") and self.ui_file.isChecked():
                            ## Create cmd command.
                            target_file_name = file_path.replace(".ui", "_ui.py")
                            batcmd = f"{ui_command} {file_path} -o {target_file_name}"

                            os.system(batcmd)
                            result = subprocess.getoutput(batcmd)

                        elif file.endswith(".qrc") and self.resource_file.isChecked():
                            ## Create cmd command.
                            target_file_name = file_path.replace(".qrc", "_rc.py")
                            batcmd = f"{rc_command} {file_path} -o {target_file_name}"

                            os.system(batcmd)
                            result = subprocess.getoutput(batcmd)
                        else:
                            continue

                        if result:
                            result_dict[file_path] = False

                            ## Show error message.
                            self.warning_frame.show()
                            self.warning_label.setText(result)
                        else:
                            result_dict[file_path] = True

                if result_dict:
                    # Set the icon mode, the icon will be at the top of text
                    # self.ui.listView.setViewMode(QListView.IconMode)

                    ## Show result data after complete converting files.
                    model = QStandardItemModel()
                    self.ui.listView.setModel(model)

                    self.ui.listView.setIconSize(QSize(15, 15))

                    for key, value in result_dict.items():
                        key = key.replace("\\", "/")
                        if value:
                            item = QStandardItem(QIcon(":/icons/static/check-mark-3-64 #1EBB2E.ico"), key)
                        else:
                            item = QStandardItem(QIcon(":/icons/static/alert-64.ico"), key)
                        model.appendRow(item)
                    self.ui.result_count.setText(f"Total Files: {len(result_dict)}")

            except Exception as E:
                print(E)

        else:
            QMessageBox.information(self, "Warning", "Please input folder path and version.")

    def reset_settings(self):
        """
            Reset all the settings on the window.
        """
        self.hide_warning_frame()
        self.folder_path.clear()
        self.version.setCurrentIndex(0)
        self.ui_file.setChecked(False)
        self.resource_file.setChecked(False)

    def hide_warning_frame(self):
        """
            Hide warning frame and reset result data.
        """
        self.warning_frame.hide()
        self.ui.result_count.clear()

        model = self.ui.listView.model()
        if model:
            model.removeRows(0, model.rowCount())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
