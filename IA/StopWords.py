from nltk.corpus import stopwords               # Para detectar stopwords en un texto

class StopWords():
    def __init__(self, parent=None):
        super(StopWords, self).__init__(parent)

    def FilterStopWord(self, tokens_input=[]):
        tokens_output = []  # Lista que guardará la nueva lista de tokens sin stop words
        for token in tokens_input:  # Recorrer los tokens uno a uno
            if not token in stopwords.words("spanish"):  # Si no es stop-word, añadir a la lista sin stop-words
                tokens_output.append(token)
        return tokens_output

