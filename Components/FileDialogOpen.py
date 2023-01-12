import os
from PyQt5.QtWidgets import *


class Dialog(QWidget):
    def GetFilesAmount(self):
        if self.textBox.text() != '':
            list = os.listdir(self.textBox.text())
            number_files = len(list)
            return number_files

        return 0
    def GetPath(self):
        return self.textBox.text()
    def __init__(self, Training, textcategory, parent=None):
        self.Training = Training
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
            if self.textCategory == "Entrantes":
                self.Training.OnPathUpdate_A()
            elif self.textCategory == "Principales":
                self.Training.OnPathUpdate_B()
            elif self.textCategory == "Segundos":
                self.Training.OnPathUpdate_C()
            elif self.textCategory == "Postres":
                self.Training.OnPathUpdate_D()


class DialogClasifTexts(QWidget):
    def __init__(self, Test, name, parent=None):
        self.name = name
        self.Test = Test
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

    def GetPath(self):
        return self.textBox.text()
    def getfile(self):
        filename = QFileDialog.getExistingDirectory(self, 'Seleccionar', self.textBox.text())
        if filename:
            self.textBox.setText(str(filename))
            self.Test.OnPathUpdate_Texts()
class DialogClasifModel(QWidget):
    def __init__(self,Test, name, parent=None):
        self.name = name
        self.Test = Test
        super(DialogClasifModel, self).__init__(parent)

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
    def GetPath(self):
        return self.textBox.text()
    def getfile(self):
        filename = QFileDialog.getOpenFileName(self, 'Abrir modelo', 'c:\\', "All files(*.*)")  # Text files (*.txt)
        if filename:
            self.textBox.setText(str(filename[0]))
            self.Test.OnPathUpdate_Model()