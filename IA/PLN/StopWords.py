from nltk.corpus import stopwords               # Para detectar stopwords en un texto

class StopWords:
    def FilterStopWord(self, tokens):
        stop_words = set(stopwords.words('spanish'))
        stop_words.add('vamos')
        tokens = [t for t in tokens if not t in stop_words]
        return tokens
