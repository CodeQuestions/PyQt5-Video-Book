import sys
import random
import csv

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton
from PyQt5.QtGui import QIcon, QPixmap

from UI.Password import Ui_MainWindow
from Tools import QssTool


class MainWindow(QMainWindow):
    # 初始化程序
    # ///////////////////////////////////////////////////////////////////
    def __init__(self):
        super(MainWindow, self).__init__()

        setQSS = QssTool()

        # 加载界面
        # ///////////////////////////////////////////////////////////////////
        self.main_window_ui = Ui_MainWindow()
        self.main_window_ui.setupUi(self)

        # 设置窗口图标
        # ///////////////////////////////////////////////////////////////////
        icon = QIcon("static/icons/key-6-128.ico")
        self.setWindowIcon(icon)

        # 定义变量参数
        # ///////////////////////////////////////////////////////////////////
        self.tabWidget = self.main_window_ui.tabWidget

        self.username_s = self.main_window_ui.lineEdit_8
        self.website_s = self.main_window_ui.lineEdit_9
        self.refresh_btn = self.main_window_ui.pushButton_4
        self.search_btn = self.main_window_ui.pushButton_5
        self.show_info = self.main_window_ui.tableWidget

        self.website_g = self.main_window_ui.lineEdit_5
        self.username_g = self.main_window_ui.lineEdit_6
        self.length = self.main_window_ui.comboBox
        self.uppercase_check = self.main_window_ui.checkBox
        self.numbers_check = self.main_window_ui.checkBox_2
        self.special_check = self.main_window_ui.checkBox_3
        self.generate_btn = self.main_window_ui.pushButton
        self.password = self.main_window_ui.lineEdit_7
        self.copy_btn = self.main_window_ui.pushButton_3
        self.save_btn = self.main_window_ui.pushButton_2

        self.lowercase_c = self.main_window_ui.lineEdit_4
        self.uppercase_c = self.main_window_ui.lineEdit
        self.numbers_c = self.main_window_ui.lineEdit_2
        self.special_c = self.main_window_ui.lineEdit_3

        self.generate_btn.clicked.connect(self.show_password)
        self.copy_btn.clicked.connect(self.copy_password)
        self.save_btn.clicked.connect(self.save_password)
        self.search_btn.clicked.connect(self.search_info)
        self.refresh_btn.clicked.connect(self.refresh)
        self.tabWidget.currentChanged.connect(self.show_info_change_tab)

        icon = QIcon("static/icons/show-property-128.gif")
        self.tabWidget.setTabIcon(0, icon)

        icon = QIcon("static/icons/key-4-128.gif")
        self.tabWidget.setTabIcon(1, icon)

        icon = QIcon("static/icons/data-configuration-128.gif")
        self.tabWidget.setTabIcon(2, icon)

        self.search_info()

        # 设置对象名，用于设置qss
        # ///////////////////////////////////////////////////////////////////
        self.password.setObjectName("password")

        self.refresh_btn.setObjectName("refresh")
        setQSS.setQss("static/style.qss", self.refresh_btn)

        self.search_btn.setObjectName("search")
        setQSS.setQss("static/style.qss", self.search_btn)

        self.generate_btn.setObjectName("generate")
        self.copy_btn.setObjectName("copy")
        self.save_btn.setObjectName("save")
        self.show_info.setObjectName("table")

    # 创建密码.
    # ///////////////////////////////////////////////////////////////////
    def create_password(self):

        password = ""

        characters = list(self.lowercase_c.text())

        length = int(self.length.currentText())

        if self.uppercase_check.isChecked() == True:
            characters.extend(self.uppercase_c.text())

        if self.numbers_check.isChecked() == True:
            characters.extend(self.numbers_c.text())

        if self.special_check.isChecked() == True:
            characters.extend(self.special_c.text())

        for x in range(length):
            password += random.choice(characters)

        return password

    # 校验密码.
    # ///////////////////////////////////////////////////////////////////
    def verify_password(self, password):
        characters = list(self.lowercase_c.text())
        result1 = list(set(characters) & set(password))
        if result1:
            result = True
        else:
            return False

        if self.uppercase_check.isChecked() == True:
            characters = list(self.uppercase_c.text())
            result2 = list(set(characters) & set(password))
            if result2:
                result = True
            else:
                return False

        if self.numbers_check.isChecked() == True:
            characters = list(self.numbers_c.text())
            result3 = list(set(characters) & set(password))
            if result3:
                result = True
            else:
                return False

        if self.special_check.isChecked() == True:
            characters = list("!@#$%^&*")
            result4 = list(set(characters) & set(password))
            if result4:
                result = True
            else:
                return False

        return result

    # 展示密码.
    # ///////////////////////////////////////////////////////////////////
    def show_password(self):
        flag = True
        password = ""
        while flag:
            password = self.create_password()
            result = self.verify_password(password)
            if result == True:
                password = password
                break
            else:
                continue

        self.password.setText(password)

    # 复制密码.
    # ///////////////////////////////////////////////////////////////////
    def copy_password(self):
        try:
            if self.password.text():
                clipboard = QApplication.clipboard()  # 创建剪切板对象
                clipboard.setText(self.password.text())
                QMessageBox.information(self, "Copy Password", "Successfully!!!", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "Copy Password", "Password is Empty!!!", QMessageBox.Ok)
        except:
            QMessageBox.information(self, "Copy Password", "Error", QMessageBox.Ok)

    # 保存密码.
    # ///////////////////////////////////////////////////////////////////
    def save_password(self):
        password = self.password.text()
        username = self.username_g.text()
        website = self.website_g.text()

        if password.strip() == "":
            QMessageBox.information(self, "Save password", "Password is empty. Please generate password.",
                                    QMessageBox.Ok)
            return
        if username.strip() == "":
            QMessageBox.information(self, "Save password", "Username is empty. Please enter username.", QMessageBox.Ok)
            return
        if website.strip() == "":
            QMessageBox.information(self, "Save password", "Website is empty. Please generate website.", QMessageBox.Ok)
            return

        # 打开数据保存文件
        # ///////////////////////////////////////////////////////////////////
        try:
            with open("static/db.csv", 'a', newline="") as csvFile:
                info = csv.writer(csvFile)
                info.writerow([website, username, password])
            QMessageBox.information(self, "Save password", "Successfully", QMessageBox.Ok)
        except:
            QMessageBox.information(self, "Save password", "Error", QMessageBox.Ok)

    # 查询已经保存的信息
    # ///////////////////////////////////////////////////////////////////
    def search_info(self):
        db_list = []
        search_username = self.username_s.text().strip()
        search_website = self.website_s.text().strip()
        try:
            with open("static/db.csv", 'r') as csvFile:
                info = csv.reader(csvFile)
                for item in info:
                    db_list.append(item)
            del db_list[0]

            if search_username == "" and search_website == "":
                db_list = db_list
            else:
                db_list = self.search_filter(db_list, search_username, search_website)

            row_count = len(db_list)
            self.show_info.setRowCount(row_count)
            if row_count != 0:
                for row, row_item in enumerate(db_list):
                    for column, column_item in enumerate(row_item):
                        self.show_info.setItem(row, column, QTableWidgetItem(column_item))

                    self.delete_btn = QPushButton("Delete")
                    self.delete_btn.setObjectName("delete")
                    # style = "margin: 3px 5px;"
                    # self.delete_btn.setStyleSheet(style)
                    self.delete_btn.clicked.connect(self.delete)
                    self.show_info.setCellWidget(row, 3, self.delete_btn)
            # else:
            #     QMessageBox.information(self, "Search Information", "Empty", QMessageBox.Ok)

        except Exception as e:
            QMessageBox.information(self, "Search Information", "Error", QMessageBox.Ok)

    # 删除数据功能
    # ///////////////////////////////////////////////////////////////////
    def delete(self):
        row_num = self.find_location_table()
        data_list = self.read_data()

        del data_list[row_num]

        with open("static/db.csv", 'w', newline="") as csvFile:
            info = csv.writer(csvFile)
            info.writerows(data_list)

        self.search_info()

    # 确定点击位置
    # ///////////////////////////////////////////////////////////////////
    def find_location_table(self):
        # self.value_list = []
        button = self.sender()
        if button:
            try:
                row = self.show_info.indexAt(button.pos()).row()
                return row
            except:
                pass

    # 读取存储数据
    # ///////////////////////////////////////////////////////////////////
    def read_data(self):
        data_list = []
        with open("static/db.csv", "r") as rf:
            all_data = csv.reader(rf)
            for item in all_data:
                data_list.append(item)

        return data_list

    # 切换窗口时刷新显示列表
    # ///////////////////////////////////////////////////////////////////
    def show_info_change_tab(self, change_index):
        if change_index == 0:
            self.search_info()
        else:
            pass

    # 清除搜索输入框
    # ///////////////////////////////////////////////////////////////////
    def refresh(self):
        self.username_s.clear()
        self.website_s.clear()

    # 定义筛选功能，返货筛选之后结果
    # ///////////////////////////////////////////////////////////////////
    def search_filter(self, data_list, username, website):
        filter_list = []
        for data in data_list:
            if username in data[1] and website in data[0]:
                filter_list.append(data)

        return filter_list


if __name__ == '__main__':
    app = QApplication(sys.argv)

    setQSS = QssTool()
    setQSS.setQss("static/style.qss", app)

    window = MainWindow()
    window.show()

    app.exec_()
