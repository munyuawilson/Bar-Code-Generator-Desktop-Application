import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
def window_1(app):
    

    # Create a QMainWindow
    window = QMainWindow()
    window.setWindowTitle("Bar Code Generator")

    window.setFixedSize(700, 400)

    # Create a QVBoxLayout to hold the QLabel and text label
    layout = QVBoxLayout()

    # Add the image QLabel
    image_label = QLabel()
    pixmap = QPixmap("logo.png")  # Replace with your image path
    image_label.setPixmap(pixmap)
    image_label.setAlignment(Qt.AlignCenter)
    layout.addWidget(image_label)

    # Add the text QLabel
    text_label = QLabel("Unlock Your Products' Potential with Seamless Bar Code Generation!")
    text_label.setAlignment(Qt.AlignCenter)
    text_label.setFont(QFont("Arial", 14))  # Increase font size (adjust as needed)
    text_label.setMargin(1)  # Adjust the margin around the text label
    layout.addWidget(text_label)

    # Create a QWidget to hold the layout
    central_widget = QWidget()
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)

    #add button
    button_next=QPushButton("Next")
    button_close=QPushButton("Close")

    #add then to layout
    layout.addWidget(button_next)
    layout.addWidget(button_close)

    

    #Add color
    button_close.setStyleSheet("background-color: #436953;color:white;")
    button_next.setStyleSheet("background-color: #436953;color:white;")
    #ADD button functionality
    def button_function():
        sender = window.sender()
        if sender == button_close:
            window.close()
        elif sender == button_next:
            window.close()
            window_2(app)
    button_next.clicked.connect(button_function)
    button_close.clicked.connect(button_function)
    # Show the main window
    window.show()

    # Start the application event loop
    sys.exit(app.exec_())

def window_2(app):
    

    # Create a QMainWindow
    window = QMainWindow()
    window.setWindowTitle("Bar Code Generator")

    window.setFixedSize(700, 400)
    upload_button = QPushButton("Upload File", window)
    
    # Create a QVBoxLayout to hold the QLabel and text label
    layout = QVBoxLayout()
    layout.addWidget(upload_button)
    
    def upload():
        sender=window.sender()
        if sender==upload_button:
            pass
        
    upload_button.clicked.connect(upload)
    
    
    window.show()

    


window_1(app)