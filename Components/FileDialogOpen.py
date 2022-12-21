import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Dialog(QWidget):
    def GetFilesAmount(self):
        return 0
    def __init__(self, textcategory, parent=None):
        """
        :type textcategory: str
        """
        self.textCategory = textcategory
        super(Dialog, self).__init__(parent)

        layout = QGridLayout()
        self.setLayout(layout)

        self.fileLabel = QLabel("Textos categoría {}: ".format(self.textCategory))
        layout.addWidget(self.fileLabel, 0, 0)

        self.textBox = QLineEdit("")
        layout.addWidget(self.textBox, 0, 1)

        self.getFilesButton = QPushButton("Abrir")
        self.getFilesButton.clicked.connect(self.getfile)
        layout.addWidget(self.getFilesButton, 0, 2)

    def getfile(self):
        filename = QFileDialog.getExistingDirectory(self, 'Seleccionar carpeta', self.textBox.text())
        if filename:
            self.textBox.setText(str(filename))
