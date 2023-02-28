import json
import sys
import os
from PyQt5.QtWidgets import QApplication

from app_main import MainWindow

if __name__ == '__main__':
    flag = os.path.exists("datas/data.json")
    print(flag)

    if not flag:
        os.mkdir("datas")
        with open("datas/data.json", "w") as f:
            f.write(json.dumps([]))

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
