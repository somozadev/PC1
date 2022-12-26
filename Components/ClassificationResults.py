import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Results(QWidget):

    def __init__(self, name, pathTexts, parent=None):
        super(Results, self).__init__(parent)

        layout = QGridLayout()
        self.setLayout(layout)
        self.name = name
        self.pathTexts = pathTexts
        layout.setAlignment(Qt.AlignVCenter)

        self.label_text_title = QLabel("Texto")
        self.label_category_title = QLabel("Categoría")
        self.label_view_title = QLabel("Ver Texto")
        self.label_text_title.setObjectName("borderLabel")
        self.label_category_title.setObjectName("borderLabel")
        self.label_view_title.setObjectName("borderLabel")
        layout.addWidget(self.label_text_title, 0, 0)
        layout.addWidget(self.label_category_title, 0, 1)
        layout.addWidget(self.label_view_title, 0, 2)

        count = 0
        arrayNames = []
        for path in os.listdir(self.pathTexts):
            if os.path.isfile(os.path.join(self.pathTexts, path)):
                print(os.path.basename(os.path.join(self.pathTexts, path)))
                arrayNames.append(os.path.basename(os.path.join(self.pathTexts, path)))
                count += 1

        excelCounter = 0
        x = 1
        for i in range(count):
            if excelCounter >= 3:
                x += 1
                excelCounter = 0
            self.addLableToResults(layout, x, excelCounter, arrayNames[i][0:3])
            excelCounter += 1




    def addLableToResults(self, layout, x, y, fileName):

        if y >= 2:
            self.label = QLabel("Ver")
            self.label.setObjectName("resultLabel")
        else:
            self.label = QLabel(fileName)
            self.label.setObjectName("totalLabel")


        layout.addWidget(self.label, x, y);
