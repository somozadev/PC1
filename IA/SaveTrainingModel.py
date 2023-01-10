import pickle


class SaveTrainingModel:
    def Save(self, modelName, vectorizerName, vectorizer, model_classifier):
        modelName += '.pkl'
        pickle.dump(model_classifier, open(modelName,'wb'))

        vectorizerName += '.pkl'
        pickle.dump(vectorizer, open(vectorizerName,'wb'))

