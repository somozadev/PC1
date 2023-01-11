import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Dropdown(QWidget):

    def GetCurrentAlgorithm(self):
        content =  self.dropdown.currentText()
        return content
    def UpdateCurrentAlgorithm(self):
        self.Training.OnDropdownUpdate()

    def __init__(self, Training, parent=None):
        super(Dropdown, self).__init__(parent)
        self.Training = Training

        layout = QGridLayout()
        self.setLayout(layout)

        self.textLabel = QLabel("Seleccionar Algoritmo: ")
        layout.addWidget(self.textLabel, 0, 0)

        self.dropdown = QComboBox()
        self.dropdown.addItems(['Naive Bayes','Decision Tree', 'Linear Support Vector', 'Stochastic Gradient Descent'])
        self.dropdown.currentTextChanged.connect(self.UpdateCurrentAlgorithm)
        layout.addWidget(self.dropdown, 0, 1)
