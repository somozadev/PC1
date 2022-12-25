from PyQt5.QtWidgets import *
import Components.FileDialogOpen as FileDialogOpen
import Components.FileDialogSave as FileDialogSave
import Components.Dropdown as Dropdown
import Components.PreviewBox as PreviewBox
import Components.ResultsBox as ResultBox
from pathlib import Path
import sys


class Training(QWidget):
    def __init__(self, parent=None):
        super(Training, self).__init__(parent)
        layout = QGridLayout()
        self.setLayout(layout)


        #select folders all categories
        self.file_browser_A = FileDialogOpen.Dialog('Entrantes')
        self.file_browser_B = FileDialogOpen.Dialog('Principales')
        self.file_browser_C = FileDialogOpen.Dialog('Segundos')
        self.file_browser_D = FileDialogOpen.Dialog('Postres')
        layout.addWidget(self.file_browser_A, 0, 0)
        layout.addWidget(self.file_browser_B, 1, 0)
        layout.addWidget(self.file_browser_C, 2, 0)
        layout.addWidget(self.file_browser_D, 3, 0)
        layout.setSpacing(0)
        layout.setContentsMargins( 0, 0, 0, 0)

        #dropdown algorithm selection
        self.dropdown_algorithms = Dropdown.Dropdown(self)
        layout.addWidget(self.dropdown_algorithms, 4, 0)

        #preview coutner + rn btn
        total_files = self.file_browser_A.GetFilesAmount() + self.file_browser_B.GetFilesAmount() + self.file_browser_C.GetFilesAmount() + self.file_browser_D.GetFilesAmount()
        self.values = [self.file_browser_A.GetFilesAmount(), self.file_browser_B.GetFilesAmount(), self.file_browser_C.GetFilesAmount(), self.file_browser_D.GetFilesAmount(), total_files, self.dropdown_algorithms.GetCurrentAlgorithm()]
        self.preview_box = PreviewBox.Preview(self.values)
        self.OnDropdownUpdate()
        layout.addWidget(self.preview_box, 5, 0)




        #result box
        # self.values_rb = [0,0,0,0]
        self.values_rb = [146,49,354,760]
        if self.values_rb[0] != 0 and self.values_rb[1] != 0 and self.values_rb[2] != 0 and self.values_rb[3] != 0:
            self.result_box = ResultBox.Result(self.values_rb)
            layout.addWidget(self.result_box,6,0)

        #save file at (similar FileDialog)
        self.file_save = FileDialogSave.Dialog(self)
        layout.addWidget(self.file_save, 7, 0)
        self.show()

    def OnDropdownUpdate(self):
        total_files = self.file_browser_A.GetFilesAmount() + self.file_browser_B.GetFilesAmount() + self.file_browser_C.GetFilesAmount() + self.file_browser_D.GetFilesAmount()
        self.values = [self.file_browser_A.GetFilesAmount(), self.file_browser_B.GetFilesAmount(), self.file_browser_C.GetFilesAmount(), self.file_browser_D.GetFilesAmount(), total_files, self.dropdown_algorithms.GetCurrentAlgorithm()]
        self.preview_box.UpdatePreviewValues(self.values)