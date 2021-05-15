class QssTool():
    @staticmethod
    def setQss(file_path, obj):
        with open(file_path, "r") as f:
            style = f.read()
            obj.setStyleSheet(style)