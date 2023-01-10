from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from IA.SaveTrainingModel import SaveTrainingModel
from sklearn.feature_extraction.text import CountVectorizer
import random

def get_splits(docs):
    random.shuffle(docs)
    X_train = []  # training docs
    Y_train = []  # corresponding training labels

    X_test = []  # test docs
    Y_test = []  # corresponding test labels

    pivot = int(.80 * len(docs))  # get 80% of the docs for train

    for i in range(0, pivot):
        X_train.append(docs[i][1])
        Y_train.append(docs[i][0])

    for i in range(pivot, len(docs)):
        X_test.append(docs[i][1])
        Y_test.append(docs[i][0])

    return X_train, X_test, Y_train, Y_test

class LinearSVC:

    def train(self, docs):
        linear_svc = LinearSVC()
        X_train, X_test, Y_train, Y_test = get_splits(docs)
        vectorizer = CountVectorizer( ngram_range=(1,3),min_df=3,analyzer='word') #crea un vectorizador para convertir cada doc a un vector
        matrix = vectorizer.fit_transform(X_train) #convierte el vector en una matriz de términos

        linear_svc_classifier = linear_svc.fit(matrix, Y_train)
        prediction = linear_svc.predict(X_test)
        print("LINEAR SVC accuracy score:")
        print(accuracy_score(Y_test, prediction))
        SaveTrainingModel.Save(self, "LinearSVCModel", "LinearSVCVectorizer", vectorizer, linear_svc_classifier)
