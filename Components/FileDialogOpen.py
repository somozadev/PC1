import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Dialog(QWidget):
    def GetFilesAmount(self):
        return 0
    def __init__(self, textcategory, parent=None):

        self.textCategory = textcategory
        super(Dialog, self).__init__(parent)

        layout = QGridLayout()
        self.setLayout(layout)

        self.fileLabel = QLabel("Textos categoría {}: ".format(self.textCategory))
        layout.addWidget(self.fileLabel, 0, 0)
        layout.addItem(QSpacerItem(60,40, QSizePolicy.MinimumExpanding))
        self.textBox = QLineEdit("")
        layout.addWidget(self.textBox, 0, 1)

        self.getFilesButton = QPushButton("Abrir")
        self.getFilesButton.clicked.connect(self.getfile)
        layout.addWidget(self.getFilesButton, 0, 2)

    def getfile(self):
        filename = QFileDialog.getExistingDirectory(self, 'Seleccionar', self.textBox.text())
        if filename:
            self.textBox.setText(str(filename))

class DialogClasifTexts(QWidget):
    def __init__(self, name, parent=None):
        self.name = name
        super(DialogClasifTexts, self).__init__(parent)

        layout = QGridLayout()
        self.setLayout(layout)

        self.fileLabel = QLabel("{}: ".format(self.name))
        layout.addWidget(self.fileLabel, 0, 0)
        layout.addItem(QSpacerItem(60, 40, QSizePolicy.MinimumExpanding))
        self.textBox = QLineEdit("")
        layout.addWidget(self.textBox, 0, 1)

        self.getFilesButton = QPushButton("Seleccionar")
        self.getFilesButton.clicked.connect(self.getfile)
        layout.addWidget(self.getFilesButton, 0, 2)

    def getfile(self):
        filename = QFileDialog.getExistingDirectory(self, 'Seleccionar', self.textBox.text())
        if filename:
            self.textBox.setText(str(filename))

class DialogClasifModel(QWidget):
    def __init__(self, name, parent=None):
        self.name = name
        super(DialogClasifModel, self).__init__(parent)

        layout = QGridLayout()
        self.setLayout(layout)

        self.fileLabel = QLabel("{}: ".format(self.name))
        layout.addWidget(self.fileLabel, 0, 0)
        layout.addItem(QSpacerItem(60, 40, QSizePolicy.MinimumExpanding))
        self.textBox = QLineEdit("")
        layout.addWidget(self.textBox, 0, 1)

        self.getFilesButton = QPushButton("Seleccionar")
        self.getFilesButton.clicked.connect(self.getfileNoFolder)
        layout.addWidget(self.getFilesButton, 0, 2)

    def getfileNoFolder(self):
        filename = QFileDialog.getOpenFileName(self, 'Abrir modelo', 'c:\\', "All files(*.*)")  # Text files (*.txt)
        if filename:
            self.textBox.setText(str(filename[0]))