import requests
import json
import sys
import pandas as pd

from PyQt6 import QtWidgets, QtCore, QtGui, uic


# Thread class for asynchronously loading nationality flags
class TaskThread(QtCore.QThread):
    # Constructor to initialize the thread with the target combobox and a list of flag URLs
    def __init__(self, obj, flag_url_list):
        super().__init__()
        self.obj = obj
        self.flag_url_list = flag_url_list

    # Run method that will be executed when the thread starts
    def run(self):
        # Iterate through the list of flag URLs
        for index, flag_url in enumerate(self.flag_url_list):
            # Fetch the flag image from the URL using the requests library
            response = requests.get(flag_url)

            # Create a QPixmap from the image data
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(response.content)

            # Create an QIcon from the QPixmap
            icon = QtGui.QIcon(pixmap)

            # Set the icon for the corresponding index in the combobox
            self.obj.setItemIcon(index, icon)


# Main application window class
class MainWindow(QtWidgets.QMainWindow):
    # Define class constants for stylesheet colors and API endpoint
    RESET_COLOR = "background-color: #FFFFFF;"
    ERROR_COLOR = "background-color: #FF9800"
    NATIONALITY_URL = "https://restcountries.com/v3.1/all"

    def __init__(self):
        super().__init__()

        # Load the UI file
        self.ui = uic.loadUi("./ui/main.ui", self)

        # Initialize UI elements
        self.target_file_path = self.lineEdit
        self.first_name = self.ui.lineEdit_2
        self.last_name = self.ui.lineEdit_3
        self.age = self.ui.spinBox
        self.gender = self.ui.comboBox_2
        self.nationality = self.ui.comboBox
        self.email = self.ui.lineEdit_4
        self.phone_number = self.ui.lineEdit_5

        # Buttons for interaction
        self.select_folder_btn = self.ui.pushButton
        self.entry_data_btn = self.ui.pushButton_2

        # Initialize nationality combobox with flags
        self.init_nationality()
        # Initialize signals and slots
        self.init_signal_slot()

    # Connect button signals to corresponding methods
    def init_signal_slot(self):
        self.select_folder_btn.clicked.connect(self.get_file_path)
        self.entry_data_btn.clicked.connect(self.submit)

        # Connect signals for resetting stylesheets on text changes
        self.target_file_path.textChanged.connect(self.reset_stylesheet)
        self.first_name.textChanged.connect(self.reset_stylesheet)
        self.nationality.currentTextChanged.connect(self.reset_stylesheet)
        self.email.textChanged.connect(self.reset_stylesheet)

    # Initialize the nationality combobox with flags
    def init_nationality(self):
        # List to store flag URLs for asynchronous loading
        flag_url_list = []

        # Clear existing items in the nationality combobox
        self.nationality.clear()

        # Fetch the list of countries with their flags from a REST API
        res = requests.get(url=self.NATIONALITY_URL)

        # Check if the response contains valid JSON data
        if res.json():
            # Iterate through the list of countries and their flag URLs
            for index, nationality in enumerate(res.json()):
                # Extract the common name and flag URL for each country
                name = nationality.get("name")["common"]
                flag_url = nationality.get("flags")["svg"]

                # Add the common name to the nationality combobox
                self.nationality.addItem(name)

                # Collect the flag URL for asynchronous loading
                flag_url_list.append(flag_url)

            # Create a separate thread for loading nationality flags asynchronously
            task_thread = TaskThread(obj=self.nationality, flag_url_list=flag_url_list)
            task_thread.start()

            # Make the main window visible
            self.show()

    # Open a file dialog to get the path of an Excel file
    def get_file_path(self):
        # Open a folder dialog and get the selected file path
        folder_path = QtWidgets.QFileDialog.getOpenFileName(self, caption="Open Folder",
                                                            filter="*.xlsx")

        # Check if a file path was selected
        if folder_path[0]:
            # Clear any existing text in the target_file_path widget
            self.target_file_path.clear()

            # Set the selected file path in the target_file_path widget
            self.target_file_path.setText(folder_path[0])

    # Retrieve and validate data entered in the UI form
    def get_form_data(self):
        # Extract values from UI input fields
        file_path = self.target_file_path.text().strip()
        first_name = self.first_name.text().strip()
        last_name = self.last_name.text().strip()
        age = self.age.value()
        gender = self.gender.currentText()
        nationality = self.nationality.currentText()
        email = self.email.text().strip()
        phone_number = self.phone_number.text().strip()

        # Create a dictionary containing user input data
        data = {
            "First Name": first_name,
            "Last Name": last_name,
            "Age": age,
            "Gender": gender,
            "Nationality": nationality,
            "Email": email,
            "Phone Number": phone_number
        }

        # Create a dictionary for input data to be checked for validation
        check_data_dict = {
            self.target_file_path: file_path,
            self.first_name: first_name,
            self.nationality: nationality,
            self.email: email,
        }

        # Check the input data for validation errors
        check_result = self.check_input_data(data=check_data_dict)

        # If there are validation errors, return None
        if check_result:
            return
        else:
            # If validation passes, return the file path and user data as a tuple
            return file_path, data

    # Check the validity of input data and visually indicate errors in the UI
    def check_input_data(self, data):
        # Flag to indicate whether there are validation errors
        check_flag = False

        # Extract the email information for separate validation
        check_email = data.popitem()

        # Iterate through the remaining data items to check for empty values
        for obj, value in data.items():
            if not value:
                # Set the stylesheet of the widget to indicate an error
                check_flag = True
                obj.setStyleSheet(self.ERROR_COLOR)

        # Check if the email value is empty or lacks the "@" symbol
        if not check_email[1] or "@" not in check_email[1]:
            # Set the stylesheet of the email widget to indicate an error
            check_flag = True
            check_email[0].setStyleSheet(self.ERROR_COLOR)

        # Return the flag indicating whether there are validation errors
        return check_flag

    # Reset the stylesheet of the calling widget to the default color
    def reset_stylesheet(self):
        # Get the object (widget) that emitted the signal
        obj = self.sender()

        # Set the stylesheet of the widget to the default color
        obj.setStyleSheet(self.RESET_COLOR)

    # Method to clear the form fields
    def clear_form(self):
        # Clear the text content of specific form fields
        self.first_name.clear()
        self.last_name.clear()
        self.email.clear()
        self.phone_number.clear()

    # Method to submit form data to an Excel file
    def submit(self):
        try:
            # Get user input data from the form
            data = self.get_form_data()

            # Check if valid data is obtained
            if data:
                # Extract file path and user data from the returned tuple
                file_path = data[0]
                user_data = data[1]

                # Read existing data from the Excel file into a DataFrame
                df = pd.read_excel(file_path)

                # Create a DataFrame for the new user data
                user_df = pd.DataFrame(user_data, index=[0])

                # Choose one of the following methods to insert the new user data:

                # Method 1: Append new row to the last row
                # new_df = pd.concat([df, user_df], ignore_index=True)

                # Method 2: Insert new rows at a specific location (e.g., at the beginning)
                insert_row_index = 0
                new_df = pd.concat([df.iloc[:insert_row_index], user_df, df.iloc[insert_row_index:]],
                                   ignore_index=True)

                # Save the updated DataFrame to the Excel file, excluding the index column
                new_df.to_excel(file_path, index=False)

                # Clear the form fields after successful submission
                self.clear_form()
            else:
                # Display a warning message if form data is incomplete
                QtWidgets.QMessageBox.warning(self, "Warning", "Please input information.")

        except Exception as E:
            # Display a warning message in case of an error during submission
            QtWidgets.QMessageBox.warning(self, "Warning", f"Error: {E}")
            return


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    #  Load QSS file
    with open("style.qss", "r") as f:
        _style_str = f.read()
        app.setStyleSheet(_style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

















