import sys
from PyQt6 import QtWidgets, uic, QtGui, QtCore

from connect_db import DatabaseConnect
from new_product import NewProductWindow
from update_product_info import UpdateProductWindow
from update_stock import UpdateStockWindow
from search import SearchWindow


class StockManagement(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the main ui file
        self.ui = uic.loadUi("./ui/main.ui", self)

        # Initialize dialog windows and database connection
        self.new_product_dialog = NewProductWindow()
        self.update_product_dialog = UpdateProductWindow()
        self.update_stock_dialog = UpdateStockWindow()
        self.search_dialog = SearchWindow()
        self.connect_db = DatabaseConnect()

        # Define actions for menu items
        self.actions = {
            self.ui.actionNew_Product: "open_new_product_dialog",
            self.ui.actionStock_Update: "open_update_stock_dialog",
            self.ui.actionSearch: "open_search_dialog",
            self.ui.actionExit: "exit_app",
        }

        # Populate initial data
        self.init_signal_slot()
        self.update_dashboard()
        self.search_all_product()

    def init_signal_slot(self):
        # Connect actions to their respective functions
        for action, function_name in self.actions.items():
            action.triggered.connect(getattr(self, function_name))

        # Connect buttons to their respective functions
        self.search_dialog.detail_btn.clicked.connect(self.search_more_detail)
        self.search_dialog.current_stock_btn.clicked.connect(self.search_in_stock_product)
        self.search_dialog.reorder_btn.clicked.connect(self.search_reorder_product)
        self.search_dialog.no_stock_btn.clicked.connect(self.search_no_stock_product)
        self.search_dialog.all_product_btn.clicked.connect(self.search_all_product)

        # Connect new product dialog buttons to their respective functions
        self.new_product_dialog.new_product_save_btn.clicked.connect(self.new_product_save)
        self.new_product_dialog.new_product_cancel_btn.clicked.connect(self.new_product_cancel)

        # Connect update product button box to its function
        self.update_product_dialog.product_update_button_box.accepted.connect(self.update_product_save)

        # Update stock dialog button
        self.update_stock_dialog.submit_btn.clicked.connect(self.update_stock_submit)

    def open_new_product_dialog(self):
        """
        Open the new product dialog and populate location options
        """
        self.new_product_dialog.show()

        # Set location options
        locations = self.connect_db.get_all_locations()
        locations_list = [str(location[0]) for location in locations]
        locations_list.insert(0, "")
        self.new_product_dialog.location.clear()
        self.new_product_dialog.location.addItems(locations_list)

    def open_update_stock_dialog(self):
        """
        Open update stock dialog
        """
        self.update_stock_dialog.show()
        self.update_stock_dialog.init_search_dialog()
        self.update_stock_dialog.raise_()

    def open_search_dialog(self):
        """
        Open the search dialog
        """
        self.search_dialog.show()
        self.search_dialog.raise_()

    def exit_app(self):
        """
        Close the application
        """
        self.close()

    def open_update_product_dialog(self, product_name):
        """
        Open the update product dialog and pupulate data
        :param product_name:
        :return:
        """
        self.update_product_dialog.show()
        self.update_product_dialog.init_product_list(product_name=product_name)
        self.update_product_dialog.raise_()

    ## Common function for show new data in the QTableWidget ////////////////////////////////////////////////
    def show_data(self, data, title="Stock Management Example"):
        """
        The order of the data:
            product_name, cost, price, stock, location, reorder_level

        :param data:
        :param title:
        :return:
        """
        table = self.ui.tableWidget
        table.setRowCount(0)
        self.ui.label_11.setText(title)

        if data:
            self.update_dashboard()
            row_count = len(data)
            table.setRowCount(row_count)

            for row, product in enumerate(data):
                action_edit = QtGui.QAction("Edit", self)
                action_delete = QtGui.QAction("Delete", self)

                # Connect actions to functions
                action_edit.triggered.connect(lambda: self.action_edit_triggered(table))
                action_delete.triggered.connect(lambda: self.action_delete_triggered(table))

                # Create QMenu
                menu = QtWidgets.QMenu(self)
                # Add actions
                menu.addActions([action_edit, action_delete])

                option_btn = QtWidgets.QPushButton(self)
                option_btn.setText("Option")
                option_btn.setMenu(menu)

                row_data = [
                    product[0], product[3], product[2], product[1], product[5],
                    "Yes" if product[5] >= product[3] else "No",
                    product[4], option_btn
                ]

                for column, item in enumerate(row_data):
                    if column != 7:
                        item_obj = QtWidgets.QTableWidgetItem(str(item))
                        table.setItem(row, column, item_obj)
                    else:
                        table.setCellWidget(row, column, item)

    def update_dashboard(self):
        current_stock = self.connect_db.get_current_stock()[0]
        self.ui.label.setText(str(current_stock) + "Unit(s)")

        stock_value = self.connect_db.get_stock_value()[0]
        self.ui.label_3.setText("$" + str(stock_value))

        stock_cost = self.connect_db.get_stock_cost()[0]
        self.ui.label_5.setText("$" + str(stock_cost))

        reorder_count = self.connect_db.get_reorder_product()[0]
        self.ui.label_7.setText(str(reorder_count))

        no_stock_count = self.connect_db.get_no_stock_product()[0]
        self.ui.label_9.setText(str(no_stock_count))

    ## QAction function for options in table ////////////////////////////////////////////////////////////
    def action_edit_triggered(self, table):
        product_name = table.item(table.currentRow(), 0).text()
        self.open_update_product_dialog(product_name=product_name)

    def action_delete_triggered(self, table):
        product_name = table.item(table.currentRow(), 0).text()
        choice = QtWidgets.QMessageBox.warning(self, "Delete !!!", f"Are you sure to delete {product_name} ?",
                                               QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.Cancel)
        if choice == QtWidgets.QMessageBox.StandardButton.Yes:
            self.connect_db.delete_product(product_name=product_name)

            search_data = self.search_dialog.get_all_products()
            self.show_data(data=search_data, title="Stock Management Example >>> All products")

    ## Function for adding new product //////////////////////////////////////////////////////////////////
    def new_product_save(self):
        add_result = self.new_product_dialog.add_new_product()

        if not add_result:
            # Clear data in dialog
            self.new_product_dialog.clear_data()
            self.new_product_dialog.close()

            # Show datas after add new product
            search_data = self.search_dialog.get_all_products()
            self.show_data(data=search_data, title="Stock Management Example >>> All Products")
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", add_result, QtWidgets.QMessageBox.StandardButton.Ok)

            # Bring the dialog window to the front
            self.new_product_dialog.raise_()

    def new_product_cancel(self):
        self.new_product_dialog.close()
        search_data = self.search_dialog.get_all_products()
        self.show_data(data=search_data, title="Stock Management Example >>> All Products")

    ## Functions for SEARCH dialog ///////////////////////////////////////////////////////////////////////
    def search_more_detail(self):
        data = self.search_dialog.get_more_detail()
        self.show_data(data=data, title="Stock Management Example >>> Single Product Information")

    def search_in_stock_product(self):
        data = self.search_dialog.get_in_stock_product()
        self.show_data(data=data, title="Stock Management Example >>> All in Stock Products")

    def search_reorder_product(self):
        data = self.search_dialog.get_reorder_product()
        self.show_data(data=data, title="Stock Management Example >>> Reorder Required Products")

    def search_no_stock_product(self):
        data = self.search_dialog.get_no_stock_product()
        self.show_data(data=data, title="Stock Management Example >>> All out of Stock Products")

    def search_all_product(self):
        data = self.search_dialog.get_all_products()
        self.show_data(data=data, title="Stock Management Example >>> All Products")

    ## Function for updating product ///////////////////////////////////////////////////////////
    def update_product_save(self):
        update_result = self.update_product_dialog.update_product_info()

        if not update_result:
            self.update_product_dialog.close()

            # Show data after update product
            search_data = self.search_dialog.get_all_products()
            self.show_data(data=search_data, title="Stock Management Example >>> All products")

        else:
            QtWidgets.QMessageBox.warning(self, "Warning", f"Please try again: {update_result}",
                                          QtWidgets.QMessageBox.StandardButton.Ok)

            self.update_product_dialog.raise_()

    ## Function for updating stock ///////////////////////////////////////////////////////////
    def update_stock_submit(self):
        update_result = self.update_stock_dialog.submit()

        if update_result:
            QtWidgets.QMessageBox.warning(self, "Warning", update_result)
            self.update_stock_dialog.raise_()
            return
        else:
            self.update_stock_dialog.show_product_name.clear()
            self.update_stock_dialog.close()
            search_data = self.search_dialog.get_all_products()
            self.show_data(data=search_data, title="Stock Management Example >>> All Products ")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = StockManagement()
    window.show()
    sys.exit(app.exec())
