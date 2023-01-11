import sys

from PyQt5 import QtGui
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Result(QWidget):
    def __init__(self, values, parent=None):
        super(Result, self).__init__(parent)

        self.values = values
        layout = QVBoxLayout()
        grid_layout_result = QGridLayout()

        self.setLayout(layout)

        self.titleLabel = QLabel("Resultado: ")
        self.titleFont = QtGui.QFont()
        self.titleFont.setBold(True)
        self.titleLabel.setFont(self.titleFont)

        self.excel = QGroupBox()

        self.label_TrueEntrante = QLabel("True Entrante")
        self.label_TruePrincipal = QLabel("True Principal")
        self.label_TrueSegundo = QLabel("True Segundo")
        self.label_TruePostre = QLabel("True Postre")

        self.label_TrueEntrante.setObjectName("borderLabel")
        self.label_TruePrincipal.setObjectName("borderLabel")
        self.label_TrueSegundo.setObjectName("borderLabel")
        self.label_TruePostre.setObjectName("borderLabel")

        self.label_ClassTotal = QLabel("Total")
        self.label_ClassPrecision = QLabel("Class recall")

        self.label_ClassTotal.setObjectName("borderLabel")
        self.label_ClassPrecision.setObjectName("borderLabel")

        self.label_PredEntrante = QLabel("Pred. Entrante")
        self.label_PredPrincipal = QLabel("Pred. Principal")
        self.label_PredSegundo = QLabel("Pred. Segundo")
        self.label_PredPostre = QLabel("Pred. Postre")

        self.label_PredEntrante.setObjectName("borderLabel")
        self.label_PredPrincipal.setObjectName("borderLabel")
        self.label_PredSegundo.setObjectName("borderLabel")
        self.label_PredPostre.setObjectName("borderLabel")

        self.label_PredTotal = QLabel("Total")
        self.label_ClassRecall = QLabel("Class precision")

        self.label_PredTotal.setObjectName("borderLabel")
        self.label_ClassRecall.setObjectName("borderLabel")


        self.label_TrueEntrante_PredEntrante = QLabel("{}".format(0))
        self.label_TruePrincipal_PredEntrante = QLabel("{}".format(0))
        self.label_TrueSegundo_PredEntrante = QLabel("{}".format(0))
        self.label_TruePostre_PredEntrante = QLabel("{}".format(0))

        self.label_TrueEntrante_PredPrincipal = QLabel("{}".format(0))
        self.label_TruePrincipal_PredPrincipal = QLabel("{}".format(0))
        self.label_TrueSegundo_PredPrincipal = QLabel("{}".format(0))
        self.label_TruePostre_PredPrincipal = QLabel("{}".format(0))

        self.label_TrueEntrante_PredSegundo = QLabel("{}".format(0))
        self.label_TruePrincipal_PredSegundo = QLabel("{}".format(0))
        self.label_TrueSegundo_PredSegundo = QLabel("{}".format(0))
        self.label_TruePostre_PredSegundo = QLabel("{}".format(0))

        self.label_TrueEntrante_PredPostre = QLabel("{}".format(0))
        self.label_TruePrincipal_PredPostre = QLabel("{}".format(0))
        self.label_TrueSegundo_PredPostre = QLabel("{}".format(0))
        self.label_TruePostre_PredPostre = QLabel("{}".format(0))



        self.label_TrueEntrante_Total = QLabel("{}".format(0))
        self.label_TruePrincipal_Total = QLabel("{}".format(0))
        self.label_TrueSegundo_Total = QLabel("{}".format(0))
        self.label_TruePostre_Total = QLabel("{}".format(0))

        self.label_TrueEntrante_Total.setObjectName("resultLabel")
        self.label_TruePrincipal_Total.setObjectName("resultLabel")
        self.label_TrueSegundo_Total.setObjectName("resultLabel")
        self.label_TruePostre_Total.setObjectName("resultLabel")


        self.label_TrueEntrante_classRecall = QLabel("{}%".format(0))
        self.label_TruePrincipal_classRecall = QLabel("{}%".format(0))
        self.label_TrueSegundo_classRecall = QLabel("{}%".format(0))
        self.label_TruePostre_classRecall = QLabel("{}%".format(0))

        self.label_TrueEntrante_classRecall.setObjectName("resultLabel")
        self.label_TruePrincipal_classRecall.setObjectName("resultLabel")
        self.label_TrueSegundo_classRecall.setObjectName("resultLabel")
        self.label_TruePostre_classRecall.setObjectName("resultLabel")

        self.label_PredEntrante_Total = QLabel("{}".format(0))
        self.label_PredPrincipal_Total = QLabel("{}".format(0))
        self.label_PredSegundo_Total = QLabel("{}".format(0))
        self.label_PredPostre_Total = QLabel("{}".format(0))

        self.label_PredEntrante_Total.setObjectName("resultLabel")
        self.label_PredPrincipal_Total.setObjectName("resultLabel")
        self.label_PredSegundo_Total.setObjectName("resultLabel")
        self.label_PredPostre_Total.setObjectName("resultLabel")

        self.label_predTotal_total = QLabel("{}".format(0))

        self.label_predTotal_total.setObjectName("resultLabel")

        self.label_predEntrante_classPrecision = QLabel("{}%".format(0))
        self.label_predPrincipal_classPrecision = QLabel("{}%".format(0))
        self.label_predSegundo_classPrecision = QLabel("{}%".format(0))
        self.label_predPostre_classPrecision = QLabel("{}%".format(0))

        self.label_predEntrante_classPrecision.setObjectName("resultLabel")
        self.label_predPrincipal_classPrecision.setObjectName("resultLabel")
        self.label_predSegundo_classPrecision.setObjectName("resultLabel")
        self.label_predPostre_classPrecision.setObjectName("resultLabel")

        grid_layout_result.addWidget(self.label_TrueEntrante,0,1)
        grid_layout_result.addWidget(self.label_TruePrincipal,0,2)
        grid_layout_result.addWidget(self.label_TrueSegundo,0,3)
        grid_layout_result.addWidget(self.label_TruePostre,0,4)
        grid_layout_result.addWidget(self.label_ClassTotal,0,5)
        grid_layout_result.addWidget(self.label_ClassPrecision,0,6)

        grid_layout_result.addWidget(self.label_PredEntrante,1,0)
        grid_layout_result.addWidget(self.label_TrueEntrante_PredEntrante,1,1)
        grid_layout_result.addWidget(self.label_TruePrincipal_PredEntrante,1,2)
        grid_layout_result.addWidget(self.label_TrueSegundo_PredEntrante,1,3)
        grid_layout_result.addWidget(self.label_TruePostre_PredEntrante,1,4)
        grid_layout_result.addWidget(self.label_PredEntrante_Total,1,5)
        grid_layout_result.addWidget(self.label_predEntrante_classPrecision,1,6)

        grid_layout_result.addWidget(self.label_PredPrincipal,2,0)
        grid_layout_result.addWidget(self.label_TrueEntrante_PredPrincipal,2,1)
        grid_layout_result.addWidget(self.label_TruePrincipal_PredPrincipal,2,2)
        grid_layout_result.addWidget(self.label_TrueSegundo_PredPrincipal,2,3)
        grid_layout_result.addWidget(self.label_TruePostre_PredPrincipal,2,4)
        grid_layout_result.addWidget(self.label_PredPrincipal_Total,2,5)
        grid_layout_result.addWidget(self.label_predPrincipal_classPrecision,2,6)

        grid_layout_result.addWidget(self.label_PredSegundo,3,0)
        grid_layout_result.addWidget(self.label_TrueEntrante_PredSegundo,3,1)
        grid_layout_result.addWidget(self.label_TruePrincipal_PredSegundo,3,2)
        grid_layout_result.addWidget(self.label_TrueSegundo_PredSegundo,3,3)
        grid_layout_result.addWidget(self.label_TruePostre_PredSegundo,3,4)
        grid_layout_result.addWidget(self.label_PredSegundo_Total,3,5)
        grid_layout_result.addWidget(self.label_predSegundo_classPrecision,3,6)

        grid_layout_result.addWidget(self.label_PredPostre,4,0)
        grid_layout_result.addWidget(self.label_TrueEntrante_PredPostre,4,1)
        grid_layout_result.addWidget(self.label_TruePrincipal_PredPostre,4,2)
        grid_layout_result.addWidget(self.label_TrueSegundo_PredPostre,4,3)
        grid_layout_result.addWidget(self.label_TruePostre_PredPostre,4,4)
        grid_layout_result.addWidget(self.label_PredPostre_Total,4,5)
        grid_layout_result.addWidget(self.label_predPostre_classPrecision,4,6)


        grid_layout_result.addWidget(self.label_PredTotal,5,0)
        grid_layout_result.addWidget(self.label_TrueEntrante_Total,5,1)
        grid_layout_result.addWidget(self.label_TruePrincipal_Total,5,2)
        grid_layout_result.addWidget(self.label_TrueSegundo_Total,5,3)
        grid_layout_result.addWidget(self.label_TruePostre_Total,5,4)
        grid_layout_result.addWidget(self.label_predTotal_total,5,5)

        grid_layout_result.addWidget(self.label_ClassRecall,6,0)
        grid_layout_result.addWidget(self.label_TrueEntrante_classRecall,6,1)
        grid_layout_result.addWidget(self.label_TruePrincipal_classRecall,6,2)
        grid_layout_result.addWidget(self.label_TrueSegundo_classRecall,6,3)
        grid_layout_result.addWidget(self.label_TruePostre_classRecall,6,4)

        layout.addLayout(grid_layout_result)






    def UpdatePreviewValues(self, values):
        self.values = values
        self.label_TrueEntrante_PredEntrante.setText("{}".format(self.values[0][0]))
        self.label_TruePrincipal_PredEntrante.setText("{}".format(self.values[0][1]))
        self.label_TrueSegundo_PredEntrante.setText("{}".format(self.values[0][2]))
        self.label_TruePostre_PredEntrante.setText("{}".format(self.values[0][3]))

        self.label_TrueEntrante_PredPrincipal.setText("{}".format(self.values[1][0]))
        self.label_TruePrincipal_PredPrincipal.setText("{}".format(self.values[1][1]))
        self.label_TrueSegundo_PredPrincipal.setText("{}".format(self.values[1][2]))
        self.label_TruePostre_PredPrincipal.setText("{}".format(self.values[1][3]))

        self.label_TrueEntrante_PredSegundo.setText("{}".format(self.values[2][0]))
        self.label_TruePrincipal_PredSegundo.setText("{}".format(self.values[2][1]))
        self.label_TrueSegundo_PredSegundo.setText("{}".format(self.values[2][2]))
        self.label_TruePostre_PredSegundo.setText("{}".format(self.values[2][3]))

        self.label_TrueEntrante_PredPostre.setText("{}".format(self.values[3][0]))
        self.label_TruePrincipal_PredPostre.setText("{}".format(self.values[3][1]))
        self.label_TrueSegundo_PredPostre.setText("{}".format(self.values[3][2]))
        self.label_TruePostre_PredPostre.setText("{}".format(self.values[3][3]))

        trueEntrante_recall_total = self.values[0][0] + self.values[1][0] + self.values[2][0] + self.values[3][0]
        truePrincipal_recall_total = self.values[0][1] + self.values[1][1] + self.values[2][1] + self.values[3][1]
        trueSegundo_recall_total = self.values[0][2] + self.values[1][2] + self.values[2][2] + self.values[3][2]
        truePostre_recall_total = self.values[0][3] + self.values[1][3] + self.values[2][3] + self.values[3][3]

        self.label_TrueEntrante_Total.setText("{}".format(trueEntrante_recall_total))
        self.label_TruePrincipal_Total.setText("{}".format(truePrincipal_recall_total))
        self.label_TrueSegundo_Total.setText("{}".format(trueSegundo_recall_total))
        self.label_TruePostre_Total.setText("{}".format(truePostre_recall_total))


        self.label_TrueEntrante_classRecall.setText(
            "{}%".format(round((self.values[0][0] / trueEntrante_recall_total) * 100), 2))
        self.label_TruePrincipal_classRecall.setText(
            "{}%".format(round((self.values[1][1] / truePrincipal_recall_total) * 100), 2))
        self.label_TrueSegundo_classRecall.setText(
            "{}%".format(round((self.values[2][2] / trueSegundo_recall_total) * 100), 2))
        self.label_TruePostre_classRecall.setText(
            "{}%".format(round((self.values[3][3] / truePostre_recall_total) * 100), 2))

        trueEntrante_precission_total = self.values[0][0] + self.values[0][1] + self.values[0][2] + self.values[0][3]
        truePrincipal_precission_total = self.values[1][0] + self.values[1][1] + self.values[1][2] + self.values[1][3]
        trueSegundo_precission_total = self.values[2][0] + self.values[2][1] + self.values[2][2] + self.values[2][3]
        truePostre_precission_total = self.values[3][0] + self.values[3][1] + self.values[3][2] + self.values[3][3]

        self.label_PredEntrante_Total.setText("{}".format(trueEntrante_precission_total))
        self.label_PredPrincipal_Total.setText("{}".format(truePrincipal_precission_total))
        self.label_PredSegundo_Total.setText("{}".format(trueSegundo_precission_total))
        self.label_PredPostre_Total.setText("{}".format(truePostre_precission_total))

        self.label_predTotal_total.setText("{}".format(
            trueEntrante_precission_total + truePrincipal_precission_total + trueSegundo_precission_total + truePostre_precission_total))

        self.label_predEntrante_classPrecision.setText(
            "{}%".format(round((self.values[0][0] / trueEntrante_precission_total) * 100), 2))
        self.label_predPrincipal_classPrecision.setText(
            "{}%".format(round((self.values[1][1] / truePrincipal_precission_total) * 100), 2))
        self.label_predSegundo_classPrecision.setText(
            "{}%".format(round((self.values[2][2] / trueSegundo_precission_total) * 100), 2))
        self.label_predPostre_classPrecision.setText(
            "{}%".format(round((self.values[3][3] / truePostre_precission_total) * 100), 2))

