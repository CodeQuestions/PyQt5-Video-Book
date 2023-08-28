import sys
import qrcode
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, \
                                QPushButton, QSlider, QLineEdit, QColorDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Slot
from PIL import ImageQt

# Import the UI class generated from the .ui file
from main_ui import Ui_MainWindow


# Define the main application window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_qss("style.qss")

        # Assign UI elements to instance variables for easy access
        self.input_content = self.ui.textEdit
        self.version = self.ui.horizontalSlider
        self.box_size = self.ui.horizontalSlider_2
        self.border_size = self.ui.horizontalSlider_3
        self.fill_color_btn = self.ui.pushButton
        self.fill_color_text = self.ui.lineEdit
        self.back_color_btn = self.ui.pushButton_2
        self.back_color_text = self.ui.lineEdit_2
        self.qr_code = self.ui.result_label
        self.generate_btn = self.ui.generate_btn
        self.save_btn = self.ui.save_btn

        # Clear the QR code display
        self.qr_code.clear()

        # Initialize signal-slot connections
        self.init_signal_slot()

    # Load and apply QSS from file
    @staticmethod
    def load_qss(file_path):
        with open(file_path, "r") as f:
            qss = f.read()

        app.setStyleSheet(qss)

    def init_signal_slot(self):
        # Create a list of UI elements to connect signals to slots
        objects_list = [
            self.generate_btn,
            self.save_btn,
            self.version,
            self.box_size,
            self.border_size,
            self.fill_color_text,
            self.back_color_text,
        ]

        # Connect signals based on object type
        for obj in objects_list:
            if type(obj) == QPushButton:
                obj.clicked.connect(self.create_qr_code)
            elif type(obj) == QSlider:
                obj.valueChanged.connect(self.create_qr_code)
            elif type(obj) == QLineEdit:
                obj.textChanged.connect(self.create_qr_code)
            else:
                continue

        # Connect the save button to the save_qr_code method
        self.save_btn.clicked.connect(self.save_qr_code)
        # Connect the fill color button to the select_fill_color method
        self.fill_color_btn.clicked.connect(self.select_fill_color)
        # Connect the back color button to the select_back_color method
        self.back_color_btn.clicked.connect(self.select_back_color)

    def select_fill_color(self):
        # Open a color dialog for selecting fill color
        fill_color = QColorDialog.getColor()
        if fill_color.isValid():
            self.fill_color_text.setText(fill_color.name())

    def select_back_color(self):
        # Open a color dialog for selecting background color
        back_color = QColorDialog.getColor()
        if back_color.isValid():
            self.back_color_text.setText(back_color.name())

    def save_qr_code(self):
        # Open a file dialog to save the QR code image
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "", "Images (*.png)", options=options)

        if file_path:
            # Save the QR code pixmap as a PNG image
            self.qr_code.pixmap().save(file_path, "PNG")

    def create_qr_code(self):
        # Get data from the input content field
        data = self.input_content.toPlainText()

        if not data:
            # Clear the QR code display if there's no data
            self.qr_code.clear()
            return

        # Retrieve version, box size, border size, fill color, and back color
        version = self.version.value()
        if not version:
            version = None

        box_size = self.box_size.value()
        border = self.border_size.value()
        fill_color = self.fill_color_text.text()
        back_color = self.back_color_text.text()

        # Generate the QR code with the specified parameters
        qr = qrcode.QRCode(
            version=version,  # None or 1 - 40
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )

        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Convert the PIL image object to a QPixmap object
        qr_img_pixmap = QPixmap.fromImage(ImageQt.ImageQt(qr_img))

        # Set the QPixmap as the QR code display
        self.qr_code.setPixmap(qr_img_pixmap)


# Main entry point of the application
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create and show the main application window
    window = MainWindow()
    window.show()

    # Start the event loop
    sys.exit(app.exec())
