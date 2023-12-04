from PyQt6 import QtWidgets, QtCore, uic
from connect_db import DatabaseConnect


class UpdateStockWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # Load the inventory UI
        self.ui = uic.loadUi('./ui/update_stock.ui', self)

        # Initialize UI elements
        self.submit_btn = self.ui.pushButton_2
        self.select_btn = self.ui.pushButton

        self.input_product_name = self.ui.lineEdit
        self.show_product_name = self.ui.lineEdit_2
        self.product_name_list = self.ui.listWidget
        self.new_stock = self.ui.spinBox

        self.in_radio_btn = self.ui.radioButton
        self.out_radio_btn = self.ui.radioButton_2

        # Connect to the database
        self.connect_db = DatabaseConnect()

        # Initialize search dialog
        self.init_search_dialog()

        # Connect signals to slots
        self.input_product_name.textChanged.connect(self.update_product_name_list)
        self.select_btn.clicked.connect(self.select_product)

    def init_search_dialog(self):
        """
        Initialize the search dialog by populating the list of product names.
        """
        # Retrieve all product names from the database
        search_result = self.connect_db.get_product_names("")
        product_name_list = [item[0] for item in search_result]

        # Add product names to the list widget
        self.product_name_list.clear()
        self.product_name_list.addItems(product_name_list)

    def update_product_name_list(self, text):
        """
        Update the list of product names based on the input text.
        """
        # Clear the product name list widget
        self.product_name_list.clear()

        # Get product names from the database based on the input text
        search_result = self.connect_db.get_product_names(text)
        product_name_list = [item[0] for item in search_result]

        # Add product names to the list widget
        self.product_name_list.addItems(product_name_list)

    def select_product(self):
        """
        Select the product from the list and set it in the input field.
        """
        # Get the selected product name from the list widget
        self.show_product_name.clear()
        select_obj = self.product_name_list.currentItem()
        product_name = ""
        if select_obj:
            product_name = select_obj.text()


        # Set the selected product name in the input field
        self.show_product_name.setText(product_name)

    def submit(self):
        """
        Submit the stock update to the database.
        """
        # Get the product name from the input field
        product_name = self.show_product_name.text()
        if product_name:
            # Retrieve original stock and update stock from the UI
            original_stock = self.connect_db.get_single_product_info(product_name=product_name)[0]
            update_stock = self.new_stock.value()

            # Update the stock based on the selected operation (add or subtract)
            if self.in_radio_btn.isChecked():
                stock = original_stock + update_stock
            else:
                stock = original_stock - update_stock

            # Update the stock in the database
            update_result = self.connect_db.update_stock(product_name=product_name, stock=stock)

            return update_result

        else:
            return "Please select a product to update stock."
