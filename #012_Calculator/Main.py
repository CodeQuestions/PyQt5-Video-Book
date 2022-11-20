import sys
from functools import partial

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

from UI.ui_calculator import Ui_MainWindow

ERROR_MSG = "ERROR"


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.display = self.ui.lineEdit

    def setDisplayText(self, text):
        """
        设置显示文本
        :param text:
        :return:
        """
        self.display.setText(text)
        self.display.setFocus()

    def setInit(self):
        self.display.setText("0")
        self.display.setFocus()

    def displayText(self):
        """
        获取显示文本
        :return: text
        """
        return self.display.text()

    def clearDisplay(self):
        """
        清除显示文本
        :return:
        """
        self.display.clear()


class PyCalCtrl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()

    def _calculateResult(self):
        """
        计算结果，并显示
        :return:
        """
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """
        创建表达式
        :param sub_exp:
        :return:
        """
        # 显示为错误信息需要先清除
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        if self._view.displayText() == "0":
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """
        连接信号与槽
        :return:
        """
        # 遍历页面所有控件，找到指定类型
        btn_list = self._view.findChildren(QPushButton)

        for btn in btn_list:
            if btn.text() not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btn.text()))
            elif btn.text() == "C":
                btn.clicked.connect(self._view.setInit)
            elif btn.text() == "=":
                btn.clicked.connect(self._calculateResult)

        self._view.display.returnPressed.connect(self._calculateResult)


def evaluateExpression(expression):
    try:
        # eval()将字符串作为表达式求值
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    PyCalCtrl(model=evaluateExpression, view=window)

    sys.exit(app.exec_())
