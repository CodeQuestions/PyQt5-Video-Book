import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt, QPoint

# Import the UI layout defined in Qt Designer
from main_ui import Ui_MainWindow


class FrameLessMainWindow(QMainWindow):
    def __init__(self):    
        super().__init__()        

        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)  # Setup the UI    

        # Remove the title bar and set the window to be frameless            
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)        
        # Enable transparency of background        
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)        

        self.ui.maxmize_btn.setCheckable(True)       

        # Connect the custom minimize, maximize/restore, and close buttons to their functions        
        self.ui.minimize_btn.clicked.connect(self.showMinimized)        
        self.ui.maxmize_btn.clicked.connect(self.toggle_maximize_restore)        
        self.ui.close_btn.clicked.connect(self.close)   

        # Variables to keep track of the window dragging             
        self.old_pos = self.pos()  # Initial position of the window        
        self.mouse_pressed = False  # Flag to track if the mouse is pressed        



    def toggle_maximize_restore(self):        
        # Toggle between fullscreen and normal size        
        if self.isFullScreen():        
            self.showNormal()            
        else:            
            self.showFullScreen()            
    
    def mousePressEvent(self, event):
        # Capture the initial position of the mouse when it is pressed        
        self.old_pos = event.globalPosition().toPoint()        
        self.mouse_pressed = True        

    def mouseMoveEvent(self, event):        
        # Move the window as the mouse is dragged        
        if self.mouse_pressed:        
            delta = QPoint(event.globalPosition().toPoint() - self.old_pos)            
            self.move(self.x() + delta.x(), self.y() + delta.y())            
            self.old_pos = event.globalPosition().toPoint()            

    def mouseReleaseEvent(self, event):            
        # Release the mouse press flag        
        self.mouse_pressed = False        

        

if __name__ == "__main__":        
    app = QApplication(sys.argv)    

    # Load and apply a stylesheet for custom UI appearance    
    stylesheet_str = """    
            #icon_label {   
                border-image: url("./icon/logo.png")            
            }                
        """            
    app.setStyleSheet(stylesheet_str)        

    window = FrameLessMainWindow()    
    window.show()    
    sys.exit(app.exec())    






























