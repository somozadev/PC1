import os.path
from PyQt5.QtWidgets import *
import IA.ToCsv as Csv
from IA.ToupleList import ToupleList
from IA.NaiveBayes import NaiveBayes
from IA.DecissionTree import DecisionTree
from IA.LinearSupportVector import LinearSupportVector
from IA.StochasticGradientDescent import StochasticGradientDescent
class RunButton(QWidget):

    def __init__(self, paths, currentAlgorithm, parent=None):
        super(RunButton, self).__init__(parent)
        self.training_algorithm = None
        self.paths = paths
        self.currentAlgorithm = currentAlgorithm
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.runButton = QPushButton("Ejecutar")
        self.runButton.clicked.connect(self.Run)
        layout.addWidget(self.runButton)
    def Run(self):
        print("Running! ")
        if(self.paths[0] != "" and self.paths[1] != "" and self.paths[2] != "" and self.paths[3] != ""):

            if os.path.exists('CSV/test.csv') is False:
                self.csv = Csv.ToCsv().GenerateCSV('test',self.paths,['Entrantes','Primeros','Segundos','Postres']) #generate csv

            self.touples_list = ToupleList.GenerateToupleList(self,'test') #generate dataset (array of touples (label,text)

            #ToupleList.PrintFrequencyDistribution(self, self.touples_list) #prints the frequency distribution for each token in each label

            if self.currentAlgorithm == "Naive Bayes":
                self.training_algorithm = NaiveBayes.Train(self, self.touples_list)
            elif self.currentAlgorithm == "Decision Tree":
                self.training_algorithm = DecisionTree.Train(self, self.touples_list)
            elif self.currentAlgorithm == "Linear Support Vector":
                self.training_algorithm = LinearSupportVector.Train(self, self.touples_list)
            elif self.currentAlgorithm == "Stochastic Gradient Descent":
                self.training_algorithm = StochasticGradientDescent.Train(self, self.touples_list)



    def UpdateCurrentAlgorithm(self,currentAlgorithm):
        self.currentAlgorithm = currentAlgorithm