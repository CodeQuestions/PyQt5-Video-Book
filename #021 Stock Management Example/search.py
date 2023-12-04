from PyQt6 import QtWidgets, uic
from connect_db import DatabaseConnect


class SearchWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Load the search UI file
        self.ui = uic.loadUi("./ui/search.ui", self)

        self.connect_db = DatabaseConnect()

        # UI elements
        self.product_name_LW = self.ui.listWidget
        self.input_product_name_LE = self.ui.lineEdit
        self.current_stock_label = self.ui.label_2
        self.reorder_label = self.ui.label_4
        self.location_number_label = self.ui.label_6

        # Buttons
        self.all_product_btn = self.ui.pushButton
        self.current_stock_btn = self.ui.pushButton_2
        self.reorder_btn = self.ui.pushButton_3
        self.no_stock_btn = self.ui.pushButton_4
        self.detail_btn = self.ui.pushButton_5

        # Initialize the search dialog
        self.init_search_dialog()

        # Connect signals to slots
        self.input_product_name_LE.textChanged.connect(self.update_product_name_list)
        self.product_name_LW.currentTextChanged.connect(self.search_product_info)

    def init_search_dialog(self):
        """
        Initialize the search dialog by populating the list of product names.
        """
        search_result = self.connect_db.get_product_names("")
        product_name_list = [item[0] for item in search_result]
        self.product_name_LW.clear()
        self.product_name_LW.addItems(product_name_list)

        # Set initial values for UI labels
        self.current_stock_label.setText("-")
        self.reorder_label.setText("-")
        self.location_number_label.setText("-")

    def get_more_detail(self):
        product_name_obj = self.ui.listWidget.currentItem()

        if product_name_obj:
            product_name = product_name_obj.text()

            data = self.connect_db.get_data(product_name=product_name)
            self.close()
            return data

        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a product.")
            return

    def get_in_stock_product(self):
        data = self.connect_db.get_data(search_flag="IN_STOCK")
        self.close()

        return data

    def get_reorder_product(self):
        data = self.connect_db.get_data(search_flag="RE_ORDER")
        self.close()

        return data

    def get_no_stock_product(self):
        data = self.connect_db.get_data(search_flag="NO_STOCK")
        self.close()

        return data

    def get_all_products(self):
        data = self.connect_db.get_data(search_flag="ALL")
        self.close()

        return data

    def search_product_info(self, product_name):
        """
        Search for product information and update UI labels.
        """
        print("search_product_info,", product_name)

        if product_name:
            # Retrieve product information from the database
            search_result = self.connect_db.get_single_product_info(product_name=product_name)
            print(search_result)

            # Update UI labels with the retrieved information
            self.current_stock_label.setText(str(search_result[0]))

            if search_result[0] > search_result[1]:
                self.reorder_label.setText("No")
            else:
                self.reorder_label.setText("Yes")

            self.location_number_label.setText(str(search_result[2]))

        else:
            # Clear UI labels if no product name is selected
            self.current_stock_label.setText("-")
            self.reorder_label.setText("-")
            self.location_number_label.setText("-")

    def update_product_name_list(self, text):
        """
        Update the list of product names based on the input text.
        """
        self.product_name_LW.clear()

        # Retrieve product names from the database based on the input text
        search_result = self.connect_db.get_product_names(text)
        product_name_list = [item[0] for item in search_result]
        self.product_name_LW.addItems(product_name_list)
