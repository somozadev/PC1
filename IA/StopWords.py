from nltk.corpus import stopwords               # Para detectar stopwords en un texto

class StopWords():
    def __init__(self, parent=None):
        super(StopWords, self).__init__(parent)

    def stop_word(self, tokens_a=[]):
        tokens_b = []  # Lista que guardará la nueva lista de tokens sin stop words
        for tok in tokens_a:  # Recorrer los tokens uno a uno
            if not tok in stopwords.words("spanish"):  # Si no es stop-word, añadir a la lista sin stop-words
                tokens_b.append(tok)
        return tokens_b

