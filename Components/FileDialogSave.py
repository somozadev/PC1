import errno
import os.path
import shutil
from PyQt5.QtWidgets import *
from IA.SaveTrainingModel import SaveTrainingModel


class Dialog(QWidget):

    def __init__(self, name, parent=None):
        super(Dialog, self).__init__(parent)

        layout = QGridLayout()
        self.setLayout(layout)
        self.name = name

        self.fileLabel = QLabel("{}: ".format(self.name))
        layout.addWidget(self.fileLabel, 0, 0)

        self.textBox = QLineEdit("")
        layout.addWidget(self.textBox, 0, 1)

        self.getFilesButton = QPushButton("Guardar")
        self.getFilesButton.clicked.connect(self.savefile)
        layout.addWidget(self.getFilesButton, 0, 2)

    def savefile(self):
        filename = QFileDialog.getSaveFileName(self, 'Guardar modelo', 'c:\\', "(*.pkl)")
        SaveTrainingModel.FinalSavingPathChosen(SaveTrainingModel, filename[0])
        self.textBox.setText(str(filename[0]))


class DialogTexts(QWidget):
    def __init__(self, name, tempPath, tempfile, parent=None):

        super(DialogTexts, self).__init__(parent)
        layout = QGridLayout()
        self.setLayout(layout)
        self.name = name
        self.tempPath = tempPath
        self.tempfile = tempfile
        self.fileLabel = QLabel("{}:".format(self.name))
        layout.addWidget(self.fileLabel, 0, 0)

        self.textBox = QLineEdit("")
        layout.addWidget(self.textBox, 0, 1)

        self.getFilesButton = QPushButton("Guardar")
        self.getFilesButton.clicked.connect(self.savefile)
        layout.addWidget(self.getFilesButton, 0, 2)

    def UpdateTempVars(self, tempPath, tempfile):
        self.tempPath = tempPath
        self.tempfile = tempfile
    def savefile(self):
        if self.tempPath == '':
            return
        filename = QFileDialog.getExistingDirectory(self, 'Seleccionar', self.textBox.text())
        try:
            if os.path.exists(filename):
                shutil.rmtree(filename)
                shutil.copytree(self.tempPath,filename)
        except OSError as e:
            if e.errno == errno.ENOTDIR:
                shutil.copy(self.tempPath,filename)
        self.textBox.setText(str(filename))
        # self.tempfile.cleanup()
