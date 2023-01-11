import os.path
from PyQt5.QtWidgets import *
import IA.ToCsv as Csv
from IA.ToupleList import ToupleList

from IA.NaiveBayes import NaiveBayes
from IA.DecissionTree import DecisionTree
from IA.RandomForest import RandomForest
from IA.LinearSupportVector import LinearSupportVector
from IA.StochasticGradientDescent import StochasticGradientDescent
class RunButton(QWidget):

    def __init__(self, previewBox, paths, currentAlgorithm, parent=None):
        super(RunButton, self).__init__(parent)
        self.training_algorithm_dt = None
        self.training_algorithm_lsv = None
        self.training_algorithm_sgd = None
        self.training_algorithm_nb = None
        self.confusion_matrix = None
        self.paths = paths
        self.previewBox = previewBox
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
                self.training_algorithm_nb = NaiveBayes(self)
                self.training_algorithm_nb.Train(self.touples_list)

            elif self.currentAlgorithm == "Decision Tree":
                self.training_algorithm_dt = DecisionTree(self)
                self.training_algorithm_dt.Train(self.touples_list)

            elif self.currentAlgorithm == "Random Forest":
                self.training_algorithm_rf = RandomForest(self)
                self.training_algorithm_rf.Train(self.touples_list)

            elif self.currentAlgorithm == "Linear Support Vector":
                self.training_algorithm_lsv = LinearSupportVector(self)
                self.training_algorithm_lsv.Train(self.touples_list)

            elif self.currentAlgorithm == "Stochastic Gradient Descent":
                self.training_algorithm_sgd = StochasticGradientDescent(self)
                self.training_algorithm_sgd.Train(self.touples_list)

    def UpdatePreviewBox(self):
        self.previewBox.PropagateConfusionMatrix(self.confusion_matrix)

    def GetCurrentAlgorithm(self):
        return self.currentAlgorithm
    def UpdateCurrentAlgorithm(self,currentAlgorithm):
        self.currentAlgorithm = currentAlgorithm
    def GetConfusionMatrix(self):
        if self.currentAlgorithm == "Naive Bayes":
            self.confusion_matrix = self.training_algorithm_nb.GetConfusionMatrix()
            self.UpdatePreviewBox()

        elif self.currentAlgorithm == "Decision Tree":
            self.confusion_matrix = self.training_algorithm_dt.GetConfusionMatrix()
            self.UpdatePreviewBox()

        elif self.currentAlgorithm == "Random Forest":
            self.confusion_matrix = self.training_algorithm_rf.GetConfusionMatrix()
            self.UpdatePreviewBox()

        elif self.currentAlgorithm == "Linear Support Vector":
            self.confusion_matrix = self.training_algorithm_lsv.GetConfusionMatrix()
            self.UpdatePreviewBox()

        elif self.currentAlgorithm == "Stochastic Gradient Descent":
            self.confusion_matrix = self.training_algorithm_sgd.GetConfusionMatrix()
            self.UpdatePreviewBox()
