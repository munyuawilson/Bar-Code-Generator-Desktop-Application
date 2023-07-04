import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout


class WidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Widget Position Example')
        self.setGeometry(300, 300, 250, 100)

        layout = QVBoxLayout()

        label1 = QLabel('Widget 1')
        layout.addWidget(label1)

        nested_layout = QHBoxLayout()
        layout.addLayout(nested_layout)

        nested_layout.addStretch(1)  # Add stretchable space to the left

        label2 = QLabel('Widget 2')
        nested_layout.addWidget(label2)

        nested_layout.addStretch(1)  # Add stretchable space to the right

        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WidgetExample()
    sys.exit(app.exec_())
