import random
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_score,recall_score,f1_score, confusion_matrix, classification_report
from IA.SaveTrainingModel import SaveTrainingModel
class NaiveBayes:

    def __init__(self, runButton):
        self.runButton = runButton
        self.confussion_matrix = None
    def Train(self, docs):
        multinomial_naive_bayes =MultinomialNB()

        X_train, X_test, Y_train, Y_test = GetSplits(docs)
        self.vectorizer = TfidfVectorizer()                                  #CountVectorizer() #crea un vectorizador para convertir cada doc a un vector
        self.vectorizer.analyzer = 'word'                                    #should understand as separated words, and not chars or char_wb
        self.vectorizer.min_df = 3                                           #ignore terms that have a document frequency strictly lower than the given threshold

        matrix = self.vectorizer.fit_transform(X_train)                      #convierte el vector en una matriz de términos
        self.classifier =multinomial_naive_bayes.fit(matrix, Y_train)   #multinomialNB es un clasificador para naive bayes especializado en word counts para clasificacion de texto, funciona con tfidf
        # self.Evaluate("Naive Bayes \t TEST \t", X_test, Y_test)
        self.Evaluate("Naive Bayes \t TRAIN \t", X_train, Y_train)
        SaveTrainingModel.Save(SaveTrainingModel,"NaiveBayesModel","NaiveBayesVectorizer",self.vectorizer,self.classifier)
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
    X_train = []  # training docs
    Y_train = []  # corresponding training labels

    X_test = []  # test docs
    Y_test = []  # corresponding test labels

    # pivot = int(.80 * len(docs))  # get 80% of the docs for train

    for i in range(0, 1):
        X_train.append(docs[i][1])
        Y_train.append(docs[i][0])

    # for i in range(1, len(docs)):
    #     X_test.append(docs[i][1])
    #     Y_test.append(docs[i][0])

    return X_train, X_test, Y_train, Y_test
