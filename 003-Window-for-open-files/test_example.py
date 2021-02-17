from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
import sys

from example import Ui_MainWindow


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        # 实例化窗口类
        # Instantiate window class
        self.main_ui = Ui_MainWindow()
        # 窗口setup
        # window setup
        self.main_ui.setupUi(self)
        # 定义窗口对象
        # Define window objects
        self.open_button = self.main_ui.OpenButton
        self.file_name_line_edit = self.main_ui.FileNameLineEdit
        # 设置全局变量名
        # Set global variable name
        self.file_name = ""
        self.file_path = ""
        # 关联打开文件事件
        # Associated open file event
        self.open_button.clicked.connect(self.open_file)

    # 创建打开文件方法
    # Create open file method
    def open_file(self):
        self.file_path = QFileDialog.getOpenFileName(caption='select file', directory='',
                                                     filter='Excel files(*.xlsx , *.xls)', initialFilter='')
        self.file_name = self.file_path[0].split('/')[-1]

        # 调用显示文件名称方法
        # Call the display file name method
        self.show_file_name()

    # 创建显示文件名称方法
    # Create a display file name method
    def show_file_name(self):
        file_name = self.file_name
        if file_name:
            # 设置QLineEdit显示文本
            # Set QLineEdit to display text
            self.file_name_line_edit.setText(file_name)
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyMainWindow()
    window.show()

    app.exit(app.exec_())
