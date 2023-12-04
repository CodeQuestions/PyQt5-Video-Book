from PyQt6 import QtWidgets, uic
from connect_db import DatabaseConnect


class NewProductWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI file
        self.ui = uic.loadUi("./ui/new_product.ui", self)

        # Get references to the new product dialog
        self.new_product_save_btn = self.ui.pushButton
        self.new_product_cancel_btn = self.ui.pushButton_2

        self.product_name = self.ui.lineEdit
        self.cost = self.ui.doubleSpinBox
        self.price = self.ui.doubleSpinBox_2
        self.location = self.ui.comboBox
        self.reorder_level = self.ui.spinBox
        self.stock = self.ui.spinBox_2

        # Initialize the ConnectDB object for database operations
        self.connect_db = DatabaseConnect()

    def new_product_data(self):
        # Retrieve data from UI components
        product_name = self.product_name.text().strip()
        cost = self.cost.value()
        price = self.price.value()
        location = self.location.currentText()
        reorder_level = self.reorder_level.value()
        stock = self.stock.value()

        # Validate input data
        data_list = [product_name, location]
        bool_data_list = list(map(lambda item: bool(item), data_list))

        if False in bool_data_list:
            # Incomplete data, return None
            return None
        else:
            # Create a dictionary with the extracted data
            data_dict = {
                "product_name": product_name,
                "cost": cost,
                "price": price,
                "location": location,
                "reorder_level": reorder_level,
                "stock": stock,
            }

            return data_dict

    def add_new_product(self):
        # Retrieve product data
        product_data = self.new_product_data()

        if product_data:
            # Add the new product data into database
            add_result = self.connect_db.add_new_product(**product_data)

            return add_result

        else:
            # Incomplete data, return an error message
            return "More data needed to input"

    def clear_data(self):
        # Clear data in UI components
        self.product_name.clear()
        self.cost.setValue(0)
        self.price.setValue(0)
        self.location.clear()
        self.reorder_level.setValue(0)
        self.stock.setValue(0)
