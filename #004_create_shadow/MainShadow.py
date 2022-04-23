import sys

from PyQt6.QtGui import QColor
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QColorDialog

from shadow_ui import Ui_MainWindow


class myMainWindow(QMainWindow):
    def __init__(self):
        super(myMainWindow, self).__init__()

        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        ## ///////////////////////////////////////////////////////////////////////////////////
        ## init widgets
        self.label = self.main_ui.label
        self.button = self.main_ui.pushButton
        self.lineEdit = self.main_ui.lineEdit

        self.x_offset = self.main_ui.x_value
        self.y_offset = self.main_ui.y_value
        self.blur_radius = self.main_ui.y_value_2

        self.color = self.main_ui.lineEdit_2
        self.shadow_label = QGraphicsDropShadowEffect()

        self.show_fix_shadows()

    def show_fix_shadows(self):

        ## /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        ## fix shadow
        # creating a QGraphicsDropShadowEffect object
        shadow_button = QGraphicsDropShadowEffect()
        # set blur radius
        shadow_button.setBlurRadius(20)
        # setting color
        # shadow_label.setColor(QColor(0, 255, 255))
        shadow_button.setColor(QColor("#0000ff"))

        shadow_lineEidt = QGraphicsDropShadowEffect()
        shadow_lineEidt.setBlurRadius(20)

        ## /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        ## add shadow to widgets
        self.button.setGraphicsEffect(shadow_button)
        self.lineEdit.setGraphicsEffect(shadow_lineEidt)

    def on_horizontalSlider_valueChanged(self):
        self.show_alterable_shadow()

    def on_horizontalSlider_2_valueChanged(self):
        self.show_alterable_shadow()

    def on_horizontalSlider_3_valueChanged(self):
        self.show_alterable_shadow()

    def show_alterable_shadow(self):
        """
        set alterable shadow for label
        :return:
        """

        ## //////////////////////////////////////////////////////////////////////////////////
        ## get all the parameters for label
        x_offset = float(self.x_offset.text())
        y_offset = float(self.y_offset.text())
        blur_radius = float(self.blur_radius.text())

        ## /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        ## set parameters
        # set blur radius
        self.shadow_label.setBlurRadius(blur_radius)
        # setting offset
        self.shadow_label.setOffset(x_offset, y_offset)

        ## /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        ## set shadow for label
        self.label.setGraphicsEffect(self.shadow_label)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        set shadow of label by QColorDialog
        :return:
        """

        ## /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        ## init color dialog
        color_dialog = QColorDialog(self)

        if color_dialog.exec():
            ## /////////////////////////////////////////////////////////////////////////////////////////////////////////
            ## get slected color
            color = color_dialog.selectedColor()
            if color.isValid():
                ## /////////////////////////////////////////////////////////////////////////////////////////////////////
                ## show rgb value of the selected color
                self.color.setText(str(color.getRgb()))
                ## /////////////////////////////////////////////////////////////////////////////////////////////////////
                # setting color of shadow
                self.shadow_label.setColor(color)

                ## /////////////////////////////////////////////////////////////////////////////////////////////////////
                ## shadow of label
                self.show_alterable_shadow()
        else:
            ## /////////////////////////////////////////////////////////////////////////////////////////////////////////
            ## cancel to change shadow color
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = myMainWindow()
    window.show()

    sys.exit(app.exec())
