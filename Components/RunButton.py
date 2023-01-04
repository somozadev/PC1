import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import IA.ToDataset as Dataset
import IA.LowerToken as LowerToken
import IA.StopWords as StopWords
import IA.Stemming as Stemming

class RunButton(QWidget):

    def __init__(self, paths, parent=None):
        super(RunButton, self).__init__(parent)
        self.paths = paths
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.runButton = QPushButton("Ejecutar")
        self.runButton.clicked.connect(self.Run)
        layout.addWidget(self.runButton)

    def Run(self):
        print("Running! ")
        if(self.paths[0] != "" and self.paths[1] != "" and self.paths[2] != "" and self.paths[3] != ""):
            print(self.paths[0])
            print(self.paths[1])
            print(self.paths[2])
            print(self.paths[3])

            # self.Dataset = Dataset.ToDataset.
            # self.TokenizeLower = LowerToken.LowerToken.ToLowerTokenize()
            # self.Stemming = Stemming.Stemming.GetStemming()

