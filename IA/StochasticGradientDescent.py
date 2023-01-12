from sklearn.linear_model import SGDClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, classification_report
from IA.SaveTrainingModel import SaveTrainingModel
from sklearn.feature_extraction.text import  TfidfVectorizer
import random


class StochasticGradientDescent:

    def __init__(self, runButton):
        self.runButton = runButton
        self.confussion_matrix = None

    def Train(self, docs):
        sgd = SGDClassifier()

        X_train, X_test, Y_train, Y_test = GetSplits(docs)
        self.vectorizer = TfidfVectorizer()
        self.vectorizer.analyzer = 'word'
        self.vectorizer.min_df = 3

        matrix = self.vectorizer.fit_transform(X_train)
        self.classifier = sgd.fit(matrix, Y_train)
        self.Evaluate("Stochastic Gradient Descent \t TEST \t",  X_test, Y_test)
        self.Evaluate("Stochastic Gradient Descent \t TRAIN \t", X_train, Y_train)
        SaveTrainingModel.Save(SaveTrainingModel, "StochasticGradientDescentModel", "StochasticGradientDescentVectorizer",self.vectorizer, self.classifier)
        self.runButton.GetConfusionMatrix()

    def GetConfusionMatrix(self):
        return self.confussion_matrix
    def Evaluate(self, title, X, Y):
        X_tfidf = self.vectorizer.transform(X)
        Y_pred = self.classifier.predict(X_tfidf)

        self.confussion_matrix = confusion_matrix(Y, Y_pred)
        print(self.confussion_matrix)

        clasification_report = classification_report(Y, Y_pred)
        print(clasification_report)

        precision = precision_score(Y, Y_pred, average='micro')
        recall = recall_score(Y, Y_pred, average='micro')
        f1 = f1_score(Y, Y_pred, average='micro')
        print("%s\t%f\t%f\t%f\n" % (title, precision, recall, f1))


def GetSplits(docs):
    random.shuffle(docs)
    X_train = []
    Y_train = []

    X_test = []
    Y_test = []

    pivot = int(.80 * len(docs))

    for i in range(0, pivot):
        X_train.append(docs[i][1])
        Y_train.append(docs[i][0])

    for i in range(pivot, len(docs)):
        X_test.append(docs[i][1])
        Y_test.append(docs[i][0])

    return X_train, X_test, Y_train, Y_test
