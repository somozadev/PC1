from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score,recall_score,f1_score, confusion_matrix, classification_report
from IA.SaveTrainingModel import SaveTrainingModel
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import random


class RandomForest:

    def Train(self, docs):
        random_forest = RandomForestClassifier()
        random_forest.n_estimators = 500    #The number of trees in the forest.
        random_forest.criterion = 'gini'    #The function to measure the quality of a split

        X_train, X_test, Y_train, Y_test = GetSplits(docs)
        vectorizer = TfidfVectorizer()
        vectorizer.analyzer = 'word'
        vectorizer.min_df = 3

        matrix = vectorizer.fit_transform(X_train)
        random_forest_classifier = random_forest.fit(matrix, Y_train)
        Evaluate("Random Forest \t TRAIN \t", random_forest_classifier, vectorizer, X_train, Y_train)
        Evaluate("Random Forest \t TEST \t", random_forest_classifier, vectorizer, X_test, Y_test)
        SaveTrainingModel.Save(self, "RandomForestModel", "RandomForestVectorizer", vectorizer, random_forest_classifier)



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
    X_train = []
    Y_train = []

    X_test = []
    Y_test = []

    pivot = int(.80 * len(docs))

    for i in range(0,pivot):
        X_train.append(docs[i][1])
        Y_train.append(docs[i][0])

    for i in range(pivot, len(docs)):
        X_test.append(docs[i][1])
        Y_test.append(docs[i][0])

    return X_train,X_test,Y_train,Y_test