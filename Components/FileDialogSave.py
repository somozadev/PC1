import sys
from PyQt5.QtWidgets import *
from IA.SaveTrainingModel import SaveTrainingModel
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Dialog(QWidget):

    def __init__(self, name, parent=None):
        super(Dialog, self).__init__(parent)

        layout = QGridLayout()
        self.setLayout(layout)
        self.name = name

        self.fileLabel = QLabel("{}: ".format(self.name))
        layout.addWidget(self.fileLabel, 0, 0)

        self.textBox = QLineEdit("")
        layout.addWidget(self.textBox, 0, 1)

        self.getFilesButton = QPushButton("Guardar")
        self.getFilesButton.clicked.connect(self.savefile)
        layout.addWidget(self.getFilesButton, 0, 2)

    def savefile(self):
        filename = QFileDialog.getSaveFileName(self, 'Guardar modelo', 'c:\\', "(*.pkl)")
        filename
        SaveTrainingModel.FinalSavingPathChosen(SaveTrainingModel, filename[0])
