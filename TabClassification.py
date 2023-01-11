from PyQt5.QtWidgets import *
import Components.FileDialogOpen as FileDialogOpen
import Components.FileDialogSave as FileDialogSave
import Components.ClassificationResults as ClassificationResults
import Components.ClassificationSummary as ClassificationSummary
import Components.PieChart as PieChart


class Classification(QWidget):
    def __init__(self, parent=None):
        super(Classification, self).__init__(parent)
        layout = QGridLayout()
        self.setLayout(layout)



        #select folder text to short and folder model
        self.file_browser_texts = FileDialogOpen.DialogClasifTexts('Textos a clasificar')
        self.file_browser_model = FileDialogOpen.DialogClasifModel('Modelo clasificador')
        layout.addWidget(self.file_browser_texts, 0, 0)
        layout.addWidget(self.file_browser_model, 1, 0)


        #show the results
        self.selected_texts_path = "G:/CARRERA/Docs/"
        self.results = ClassificationResults.Results("rtest",self.selected_texts_path)
        layout.addWidget(self.results,2, 0)

        #summary and execute classification
        self.paths = ['G:/CARRERA/6ºCARRERA/PC1/PC1/textosPreciddion/entrantes','G:/CARRERA/6ºCARRERA/PC1/PC1/NaiveBayesModel','G:/CARRERA/6ºCARRERA/PC1/PC1/NaiveBayesVectorizer']  # paths from the selectedd folders

        self.summary = ClassificationSummary.Summary(self.paths)
        layout.addWidget(self.summary, 3, 0)



        #save file at (similar FileDialog)
        self.file_save = FileDialogSave.Dialog('Guardar textos')
        layout.addWidget(self.file_save, 4, 0)
        self.show()

    def OnSelectedText(self):
        return 0

