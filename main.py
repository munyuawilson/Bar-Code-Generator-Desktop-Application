import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

# Create a QMainWindow
window = QMainWindow()
window.setWindowTitle("Bar Code Generator")

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

# Show the main window
window.show()

# Start the application event loop
sys.exit(app.exec_())
