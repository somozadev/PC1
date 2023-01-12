from PyQt5.QtWidgets import *
import Components.FileDialogOpen as FileDialogOpen
import Components.FileDialogSave as FileDialogSave
import Components.ClassificationResults as ClassificationResults
import Components.ClassificationSummary as ClassificationSummary


class Classification(QWidget):
    def __init__(self, parent=None):
        super(Classification, self).__init__(parent)
        layout = QGridLayout()
        self.setLayout(layout)



        #select folder text to short and folder model
        self.file_browser_texts = FileDialogOpen.DialogClasifTexts(self,'Textos a clasificar')
        self.file_browser_model = FileDialogOpen.DialogClasifModel(self,'Modelo clasificador')
        layout.addWidget(self.file_browser_texts, 0, 0)
        layout.addWidget(self.file_browser_model, 1, 0)


        #show the results
        self.selected_texts_path = "G:/CARRERA/Docs/"
        self.results = ClassificationResults.Results(self, self.selected_texts_path)
        layout.addWidget(self.results,2, 0)

        #summary and execute classification
        # self.paths = ['G:/CARRERA/6ºCARRERA/PC1/PC1/textosPreciddion/entrantes','G:/CARRERA/6ºCARRERA/PC1/PC1/NaiveBayesModel','G:/CARRERA/6ºCARRERA/PC1/PC1/NaiveBayesVectorizer']  # paths from the selectedd folders
        self.paths = ['','','']

        self.summary = ClassificationSummary.Summary(self, self.paths)
        layout.addWidget(self.summary, 3, 0)


        self.tempPath = ""
        self.tempfile = None
        #save file at (similar FileDialog)

        self.file_save = FileDialogSave.DialogTexts('Guardar textos', self.tempPath, self.tempfile)
        layout.addWidget(self.file_save, 4, 0)
        self.show()


    def FinishedTesting(self):
        self.selected_texts_path = self.summary.GetTempPath()
        self.tempPath = self.selected_texts_path
        self.tempfile = self.summary.GetTempFile()
        self.results.DisplayWhenExecuteTest(self.selected_texts_path)
        self.file_save.UpdateTempVars(self.tempPath, self.tempfile)

    def FinishedDisplayTexts(self):
        self.summary.UpdatePreviewAmountTexts()
    def OnPathUpdate_Texts(self):
        self.paths[0] = self.file_browser_texts.GetPath()
        print(self.paths)

    def OnPathUpdate_Model(self):
        self.paths[1] = self.file_browser_model.GetPath()
        aux = self.file_browser_model.GetPath()
        aux = aux[:-4]
        aux += "_vector.pkl"
        self.paths[2] = aux
        print(self.paths)
