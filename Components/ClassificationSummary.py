import sys
import os
import Components.PieChart as PieChart

from PyQt5 import QtGui
from PyQt5.QtWidgets import *


class Summary(QWidget):

    def __init__(self, parent=None):
        super(Summary, self).__init__(parent)
        masterLayout = QVBoxLayout()
        parentLayout = QHBoxLayout()
        layout = QGridLayout()
        pielayout = QGridLayout()


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


        #piechart
        values = [("Entrantes", 10), ("Principales", 40), ("Segundos", 5), ("Postres", 120)]
        self.pieChart = PieChart.Pie(values)
        pielayout.addWidget(self.pieChart,0,0)

        self.setLayout(masterLayout)