import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QPushButton,QFileDialog,QLineEdit,QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont,QIcon
from PyQt5.QtCore import Qt
import pandas as pd
import os
import zipfile
import barcode
from barcode.writer import ImageWriter
from PIL import Image

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import shutil


def downloadFile(path):
    
    # Specify the path and filename of the file to be downloaded
    

    # Prompt the user to select the download location
    save_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Zip Files (*.zip)")

    if save_path:
        try:
            
            shutil.copy(path, save_path)
            print("File downloaded successfully.")
        except Exception as e:
            print("Error while downloading file:", str(e))
    else:
        print("Download canceled.")
def generate_barcode(text, barcode_type='code128'):
    # Create a barcode object
    barcode_class = barcode.get_barcode_class(barcode_type)
    barcode_object = barcode_class(text, writer=ImageWriter())

    # Set the filename for the barcode image
    filename = f'barcode_{text}'

    # Save the barcode image
    barcode_object.save(filename)
    image = Image.open(filename+".png")

    # Crop the image to the desired size
    width, height = image.size
    desired_width = 256
    desired_height = 186
    x = (width - desired_width) // 2
    y = (height - desired_height) // 2
    
    image.thumbnail((desired_width, desired_height), Image.LANCZOS)

    # Save the cropped image
    image.save(filename+".png")
    return filename


if getattr(sys, 'frozen', False):
    # If the application is run as a bundle (e.g., PyInstaller executable)
    logo_path = sys._MEIPASS + '/logo.png'  # Update 'logo.png' to the name of your logo file
else:
    # If the application is run as a standalone script
    logo_path = 'logo.png' 
# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the current directory
os.chdir(current_dir)

app = QApplication(sys.argv)

def window_1(app):
    

    # Create a QMainWindow
    window = QMainWindow()
    window.setWindowTitle("Bar Code Generator")

    window.setFixedSize(700, 400)
    window.setWindowIcon(QIcon('logo.ico'))

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
    window.setWindowIcon(QIcon('logo.ico'))
    layout = QVBoxLayout()
    
    central_widget = QWidget()
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)
    
    
    
    # Add a label for the instruction on Uploading
    
    
    
    
    
    text_entry = QLineEdit(window)
    #Add styles for all the widgets
    
    text_entry.setFixedHeight(100)
    layout.addWidget(text_entry)
    
    
    #Download button
    download_output=QPushButton("Download",window)
    download_output.setGeometry(200, 500, 200, 50)
    download_output.setStyleSheet("background-color:#436953;color:white;")
    download_output.setFixedWidth(200)
    
    # Function for tgetting the text
    def get_text():
        sender=window.sender()
        if sender==submit_text:
        
            entered_text = text_entry.text()
            image_name=generate_barcode(entered_text)
            list_images=[image_name+".png"]
            
            zip_files(list_images, 'barcodes.zip')
            for image in list_images:
                os.remove(image) 
        
        
        
        
    
    download_output.clicked.connect(lambda: downloadFile(os.path.join(current_dir, "barcodes.zip")))   
    
    upload_button = QPushButton("Upload File", window)
    
    upload_button.setGeometry(250, 400, 200, 50)
    
    upload_button.setStyleSheet("background-color:#436953;color:white;")
    
    # Add submit button for text-based input
    
    submit_text=QPushButton("Generate",window)
    
    submit_text.setStyleSheet("background-color:#436953;color:white;")
    
    submit_text.setFixedWidth(200)
    layout.addWidget(submit_text)
    
    submit_text.clicked.connect(lambda:get_text())
    
    
    

    
    # Set width for the QPushButton widget
    upload_button.setFixedWidth(200)
    # Create a QVBoxLayout to hold the QLabel and text label
    
    layout.addWidget(upload_button)
    layout.addWidget(download_output)  
        
    
    
    
    
    choose_column=QLineEdit()
    def zip_files(file_paths, zip_name):
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in file_paths:
                zipf.write(file,os.path.basename(file))
    def upload():
        sender=window.sender()
        if sender==upload_button:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(window, "Upload File")
            if file_path:
                # Process the selected file
                data=pd.read_excel(file_path)
                
                list_images=[]
                
                for i in data.barcode:
                    print(i)
                    image_name=generate_barcode(i)
                    image_fullname=image_name+".png"
                    list_images.append(image_fullname)
                    print(image_fullname)
                    zip_files(list_images, 'barcodes.zip')
                    
                    
                for image in list_images:
                    os.remove(image)   
                layout.addWidget(download_output)   

                    # Calculate the desired width and height for the image in the Word document
                    
                

    upload_button.clicked.connect(upload)
    
    
    window.show()

    


window_1(app)
