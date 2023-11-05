# Import necessary libraries and modules
import sys
import re
import requests
import random
import html
from bs4 import BeautifulSoup

from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QRadioButton, QWidget, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

# Import the user interface from "main_ui.py"
from new_main_ui import Ui_MainWindow


# Define a class for making API requests and fetching question data
class DataRequest:
    def __init__(self):
        # Initialize headers and API URLs
        self._headers = {'User-Agent': 'Mozilla/5.0'}
        self._config_url = "https://opentdb.com/api_config.php"
        self._basic_url = "https://opentdb.com/api.php"
        self._api_url = None

        # Initialize dictionaries to store configuration data
        self.config_category = dict()
        self.config_difficulty = dict()
        self.config_type = dict()

        # Create a mapping of configuration names to their respective dictionaries
        self.select_names = {
            'trivia_category': self.config_category,
            'trivia_difficulty': self.config_difficulty,
            'trivia_type': self.config_type
        }

    # Method to fetch configuration data from the API
    def get_config_data(self):
        res_config = requests.request("GET", url=self._config_url, headers=self._headers)

        soup = BeautifulSoup(res_config.text, features="lxml")

        for config_name, config_data in self.select_names.items():
            # Find the select element
            select_element = soup.find('select', {'name': config_name})

            # Iterate through the option elements
            options = select_element.find_all('option')

            # Extract the values and text and store in the corresponding dictionary
            values_and_text = [(option['value'], option.text) for option in options]

            for value, text in values_and_text:
                config_data[text] = value

    # Method to fetch trivia questions based on specified parameters
    def get_questions(self, number="50", category="any", difficulty="any", type="any"):
        self._api_url = self._basic_url
        self._api_url += f"?amount={number}"

        if category != "any":
            self._api_url += f"&category={category}"

        if difficulty != "any":
            self._api_url += f"&difficulty={difficulty}"

        if type != "any":
            self._api_url += f"&type={type}"

        res_api = requests.request("GET", url=self._api_url, headers=self._headers)
        result = res_api.json()

        return result


