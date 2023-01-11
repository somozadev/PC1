import random
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_score,recall_score,f1_score, confusion_matrix, classification_report
from IA.SaveTrainingModel import SaveTrainingModel
class NaiveBayes:
    def Train(self, docs):
        X_train, X_test, Y_train, Y_test = GetSplits(docs)
        vectorizer = TfidfVectorizer()                                  #CountVectorizer() #crea un vectorizador para convertir cada doc a un vector
        vectorizer.analyzer = 'word'                                    #should understand as separated words, and not chars or char_wb
        vectorizer.min_df = 3                                           #ignore terms that have a document frequency strictly lower than the given threshold

        matrix = vectorizer.fit_transform(X_train)                      #convierte el vector en una matriz de términos
        naive_bayes_classifier = MultinomialNB().fit(matrix, Y_train)   #multinomialNB es un clasificador para naive bayes especializado en word counts para clasificacion de texto, funciona con tfidf
        Evaluate("Naive Bayes \t TRAIN \t", naive_bayes_classifier, vectorizer, X_train, Y_train)
        Evaluate("Naive Bayes \t TEST \t", naive_bayes_classifier, vectorizer, X_test, Y_test)
        SaveTrainingModel.Save(self,"NaiveBayesModel","NaiveBayesVectorizer",vectorizer,naive_bayes_classifier)


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