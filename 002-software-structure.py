# -*- coding: utf-8 -*-
"""
-------------------------------------
Package                   Version
---------------------    ------------
PyQt5                     5.15.2
---------------------    ------------
Python Version:           3.8.5
--------------------------------------
Create Time: 02-14-2021
Author:  CoolCode
--------------------------------------
"""
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # 设置窗口在屏幕中的显示位置及大小(x-position, y-position, width, height)
        # Set the display position and size of the window on the screen(x-position, y-position, width, height)
        self.setGeometry(500, 200, 500, 500)
        # 设置窗口名称
        # Set window title
        self.setWindowTitle("This is the WindowTitle")
        # 设置窗口图标
        # Set window icon
        self.setWindowIcon(QtGui.QIcon("./img/cow-2-256.ico"))

        # 设置控件式样
        # Set control style
        self.label_style = """
        QLabel {
            background-color: blue;
        }
        """
        self.setup_ui()

    def setup_ui(self):
        # 设置label并添加文字
        # Set label and add text
        label = QtWidgets.QLabel("test label", self)
        # 设置label大小
        # Set label size(width, height)
        label.resize(100, 50)
        # 设置label位置(x-position, y-position)
        # Set label position(x-position, y-position)
        label.move(100, 250)
        # 设置label式样
        # Set label style
        label.setStyleSheet(self.label_style)


if __name__ == '__main__':
    # 创建一个应用程序对象
    # Create an application object
    app = QApplication(sys.argv)
    # 实例化窗口对象
    # Instantiate window object
    window = MyWindow()
    # 展示窗口
    # Show window
    window.show()
    # 应用程序的执行, 进入到消息循环
    # The execution of the application enters the message loop
    sys.exit(app.exec_())
