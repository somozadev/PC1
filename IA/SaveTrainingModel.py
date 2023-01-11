import pickle
import os

class SaveTrainingModel:
    def Save(self, modelName, vectorizerName, vectorizer, model_classifier):
        modelName += '.pkl'
        if os.path.exists(modelName) is False:
            pickle.dump(model_classifier, open(modelName,'wb')) #save trained model
            print("model saved")
        else:
            print("model already exists")

        vectorizerName += '.pkl'
        if os.path.exists(vectorizerName) is False:
            pickle.dump(vectorizer, open(vectorizerName,'wb'))#save vectorizer so we can transform new data
            print("vectorizer saved")
        else:
            print("vectorizer already exists")


