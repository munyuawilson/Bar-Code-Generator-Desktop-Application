from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import shutil

def downloadFile(path):
    # Specify the path and filename of the file to be downloaded
    generated_file_path = "path/to/generated_file.ext"  # Replace with the path to your generated file

    # Prompt the user to select the download location
    save_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "All Files (*.*)")

    if save_path:
        try:
            # Copy the generated file to the specified location
            shutil.copy(path, save_path)
            print("File downloaded successfully.")
        except Exception as e:
            print("Error while downloading file:", str(e))
    else:
        print("Download canceled.")

if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("File Downloader")
    window.setGeometry(100, 100, 300, 200)

    download_button = QPushButton("Download File", window)
    download_button.clicked.connect(downloadFile)
    download_button.setGeometry(50, 50, 200, 30)

    window.show()
    app.exec_()
