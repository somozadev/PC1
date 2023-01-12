import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import subprocess
from PyQt5.QtCore import Qt


class Results(QWidget):

    def __init__(self,Test, pathTexts, parent=None):
        super(Results, self).__init__(parent)

        self.filename = None
        self.Test = Test
        self.layout = QVBoxLayout()
        self.pathTexts = pathTexts
        self.layout.setAlignment(Qt.AlignHCenter)

        self.h_layout = QHBoxLayout()
        self.h_layout.setAlignment(Qt.AlignHCenter)
        self.v_layout_temp = QVBoxLayout()
        self.box_group = QGroupBox()
        self.scroll_area = QScrollArea()


        self.label_text_title = QLabel("\t Texto")
        self.label_category_title = QLabel("\t\t Categoría")
        self.label_view_title = QLabel("\t\t Ver Texto")
        self.label_text_title.setFixedSize(300,25)
        self.label_view_title.setFixedSize(300,25)
        self.label_category_title.setFixedSize(300,25)
        self.label_text_title.setObjectName("borderLabel")
        self.label_category_title.setObjectName("borderLabel")
        self.label_view_title.setObjectName("borderLabel")

        self.h_layout.addWidget(self.label_text_title)
        self.h_layout.addWidget(self.label_category_title)
        self.h_layout.addWidget(self.label_view_title)

        self.layout.addLayout(self.h_layout)

        self.setLayout(self.layout)




    def DisplayWhenExecuteTest(self, temppath):

        self.pathTexts = temppath
        count = 0
        arrayNames = []



        for dir in os.listdir(self.pathTexts):
            for path in os.listdir(os.path.join(self.pathTexts, dir)):
                if os.path.isfile(os.path.join(self.pathTexts, dir, path)):
                    fullpath = os.path.join(self.pathTexts, dir)
                    fullpath+= '\\{}'.format(path)
                    arrayNames.append((os.path.basename(os.path.join(self.pathTexts, path)), dir, fullpath)) #saves file path + its category
                    count += 1



        for i in range(count):
            self.AddLableToResults(arrayNames[i])

        self.box_group.setLayout(self.v_layout_temp)
        self.scroll_area.setWidget(self.box_group)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedHeight(250)
        self.scroll_area.setFixedWidth(900)

        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)

        self.Test.FinishedDisplayTexts()

    def OpenFile(self, filename):
        print(filename)
        subprocess.Popen([filename[2]], shell = True)


    def AddLableToResults(self, fileName):
        self.filename = fileName
        self.label_name = QLabel(fileName[0])
        self.label_name.setObjectName("totalLabel")
        self.label_category = QLabel(fileName[1])
        self.label_category.setObjectName("totalLabel")

        self.view_button = QPushButton("Ver")
        self.view_button.setObjectName("resultLabel")
        self.view_button.clicked.connect(lambda state, x=fileName: self.OpenFile(x))
        self.label_name.setFixedSize(300,25)
        self.label_category.setFixedSize(300,25)
        self.view_button.setFixedSize(200,25)

        self.label_category.setAlignment(Qt.AlignHCenter)

        self.h_layout = QHBoxLayout()
        self.h_layout.setAlignment(Qt.AlignHCenter)
        self.h_layout.addWidget(self.label_name)
        self.h_layout.addWidget(self.label_category)
        self.h_layout.addWidget(self.view_button)

        self.v_layout_temp.addLayout(self.h_layout)
