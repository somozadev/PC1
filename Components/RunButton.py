import sys
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import IA.ToDataset as Dataset
import IA.StopWords as StopWords
import IA.Stemming as Stemming
import IA.ToCsv as Csv
import IA.ToupleList as ToupleList
from IA.NaiveBayes import NaiveBayes
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

            if os.path.exists('CSV/test.csv') is False:
                self.csv = Csv.ToCsv().GenerateCSV('test',self.paths,['Entrantes','Primeros','Segundos','Postres'])

            self.touples_list = ToupleList.ToToupleList().GenerateToupleList('test')

            # ToupleList.ToToupleList().PrintFrequencyDistribution(self.touples_list)


            self.naive_bayes = NaiveBayes.Train(self,self.touples_list)
            # self.Dataset = Dataset.ToDataset.
            # self.TokenizeLower = LowerToken.LowerToken.ToLowerTokenize()
            # self.Stemming = Stemming.Stemming.GetStemming()


