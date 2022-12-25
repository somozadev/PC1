import sys

from PyQt5 import QtGui
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Components.RunButton as RunButton


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
        self.label_TrueYes = QLabel("True Yes")
        self.label_TrueNo = QLabel("True No")
        self.label_ClassTotal = QLabel("Total")
        self.label_ClassPrecision = QLabel("Class precision")
        self.label_PredYes = QLabel("Pred. Yes")
        self.label_PredNo = QLabel("Pred. No")
        self.label_PredTotal = QLabel("Total")
        self.label_ClassRecall = QLabel("Class recall")
        self.label_TrueYes.setObjectName("borderLabel")
        self.label_TrueNo.setObjectName("borderLabel")
        self.label_ClassTotal.setObjectName("borderLabel")
        self.label_ClassPrecision.setObjectName("borderLabel")
        self.label_PredYes.setObjectName("borderLabel")
        self.label_PredNo.setObjectName("borderLabel")
        self.label_PredTotal.setObjectName("borderLabel")
        self.label_ClassRecall.setObjectName("borderLabel")


        self.label_TrueYes_PredYes = QLabel("{}".format(self.values[0]))
        self.label_TrueNo_PredYes = QLabel("{}".format(self.values[1]))
        self.label_TrueYes_PredNo = QLabel("{}".format(self.values[2]))
        self.label_TrueNo_PredNo = QLabel("{}".format(self.values[3]))



        trueYes_recall_total = self.values[0] + self.values[2]
        trueNo_recall_total = self.values[1] + self.values[3]

        self.label_TrueYes_Total = QLabel("{}".format(trueYes_recall_total))
        self.label_TrueNo_Total = QLabel("{}".format(trueNo_recall_total))

        self.label_TrueYes_classRecall = QLabel("{}%".format(round((self.values[0] / trueYes_recall_total)*100),2))
        self.label_TrueYes_classRecall.setObjectName("resultLabel")
        self.label_TrueNo_classRecall = QLabel("{}%".format(round((self.values[3] / trueNo_recall_total)*100),2))
        self.label_TrueNo_classRecall.setObjectName("resultLabel")

        trueYes_total = self.values[0] + self.values[2]
        trueNo_total = self.values[1] + self.values[3]
        trueYes_pred_total = self.values[0] + self.values[1]
        trueNo_pred_total = self.values[2] + self.values[3]

        self.label_PredTotal_yes = QLabel("{}".format(trueYes_pred_total))
        self.label_PredTotal_yes.setObjectName("totalLabel")
        self.label_PredTotal_no = QLabel("{}".format(trueNo_pred_total))
        self.label_PredTotal_no.setObjectName("totalLabel")
        self.label_predTotal_total = QLabel("{}".format(trueYes_recall_total + trueNo_recall_total))
        self.label_predTotal_total.setObjectName("totalLabel")

        self.label_predYes_classPrecision = QLabel("{}%".format(round((self.values[0] / trueYes_pred_total)* 100),2))
        self.label_predYes_classPrecision.setObjectName("resultLabel")
        self.label_predNo_classPrecision = QLabel("{}%".format(round((self.values[3] / trueNo_pred_total)*100),2))
        self.label_predNo_classPrecision.setObjectName("resultLabel")

        grid_layout_result.addWidget(self.label_TrueYes,0,1)
        grid_layout_result.addWidget(self.label_TrueNo,0,2)
        grid_layout_result.addWidget(self.label_ClassTotal,0,3)
        grid_layout_result.addWidget(self.label_ClassPrecision,0,4)

        grid_layout_result.addWidget(self.label_PredYes,1,0)
        grid_layout_result.addWidget(self.label_TrueYes_PredYes,1,1)
        grid_layout_result.addWidget(self.label_TrueNo_PredYes,1,2)
        grid_layout_result.addWidget(self.label_PredTotal_yes,1,3)
        grid_layout_result.addWidget(self.label_predYes_classPrecision,1,4)

        grid_layout_result.addWidget(self.label_PredNo,2,0)
        grid_layout_result.addWidget(self.label_TrueYes_PredNo,2,1)
        grid_layout_result.addWidget(self.label_TrueNo_PredNo,2,2)
        grid_layout_result.addWidget(self.label_PredTotal_no,2,3)
        grid_layout_result.addWidget(self.label_predNo_classPrecision,2,4)

        grid_layout_result.addWidget(self.label_PredTotal,3,0)
        self.sumTrueYes = QLabel("{}".format(trueYes_total))
        self.sumTrueYes.setObjectName("totalLabel")
        grid_layout_result.addWidget(self.sumTrueYes,3,1)
        self.sumTrueNo = QLabel("{}".format(trueNo_total))
        self.sumTrueNo.setObjectName("totalLabel")
        grid_layout_result.addWidget(self.sumTrueNo,3,2)
        grid_layout_result.addWidget(self.label_predTotal_total,3,3)

        grid_layout_result.addWidget(self.label_ClassRecall,4,0)
        grid_layout_result.addWidget(self.label_TrueYes_classRecall,4,1)
        grid_layout_result.addWidget(self.label_TrueNo_classRecall,4,2)

        self.setStyleSheet(Path('Components/ResultBox.css').read_text())
        layout.addLayout(grid_layout_result)



    def UpdatePreviewValues(self, values):
        self.values = values
        self.label_A.setText("Ejemplares Entrantes: {}".format(self.values[0]))
        self.label_B.setText("Ejemplares Entrantes: {}".format(self.values[1]))
        self.label_C.setText("Ejemplares Entrantes: {}".format(self.values[2]))
        self.label_D.setText("Ejemplares Entrantes: {}".format(self.values[3]))
        self.label_total.setText("Total: ".format(self.values[4]))
        self.chosen_algorithm.setText("Algoritmo seleccionado: {}".format(self.values[5]))
