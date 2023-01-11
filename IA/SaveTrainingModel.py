import pickle
import os
import tempfile
import shutil

class SaveTrainingModel:
    def __init__(self):
        self.tmpdirname = None

    def Save(self, modelName, vectorizerName, vectorizer, model_classifier):

        self.tempfile = tempfile.TemporaryDirectory()
        self.tempfileModel = self.tempfile.name
        modelName += '.pkl'
        self.tempfileModel += "\\{}".format(modelName)
        if os.path.exists(self.tempfileModel) is False:
            pickle.dump(model_classifier, open(self.tempfileModel,'wb')) #save trained model
            print("model saved")
        else:
            print("model already exists")

        self.tempfileVector = self.tempfile.name
        vectorizerName += '.pkl'
        self.tempfileVector += "\\{}".format(vectorizerName)
        if os.path.exists(self.tempfileVector) is False:
            pickle.dump(vectorizer, open(self.tempfileVector,'wb'))#save vectorizer so we can transform new data
            print("vectorizer saved")
        else:
            print("vectorizer already exists")


    def FinalSavingPathChosen(self, finalpath):
        finalpathVector = finalpath[:-4]
        finalpathVector+= "_vector.pkl"
        shutil.move(self.tempfileModel, finalpath)
        shutil.move(self.tempfileVector, finalpathVector)

        self.tempfile.cleanup()