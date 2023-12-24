import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from new_main_ui import Ui_Form


class MainWindow(QtWidgets.QWidget):
    ERROR_MSG = "ERROR"
    MAX_FONT_SIZE = 100
    MIN_FONT_SIZE = 30
    FONT_SIZE_THRESHOLDS = [item for item in enumerate(range(90, 30, -5), 9)]

    def __init__(self):
        super().__init__()

        # Initialize variables for calculator state and UI handling
        self._dragPos = None
        self.new_input_flag = False
        self.prev_text = ""
        self.curr_text = ""
        self.show_text = ""
        self.operator = ""

        # Load the UI setup from the external UI form
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Assign UI components to class attributes for easy access
        self.output = self.ui.lineEdit
        self.close_btn = self.ui.close_btn
        self.clear_btn = self.ui.pushButton_3
        self.plus_minus_btn = self.ui.pushButton_4
        self.percent_btn = self.ui.pushButton_5
        self.addition_btn = self.ui.pushButton_15
        self.subtraction_btn = self.ui.pushButton_11
        self.multiplication_btn = self.ui.pushButton_8
        self.division_btn = self.ui.pushButton_6
        self.calculate_btn = self.ui.pushButton_19

        # Mapping of operator buttons to their corresponding symbols
        self.operator_btn_list = [
            (self.addition_btn, "+"),
            (self.subtraction_btn, "-"),
            (self.multiplication_btn, "*"),
            (self.division_btn, "/"),
        ]

        # Configuration for the icons of various buttons
        self.icon_config = {
            self.close_btn: ["./icon/close.svg", 30],
            self.plus_minus_btn: ["./icon/plus-minus-variant.svg", 40],
            self.percent_btn: ["./icon/percent-solid.svg", 50],
        }

        # Initialize the UI components
        self.initialize_ui()

    def initialize_ui(self):
        """ Initialize window settings, buttons, and signal-slot connections """
        self.setup_window()
        self.setup_buttons()
        self.init_signal_slot()

    def setup_window(self):
        """ Configure window flags and attributes """
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.output.setText("0")

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        """ Enable window dragging with mouse press """
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self._dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        """ Handle window movement on mouse drag """
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton and self._dragPos:
            self.move(self.pos() + event.globalPosition().toPoint() - self._dragPos)
            self._dragPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        """ Reset dragging position on mouse release """
        self._dragPos = None

    def setup_buttons(self):
        """ Set up buttons with icons and configurations """
        for btn, conf in self.icon_config.items():
            icon = QtGui.QIcon(conf[0])
            btn.setIcon(icon)
            btn.setIconSize(QtCore.QSize(conf[1], conf[1]))

        self.plus_minus_btn.setCheckable(True)
        self.plus_minus_btn.setChecked(False)

    def init_signal_slot(self):
        """ Initialize signal-slot connections for interactive UI elements """
        self.close_btn.clicked.connect(self.close)
        self.output.textChanged.connect(self.update_clear_btn)
        self.output.textChanged.connect(self.update_font_size)

        # Connect all button clicks to the calculate method
        btn_list = self.ui.button_frame.findChildren(QtWidgets.QPushButton)
        for btn in btn_list:
            btn.clicked.connect(self.calculate)

        # Special button functionalities
        self.plus_minus_btn.toggled.connect(self.change_text)
        self.percent_btn.clicked.connect(self.percent)

    def set_display_text(self):
        """ Set display text on the calculator screen """
        if self.show_text and "." in self.show_text:
            if self.show_text.endswith("."):
                self.output.setText(f"{int(self.show_text[:-1]):,}")
            elif self.show_text.endswith(".0"):
                self.output.setText(f"{int(self.show_text[:-2]):,}")
            else:
                self.output.setText(f"{float(self.show_text):,}")
        elif self.show_text and "." not in self.show_text:
            self.output.setText(f"{int(self.show_text):,}")
        else:
            self.output.setText("0")

    def update_clear_btn(self):
        """ Update the clear button text based on input """
        if self.output.text() != "0":
            self.clear_btn.setText("C")
        else:
            self.clear_btn.setText("AC")

    def update_font_size(self):
        """ Adjust font size based on the length of the text """
        text_length = len(self.output.text())

        for threshold, size in self.FONT_SIZE_THRESHOLDS:
            if threshold == text_length:
                self.output.setStyleSheet(f"font-size:{size}px")
                return

        if text_length > 16:
            self.output.setStyleSheet(f"font-size:{self.MIN_FONT_SIZE}px")
        else:
            self.output.setStyleSheet(f"font-size:{self.MAX_FONT_SIZE}px")

    def calculate(self):
        """ Handle calculator operations based on button clicks """
        show_text = self.output.text()
        if show_text == self.ERROR_MSG:
            return

        clicked_btn = self.sender()
        # Handle clear button
        if clicked_btn == self.clear_btn:
            self.reset_calculation()

        # Handle input numbers and decimal point
        elif clicked_btn.text() in ["."] + [str(i) for i in range(10)]:
            self.reset_buttons()
            # Check if any operator was selected
            if self.new_input_flag:
                self.show_text = clicked_btn.text()
                self.new_input_flag = False
            else:
                if clicked_btn.text() == "." and "." in self.show_text:
                    return

                self.show_text = self.output.text().replace(",", "") + clicked_btn.text()

            self.set_display_text()

        # Handle operator input
        elif clicked_btn in [btn[0] for btn in self.operator_btn_list]:
            selected_operator = [btn for btn in self.operator_btn_list if btn[0].isChecked()]

            if self.operator == selected_operator[0][1]:
                self.new_input_flag = True
                return

            elif self.operator and self.operator != selected_operator[0][1]:
                self.show_text = str(self.safe_evaluate_expression())
                self.set_display_text()
                self.operator = selected_operator[0][1]
                self.prev_text = self.show_text
                self.new_input_flag = True

            else:
                self.prev_text = self.output.text().replace(",", "")
                self.operator = selected_operator[0][1]
                self.new_input_flag = True

        # Handle calculation result
        elif clicked_btn == self.calculate_btn:
            self.result()
            self.operator = ""

    def result(self):
        """ Calculate and display the result of the expression """
        if not self.operator:
            return

        if self.operator:
            try:
                result = self.safe_evaluate_expression()
                self.show_text = str(int(result) if str(result).endswith(".0") else result)
                self.set_display_text()
            except Exception:
                self.output.setText(self.ERROR_MSG)
            finally:
                self.reset_buttons()

    def change_text(self, state):
        """ Toggle negative sign for the current input """
        if state:
            self.show_text = f"-{self.output.text()}".replace(" ", "")
        else:
            self.show_text = self.output.text()[1:].replace(",", "")
        self.set_display_text()

    def percent(self):
        """ Calculate and display the percentage of the current input """
        self.show_text = str(float(self.output.text().replace(",", "")) / 100)

        # if len(self.show_text) > 12:
        #     self.show_text = self.show_text[:12]

        self.set_display_text()

    def reset_calculation(self):
        """ Reset the calculator to its initial state """
        self.prev_text = self.show_text = self.operator = ""
        self.clear_btn.setText("AC")
        self.reset_buttons()
        self.set_display_text()

    def reset_buttons(self):
        """ Reset the state of operator buttons """
        for btn in self.operator_btn_list:
            btn[0].setAutoExclusive(False)
            btn[0].setChecked(False)
            btn[0].setAutoExclusive(True)
        self.plus_minus_btn.setChecked(False)

    def safe_evaluate_expression(self):
        """ Safely evaluate the mathematical expression """
        self.curr_text = self.output.text().replace(",", "")

        if self.prev_text == "":
            return self.curr_text
        else:
            return eval(f"{self.prev_text or 0}{self.operator}{self.curr_text}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
