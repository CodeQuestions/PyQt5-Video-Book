from PyQt6 import QtWidgets, uic
from connect_db import DatabaseConnect


class UpdateProductWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # Load the update product UI
        self.ui = uic.loadUi('./ui/update_product.ui', self)

        # Connect to the database
        self.connect_db = DatabaseConnect()

        # Initialize UI elements
        self.product_update_button_box = self.ui.buttonBox

        self.product_name = self.ui.lineEdit
        self.cost = self.ui.doubleSpinBox
        self.price = self.ui.doubleSpinBox_2
        self.location = self.ui.comboBox
        self.reorder_level = self.ui.spinBox
        self.stock = self.ui.spinBox_2

    def init_product_list(self, product_name):
        product_data = self.connect_db.get_data(product_name=product_name)

        locations = self.connect_db.get_all_locations()
        locations_list = [str(location[0]) for location in locations]
        locations_list.insert(0, "")

        self.set_data(product_data, locations_list)

    def set_data(self, product_data, location_list):
        """
        Set data in the update product dialog.

        Args:
            product_data (list): List containing product data.
            location_list (list): List of locations for the location combo box.
        """
        # Populate location combo box
        self.location.clear()
        self.location.addItems(location_list)

        # Set values in the UI based on the provided product data
        self.product_name.setText(product_data[0][0])
        self.cost.setValue(product_data[0][1])
        self.price.setValue(product_data[0][2])
        self.reorder_level.setValue(product_data[0][5])
        self.stock.setValue(product_data[0][3])
        self.location.setCurrentText(str(product_data[0][4]))

    def get_product_data(self):
        """
        Retrieve updated product data from the UI.

        Returns:
            dict: A dictionary containing updated product data.
        """
        product_name = self.product_name.text().strip()
        cost = self.cost.value()
        price = self.price.value()
        location = self.location.currentText()
        reorder_level = self.reorder_level.value()
        stock = self.stock.value()

        # Check if all required data is provided
        data_list = [product_name, location]
        bool_data_list = list(map(lambda item: bool(item), data_list))

        if False in bool_data_list:
            # Show a warning message if any data is missing
            QtWidgets.QMessageBox.warning(self, "Warning", "Please input all the data",
                                          QtWidgets.QMessageBox.StandardButton.Ok)
            return

        # Construct a dictionary with the updated product data
        data_dict = {
            "product_name": product_name,
            "cost": cost,
            "price": price,
            "location": location,
            "reorder_level": reorder_level,
            "stock": stock,
        }

        return data_dict

    def update_product_info(self):
        product_data = self.get_product_data()

        if product_data:
            update_result = self.connect_db.update_product(product_name=product_data.get("product_name"),
                                                           cost=product_data.get("cost"),
                                                           price=product_data.get("price"),
                                                           location=product_data.get("location"),
                                                           reorder_level=product_data.get("reorder_level"),
                                                           stock=product_data.get("stock"))

            return update_result

        else:
            return "More data needed to input."
