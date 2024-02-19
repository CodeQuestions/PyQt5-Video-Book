import sys
from PySide6.QtGui import QColor
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QColorDialog
from shadow_ui import Ui_MainWindow


class myMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.shadowEffect = QGraphicsDropShadowEffect()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initializeWidgets()
        self.connectSignals()

    def initializeWidgets(self):
        # self.ui.pushButton.setGraphicsEffect(self.createShadowEffect(color=QColor("#0000ff")))
        self.ui.lineEdit.setGraphicsEffect(self.createShadowEffect())

        QApplication.processEvents()

    # @staticmethod
    def createShadowEffect(self, color=QColor(0, 0, 0), radius=20):
        shadow = QGraphicsDropShadowEffect()
        shadow.setOffset(10.0, 10.0)
        shadow.setBlurRadius(radius)
        shadow.setColor(color)

        self.ui.pushButton.setGraphicsEffect(shadow)

        return shadow

    def connectSignals(self):
        sliders = [self.ui.horizontalSlider, self.ui.horizontalSlider_2, self.ui.horizontalSlider_3]
        for slider in sliders:
            slider.valueChanged.connect(self.showAlterableShadow)

        self.ui.pushButton_2.clicked.connect(self.pushButtonClicked)

    def showAlterableShadow(self):
        x_offset = float(self.ui.x_value.text())
        y_offset = float(self.ui.y_value.text())
        blur_radius = float(self.ui.y_value_2.text())

        self.shadowEffect.setBlurRadius(blur_radius)
        self.shadowEffect.setOffset(x_offset, y_offset)
        self.ui.label.setGraphicsEffect(self.shadowEffect)

    @Slot()
    def pushButtonClicked(self):
        color_dialog = QColorDialog(self)
        if color_dialog.exec():
            color = color_dialog.selectedColor()
            if color.isValid():
                self.ui.lineEdit_2.setText(str(color.getRgb()))
                print(color)
                self.shadowEffect.setColor(color)
                self.showAlterableShadow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myMainWindow()
    window.show()
    sys.exit(app.exec())
