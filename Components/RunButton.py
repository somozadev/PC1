import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import IA.ToDataset as ToDataset
import IA.Stemming as Stemming

class RunButton(QWidget):

    def __init__(self, parent=None):
        super(RunButton, self).__init__(parent)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.runButton = QPushButton("Ejecutar")
        self.runButton.clicked.connect(self.Run)
        layout.addWidget(self.runButton)

    def Run(self):
        print("Running! ")
        #llamar a la parte de IA de training

        #paths


        self.Stemming = Stemming()
        