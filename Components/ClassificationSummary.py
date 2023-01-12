import sys
import os
import Components.PieChart as PieChart
from IA.LoadTrainingModel import LoadTrainingModel
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import tempfile
import shutil
import pickle

class Summary(QWidget):

    def __init__(self, Test, paths, parent=None):
        super(Summary, self).__init__(parent)
        masterLayout = QVBoxLayout()
        parentLayout = QHBoxLayout()
        layout = QGridLayout()
        pielayout = QGridLayout()
        self.paths = paths
        self.Test = Test
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


        layout.addWidget(self.label_totalTexts,1,0)
        layout.addWidget(self.label_textsA,2,0)
        layout.addWidget(self.label_textsB,3,0)
        layout.addWidget(self.label_textsC,4,0)
        layout.addWidget(self.label_textsD,5,0)

        self.run_button = QPushButton('Ejecutar')
        masterLayout.addWidget(self.run_button)
        self.run_button.clicked.connect(self.Run)

        #piechart
        values = [("Entrantes", 0), ("Principales", 0), ("Segundos", 0), ("Postres", 0)]
        self.pieChart = PieChart.Pie(values)
        pielayout.addWidget(self.pieChart,0,0)

        self.setLayout(masterLayout)

    def Run(self):
        print("Running! ")
        if (self.paths[0] != "" and self.paths[1] != "" and self.paths[2] != ""):
            model, vectorizer = LoadTrainingModel.Load(self,self.paths[1],self.paths[2])

            self.tempfile = tempfile.TemporaryDirectory()
            os.mkdir(self.tempfile.name + "\Entrantes")
            os.mkdir(self.tempfile.name + "\Primeros")
            os.mkdir(self.tempfile.name + "\Segundos")
            os.mkdir(self.tempfile.name + "\Postres")

            for filepath in os.listdir(self.paths[0]):
                filename = '%s/%s' % (self.paths[0], str(filepath))
                with open(filename, 'rb') as file:
                    text = file.read().decode(errors='replace').replace('\n','')
                    text = [text]
                    test = vectorizer.transform(text)
                    prediction = model.predict(test)
                    print(filepath, prediction[0])
                    self.SaveOutputInTemp(filepath ,filename, prediction[0])

            self.Test.FinishedTesting()

                    #call update results and path from above
                   #update pychart

    def UpdatePreviewAmountTexts(self):
        path_a = self.GetTempPath() + '\Entrantes'
        path_b = self.GetTempPath() + '\Primeros'
        path_c = self.GetTempPath() + '\Segundos'
        path_d = self.GetTempPath() + '\Postres'
        list = os.listdir(path_a)
        number_files_a = len(list)
        self.label_textsA.setText("Ejemplares Entrantes: {}".format(str(number_files_a)))
        list = os.listdir(path_b)
        number_files_b = len(list)
        self.label_textsB.setText("Ejemplares Principales: {}".format(str(number_files_b)))
        list = os.listdir(path_c)
        number_files_c = len(list)
        self.label_textsC.setText("Ejemplares Segundos: {}".format(str(number_files_c)))
        list = os.listdir(path_d)
        number_files_d = len(list)
        self.label_textsD.setText("Ejemplares Postres: {}".format(str(number_files_d)))

        self.label_totalTexts.setText("Total textos: {}".format(str(number_files_a + number_files_b + number_files_c + number_files_d)))

        values = [("Entrantes", number_files_a), ("Principales", number_files_b), ("Segundos", number_files_c), ("Postres", number_files_d)]
        self.pieChart.UpdateValues(values)


    def SaveOutputInTemp(self, filename, path, prediction):

                if prediction == 'Entrantes':
                    shutil.copy(path,self.tempfile.name+'\Entrantes\{}'.format(filename))
                elif prediction == 'Primeros':
                    shutil.copy(path,self.tempfile.name+'\Primeros\{}'.format(filename))
                elif prediction == 'Segundos':
                    shutil.copy(path,self.tempfile.name+'\Segundos\{}'.format(filename))
                elif prediction == 'Postres':
                    shutil.copy(path,self.tempfile.name+'\Postres\{}'.format(filename))

    def GetTempPath(self):
        return self.tempfile.name
    def GetTempFile(self):
        return self.tempfile
    def SaveOutputToPath(self, finalpath):
        pass
        #self.tempfile.cleanup()


