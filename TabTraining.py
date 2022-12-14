from PyQt5.QtWidgets import *

from pathlib import Path
import sys
class TabTraining(QWidget):
    def __init__(self):
        layout = QGridLayout()

        self.setLayout(layout)

        file_browser_btn = QPushButton("Browse")
        file_browser_btn.clicked.connect(self.open_file_dialog)

        self.file_list = QListWidget(self)

        layout.addWidget(QLabel('Files:'), 0, 0)
        layout.addWidget(self.file_list, 1, 0)
        layout.addWidget(file_browser_btn, 2, 0)

        self.show()


        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setFilter("Texts (*.txt)")
