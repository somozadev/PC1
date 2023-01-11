import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Components.RunButton as RunButton


class Preview(QWidget):
    def __init__(self, Training, values, paths, currentAlgorithm, parent=None):
        super(Preview, self).__init__(parent)

        self.Training = Training
        self.confusion_matrix = None
        self.setObjectName('previewBox')
        self.values = values
        self.paths = paths
        self.currentAlgorithm = currentAlgorithm
        layout_preview = QVBoxLayout()
        layout = QGridLayout()

        layout.addLayout(layout_preview, 0 ,0 )
        self.setLayout(layout)

        self.titleLabel = QLabel("VISTA PREVIA: ")
        self.titleFont = QtGui.QFont()
        self.titleFont.setBold(True)
        self.titleLabel.setFont(self.titleFont)

        self.label_A = QLabel("Ejemplares Entrantes: {}".format(self.values[0]))
        self.label_B = QLabel("Ejemplares Principales: {}".format(self.values[1]))
        self.label_C = QLabel("Ejemplares Segundos: {}".format(self.values[2]))
        self.label_D = QLabel("Ejemplares Postres: {}".format(self.values[3]))
        self.label_total = QLabel("Total: ".format(self.values[4]))
        self.chosen_algorithm = QLabel("Algoritmo seleccionado: {}".format(self.values[5]))


        layout.addWidget(self.titleLabel)
        layout.addWidget(self.label_A)
        layout.addWidget(self.label_B)
        layout.addWidget(self.label_C)
        layout.addWidget(self.label_D)
        layout.addWidget(self.label_total)
        layout.addWidget(self.chosen_algorithm)


        self.run_button = RunButton.RunButton(self, self.paths, self.currentAlgorithm)

        layout.addWidget(self.run_button, 8, 1)


    def UpdatePreviewValues(self, values):
        self.values = values
        self.label_A.setText("Ejemplares Entrantes: {}".format(self.values[0]))
        self.label_B.setText("Ejemplares Principales: {}".format(self.values[1]))
        self.label_C.setText("Ejemplares Segundos: {}".format(self.values[2]))
        self.label_D.setText("Ejemplares Postres: {}".format(self.values[3]))
        self.chosen_algorithm.setText("Algoritmo seleccionado: {}".format(self.values[4]))
        self.run_button.UpdateCurrentAlgorithm(self.values[4])

        total_files = int(self.values[0]) + int(self.values[1]) + int(self.values[2]) + int(self.values[3])
        self.label_total.setText("Total: {}".format(total_files))


    def PropagateConfusionMatrix(self, confusion_matrix):
        self.confusion_matrix = confusion_matrix
        self.Training.OnTrainingFinished(self.confusion_matrix)
        




