from sklearn.svm import LinearSVC
from sklearn.metrics import precision_score,recall_score,f1_score, confusion_matrix, classification_report
from IA.SaveTrainingModel import SaveTrainingModel
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import random

class LinearSupportVector:

    def Train(self, docs):
        linear_svc = LinearSVC()
        X_train, X_test, Y_train, Y_test = GetSplits(docs)
        vectorizer = TfidfVectorizer()
        vectorizer.analyzer = 'word'
        vectorizer.min_df = 3
        matrix = vectorizer.fit_transform(X_train) #convierte el vector en una matriz de términos

        linear_svc_classifier = linear_svc.fit(matrix, Y_train)
        Evaluate("Linear Support Vector \t TRAIN \t", linear_svc_classifier, vectorizer, X_train, Y_train)
        Evaluate("Linear Support Vector \t TEST \t", linear_svc_classifier, vectorizer, X_test, Y_test)
        SaveTrainingModel.Save(self, "LinearSVCModel", "LinearSVCVectorizer", vectorizer, linear_svc_classifier)

def Evaluate(title, classifier, vectorizer, X, Y):
    X_tfidf = vectorizer.transform(X)
    Y_pred = classifier.predict(X_tfidf)

    confussion_matrix = confusion_matrix(Y, Y_pred)
    print(confussion_matrix)

    clasification_report = classification_report(Y, Y_pred)
    print(clasification_report)

    precision = precision_score(Y, Y_pred, average='micro')
    recall = recall_score(Y, Y_pred, average='micro')
    f1 = f1_score(Y, Y_pred, average='micro')
    print("%s\t%f\t%f\t%f\n" % (title,precision,recall,f1))
def GetSplits(docs):
    random.shuffle(docs)
    X_train = []                                                        #training docs
    Y_train = []                                                        #corresponding training labels

    X_test = []                                                         #test docs
    Y_test = []                                                         #corresponding test labels

    pivot = int(.80 * len(docs))                                        #get 80% of the docs for train

    for i in range(0,pivot):
        X_train.append(docs[i][1])
        Y_train.append(docs[i][0])

    for i in range(pivot, len(docs)):
        X_test.append(docs[i][1])
        Y_test.append(docs[i][0])

    return X_train,X_test,Y_train,Y_test