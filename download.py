from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import shutil

def downloadFile(path):
    
    # Specify the path and filename of the file to be downloaded
    

    # Prompt the user to select the download location
    save_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "PNG Files (*.png)")

    if save_path:
        try:
            # Copy the generated file to the specified location
            shutil.copy(path, save_path)
            print("File downloaded successfully.")
        except Exception as e:
            print("Error while downloading file:", str(e))
    else:
        print("Download canceled.")

