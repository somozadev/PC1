from PyQt5.QtWidgets import *
import Components.FileDialogOpen as FileDialogOpen
import Components.FileDialogSave as FileDialogSave
import Components.Dropdown as Dropdown
import Components.PreviewBox as PreviewBox
import Components.ResultsBox as ResultBox

class Training(QWidget):
    def __init__(self, parent=None):
        super(Training, self).__init__(parent)
        layout = QGridLayout()
        self.setLayout(layout)


        #select folders all categories
        self.file_browser_A = FileDialogOpen.Dialog(self, 'Entrantes')
        self.file_browser_B = FileDialogOpen.Dialog(self, 'Principales')
        self.file_browser_C = FileDialogOpen.Dialog(self, 'Segundos')
        self.file_browser_D = FileDialogOpen.Dialog(self, 'Postres')
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

        self.paths = ['','','',''] #paths from the selectedd folders
        # self.paths = ['G:/CARRERA/6ºCARRERA/PC1/PC1/ColeccionTextos/entrantes','G:/CARRERA/6ºCARRERA/PC1/PC1/ColeccionTextos/principal','G:/CARRERA/6ºCARRERA/PC1/PC1/ColeccionTextos/segundos','G:/CARRERA/6ºCARRERA/PC1/PC1/ColeccionTextos/postres'] #paths from the selectedd folders
        self.preview_box = PreviewBox.Preview(self, self.values, self.paths,self.dropdown_algorithms.GetCurrentAlgorithm())
        self.OnDropdownUpdate()
        layout.addWidget(self.preview_box, 5, 0)

        #result box
        self.values_rb = [0,0,0,0]
        # if self.values_rb[0] != 0 and self.values_rb[1] != 0 and self.values_rb[2] != 0 and self.values_rb[3] != 0:
        self.result_box = ResultBox.Result(self.values_rb)
        layout.addWidget(self.result_box,6,0)

        #save file at (similar FileDialog)
        self.file_save = FileDialogSave.Dialog('Guardar modelo')
        layout.addWidget(self.file_save, 7, 0)
        self.show()

    def OnTrainingFinished(self, confusion_matrix):
        self.values_rb = confusion_matrix
        self.result_box.UpdatePreviewValues(self.values_rb)
    def OnDropdownUpdate(self):
        self.values = [self.file_browser_A.GetFilesAmount(), self.file_browser_B.GetFilesAmount(), self.file_browser_C.GetFilesAmount(), self.file_browser_D.GetFilesAmount(),  self.dropdown_algorithms.GetCurrentAlgorithm()]
        self.preview_box.UpdatePreviewValues(self.values)
    def OnPathUpdate_A(self):
        self.paths[0] = self.file_browser_A.GetPath()
        total_files = self.file_browser_A.GetFilesAmount() + self.file_browser_B.GetFilesAmount() + self.file_browser_C.GetFilesAmount() + self.file_browser_D.GetFilesAmount()
        self.values = [self.file_browser_A.GetFilesAmount(), self.file_browser_B.GetFilesAmount(), self.file_browser_C.GetFilesAmount(), self.file_browser_D.GetFilesAmount(), total_files, self.dropdown_algorithms.GetCurrentAlgorithm()]
        self.OnDropdownUpdate()
    def OnPathUpdate_B(self):
        self.paths[1] = self.file_browser_B.GetPath()
        total_files = self.file_browser_A.GetFilesAmount() + self.file_browser_B.GetFilesAmount() + self.file_browser_C.GetFilesAmount() + self.file_browser_D.GetFilesAmount()
        self.values = [self.file_browser_A.GetFilesAmount(), self.file_browser_B.GetFilesAmount(), self.file_browser_C.GetFilesAmount(), self.file_browser_D.GetFilesAmount(), total_files, self.dropdown_algorithms.GetCurrentAlgorithm()]
        self.OnDropdownUpdate()
    def OnPathUpdate_C(self):
        self.paths[2] = self.file_browser_C.GetPath()
        total_files = self.file_browser_A.GetFilesAmount() + self.file_browser_B.GetFilesAmount() + self.file_browser_C.GetFilesAmount() + self.file_browser_D.GetFilesAmount()
        self.values = [self.file_browser_A.GetFilesAmount(), self.file_browser_B.GetFilesAmount(), self.file_browser_C.GetFilesAmount(), self.file_browser_D.GetFilesAmount(), total_files, self.dropdown_algorithms.GetCurrentAlgorithm()]
        self.OnDropdownUpdate()
    def OnPathUpdate_D(self):
        self.paths[3] = self.file_browser_D.GetPath()
        total_files = self.file_browser_A.GetFilesAmount() + self.file_browser_B.GetFilesAmount() + self.file_browser_C.GetFilesAmount() + self.file_browser_D.GetFilesAmount()
        self.values = [self.file_browser_A.GetFilesAmount(), self.file_browser_B.GetFilesAmount(), self.file_browser_C.GetFilesAmount(), self.file_browser_D.GetFilesAmount(), total_files, self.dropdown_algorithms.GetCurrentAlgorithm()]
        self.OnDropdownUpdate()


