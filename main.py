import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])
# Create a QMainWindow
window = QMainWindow()
# Create a QLabel widget
label = QLabel("Hello, PyQt5!", parent=window)
label.setGeometry(50, 50, 200, 50)  # Set the position and size of the label

# Show the main window
window.show()

# Run the application's event loop
app.exec()
