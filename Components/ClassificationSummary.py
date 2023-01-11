import sys
import os
import Components.PieChart as PieChart
from IA.LoadTrainingModel import LoadTrainingModel
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_score,recall_score,f1_score

class Summary(QWidget):

    def __init__(self, paths, parent=None):
        super(Summary, self).__init__(parent)
        masterLayout = QVBoxLayout()
        parentLayout = QHBoxLayout()
        layout = QGridLayout()
        pielayout = QGridLayout()
        self.paths = paths

        masterLayout.addLayout(parentLayout)
        parentLayout.addLayout(layout)
        parentLayout.addLayout(pielayout)



        self.titleLabel = QLabel("RESUMEN: ")
        self.titleFont = QtGui.QFont()
        self.titleFont.setBold(True)
        self.titleLabel.setFont(self.titleFont)



        self.label_totalTexts = QLabel("Total textos: ".format("0"))
        self.label_textsA = QLabel("Ejemplares Entrantes: {}".format("0"))
        self.label_textsB = QLabel("Ejemplares Principales: {}".format("0"))
        self.label_textsC = QLabel("Ejemplares Segundos: {}".format("0"))
        self.label_textsD = QLabel("Ejemplares Postres: {}".format("0"))

        self.label_totalTime = QLabel("Tiempo: {} segundos".format(""))

        layout.addWidget(self.label_totalTexts,1,0)
        layout.addWidget(self.label_textsA,2,0)
        layout.addWidget(self.label_textsB,3,0)
        layout.addWidget(self.label_textsC,4,0)
        layout.addWidget(self.label_textsD,5,0)
        layout.addWidget(self.label_totalTime,6,0)

        self.run_button = QPushButton('Ejecutar')
        masterLayout.addWidget(self.run_button)
        self.run_button.clicked.connect(self.Run)

        #piechart
        values = [("Entrantes", 10), ("Principales", 40), ("Segundos", 5), ("Postres", 120)]
        self.pieChart = PieChart.Pie(values)
        pielayout.addWidget(self.pieChart,0,0)

        self.setLayout(masterLayout)

    def Run(self):
        print("Running! ")
        if (self.paths[0] != "" and self.paths[1] != "" and self.paths[2] != ""):
            model, vectorizer = LoadTrainingModel.Load(self,self.paths[1],self.paths[2])
            for filepath in os.listdir(self.paths[0]):
                filename = '%s/%s' % (self.paths[0], str(filepath))
                with open(filename, 'rb') as file:
                    text = file.read().decode(errors='replace').replace('\n','')
                    text = [text]
                    test = vectorizer.transform(text)
                    prediction = model.predict(test)
                    print(filepath, prediction[0])