# Define the main application window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ## Initialize DataRequest #############################################################
        # Initialize the DataRequest object for API requests
        self.data_request = DataRequest()

        # Initialize dictionaries to store configuration data
        self.config_category = dict()
        self.config_difficulty = dict()
        self.config_type = dict()

        # Initialize a list to store fetched questions and the current question index
        self.current_question_index = 0
        self.questions_list = list()

        # Initialize the user interface ##########################################################
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Get references to UI elements ##########################################################
        # Settings page
        self.number = self.ui.spinBox_2
        self.category = self.ui.comboBox_6
        self.difficulty = self.ui.comboBox_5
        self.type = self.ui.comboBox_4

        # Questions page
        self.question_count_label = self.ui.question_count_label
        self.question_category_label = self.ui.lineEdit
        self.question_difficulty_label = self.ui.lineEdit_2
        self.question_text = self.ui.plainTextEdit

        self.get_question_btn = self.ui.pushButton_5
        self.try_again_btn = self.ui.pushButton_3
        self.check_answer_btn = self.ui.pushButton_4
        self.next_question_btn = self.ui.pushButton_2

        self.answer_frame = self.ui.answer_frame

        ## Init status bar #####################################################################
        # Customize the status bar
        self.ui.statusbar.setMinimumHeight(25)

        ## Status bar message
        self.status_bar_timeout = 5000

        self.answer_icon_size = QSize(12, 12)

        self.right_answer_icon = "./icons/checkmark-64.ico"
        self.right_answer_color = "#186A3B"
        self.right_answer_message = "Answer is correct."

        self.wrong_answer_icon = "./icons/x-mark-48.ico"
        self.wrong_answer_color = "#C0392B"
        self.wrong_answer_message = "Answer is wrong. Please try again."

        self.success_get_data_message = "Successfully to get new questions."
        self.fail_get__data_message = "Fail to get new questions, Please try again."

        ## QMessageBox Info #######################################################################
        # Information for reminding to select an answer
        self.reminder_select_option = "Please select an answer."

        # Information for finishing all the questions
        self.reminder_all_done = "Congratulations, You Finished All the Questions!"

        # Initialize the user interface
        self.init_ui()
        # Connect signals to slots
        self.init_signal_slot()

        self.get_new_questions()

    # Method to fetch and populate configuration data
    def get_config_data(self):
        self.data_request.get_config_data()
        self.config_category = self.data_request.config_category
        self.config_difficulty = self.data_request.config_difficulty
        self.config_type = self.data_request.config_type

    # Method to initialize the UI with configuration data
    def init_ui(self):
        self.get_config_data()

        self.category.clear()
        self.category.addItems(self.config_category.keys())

        self.difficulty.clear()
        self.difficulty.addItems(self.config_difficulty.keys())

        self.type.clear()
        self.type.addItems(self.config_type.keys())

    # Method to connect UI buttons to their respective functions
    def init_signal_slot(self):
        self.get_question_btn.clicked.connect(self.get_new_questions)
        self.try_again_btn.clicked.connect(self.try_again)
        self.check_answer_btn.clicked.connect(self.check_result)
        self.next_question_btn.clicked.connect(self.next_question)

    # Method to fetch new questions from the API
    def get_new_questions(self):
        self.questions_list = []
        self.get_question_btn.setDisabled(True)

        number = self.number.text()
        category = self.category.currentText()
        difficulty = self.difficulty.currentText()
        type = self.type.currentText()

        result = self.data_request.get_questions(number=number,
                                                 category=self.config_category.get(category),
                                                 difficulty=self.config_difficulty.get(difficulty),
                                                 type=self.config_type.get(type))

        response_code = result.get("response_code")

        if response_code == 0 and result.get("results"):
            self.ui.statusbar.showMessage(self.success_get_data_message, self.status_bar_timeout)
            self.questions_list = result.get("results")
            self.current_question_index = 0
            self.init_question_ui()
        else:

            self.ui.statusbar.showMessage(self.fail_get__data_message, self.status_bar_timeout)

        self.get_question_btn.setDisabled(False)

    # Method to initialize the UI with the current question data
    def init_question_ui(self):
        self.try_again_btn.setDisabled(True)
        self.check_answer_btn.setDisabled(False)
        if self.questions_list:
            total_count = len(self.questions_list)

            self.question_count_label.clear()
            self.question_count_label.setText(f"{self.current_question_index + 1}/{total_count}")

            self.question_category_label.clear()
            self.question_category_label.setText(self.questions_list[self.current_question_index].get("category"))

            self.question_difficulty_label.clear()
            self.question_difficulty_label.setText(
                self.questions_list[self.current_question_index].get("difficulty").title()
            )

            self.question_text.clear()

            question_text = self.questions_list[self.current_question_index].get("question")

            html_code_list = list(set(re.findall(r'&[^;]+;', question_text)))

            if html_code_list:
                new_question_text = question_text
                for code in html_code_list:
                    replace_str = html.unescape(code)
                    new_question_text = new_question_text.replace(code, replace_str)
            else:
                new_question_text = question_text

            self.question_text.setPlainText(new_question_text)

            layout = self.answer_frame.layout()
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.setParent(None)

            answer_list = []
            answer_list = answer_list + self.questions_list[self.current_question_index].get("incorrect_answers")
            answer_list.append(self.questions_list[self.current_question_index].get("correct_answer"))
            random.shuffle(answer_list)

            for answer in answer_list:
                new_answer_text = answer
                html_code_list = list(set(re.findall(r'&[^;]+;', answer)))
                for code in html_code_list:
                    replace_str = html.unescape(code)
                    new_answer_text = new_question_text.replace(code, replace_str)
                    if html_code_list:
                        new_answer_text = new_answer_text

                    else:
                        new_question_text = answer

                radio_btn = QRadioButton(new_answer_text)
                layout.addWidget(radio_btn)

    # Method to move to the next question
    def next_question(self):
        self.current_question_index += 1

        total_count = len(self.questions_list)
        if self.current_question_index < total_count:
            print("next_question", self.current_question_index)
            self.init_question_ui()
        else:
            self.current_question_index -= 1
            QMessageBox.information(self, "Information", self.reminder_all_done,
                                    QMessageBox.StandardButton.Ok)

            return

    # Method to reset the UI and try the current question again
    def try_again(self):
        self.init_question_ui()

    # Method to check the selected answer and provide feedback
    def check_result(self):
        print("check_result", self.current_question_index)
        self.check_answer_btn.setDisabled(True)
        question_data = self.questions_list[self.current_question_index]
        correct_answer = question_data.get("correct_answer")
        layout = self.answer_frame.layout()

        answer_selected_flag = False

        for i in reversed(range(layout.count())):
            radio_button = layout.itemAt(i).widget()

            if radio_button.isChecked():
                answer_selected_flag = True
                if radio_button.text() == correct_answer:
                    self.update_answer_ui(radio_button, self.right_answer_icon, self.right_answer_color,
                                          self.right_answer_message)
                else:
                    self.update_answer_ui(radio_button, self.wrong_answer_icon, self.wrong_answer_color,
                                          self.wrong_answer_message)
                    self.try_again_btn.setDisabled(False)
                break

        if not answer_selected_flag:
            self.check_answer_btn.setDisabled(False)
            QMessageBox.information(self, "Information", self.reminder_select_option,
                                    QMessageBox.StandardButton.Ok)

    def update_answer_ui(self, radio_button, icon_path, color, message):
        icon = QIcon(icon_path)
        radio_button.setIcon(icon)
        radio_button.setIconSize(self.answer_icon_size)
        radio_button.setStyleSheet(f"color: {color}")

        self.ui.statusbar.showMessage(message, self.status_bar_timeout)


# Entry point for the application
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
