import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt6.QtCore import Qt

from main_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.tableWidget = self.ui.tableWidget

    def keyPressEvent(self, event) -> None:
        super().keyPressEvent(event)
        try:
            # Check keyboard input(Ctrl + V) to accomplish of paste
            if event.key() == Qt.Key.Key_V and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):
                selection = self.tableWidget.selectedIndexes()

                if selection:
                    # Get the first selected cell position
                    row_anchor = selection[0].row()
                    column_anchor = selection[0].column()

                    # Create clipboard object to read data from clipboard
                    clipboard = QApplication.clipboard()
                    # Get data list from clipboard
                    rows = clipboard.text().split('\n')

                    # Add more rows if current row count doesn't match the new row count needed
                    if self.tableWidget.rowCount() < row_anchor + len(rows) - 1:
                        self.tableWidget.setRowCount(row_anchor + len(rows) - 1)

                    # Show data in table widget which gets from Excel file
                    for index_row, row in enumerate(rows):
                        values = row.split("\t")
                        for index_col, value in enumerate(values):
                            item = QTableWidgetItem(value)
                            self.tableWidget.setItem(row_anchor + index_row, column_anchor + index_col, item)

            # Check keyboard input(Ctrl + C) to accomplish copy
            # Check keyboard input(Ctrl + X) to accomplish cut
            if (event.key() == Qt.Key.Key_C or event.key() == Qt.Key.Key_X) \
                and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):
                # get the selection section data
                copied_cell = sorted(self.tableWidget.selectedIndexes())
                # Define a variable to save selected data
                copy_text = ""
                max_column = copied_cell[-1].column()
                for cell in copied_cell:
                    # Get each cell text
                    cell_item = self.tableWidget.item(cell.row(), cell.column())
                    if cell_item:
                        copy_text += cell_item.text()
                        # Clear data in table widget when it cuts data
                        if event.key() == Qt.Key.Key_X:
                            cell_item.setText("")

                    else:
                        copy_text += ""

                    # Format the copied data for paste into Excel file
                    if cell.column() == max_column:
                        copy_text += "\n"
                    else:
                        copy_text += "\t"

                # Save data into clipboard
                QApplication.clipboard().setText(copy_text)

        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
















