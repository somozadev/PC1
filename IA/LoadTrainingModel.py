import pickle


class LoadTrainingModel:
    def Load(self, modelName, vectorizerName):

        model = pickle.load(open(modelName,'rb')) #loads trained model
        vectorizer = pickle.load(open(vectorizerName,'rb'))#loads vectorizer so we can transform new data
        return model,vectorizer
