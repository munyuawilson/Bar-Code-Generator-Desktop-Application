from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import shutil
from PIL import Image

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

