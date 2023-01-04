from nltk.tokenize import RegexpTokenizer       # Para tokenizar un texto

class LowerToken():
    def __init__(self, parent=None):
        super(LowerToken, self).__init__(parent)

    def ToLowerTokenize(self, text):
        result = RegexpTokenizer(r'\w+').tokenize(text.lower())  # Tokenizar y pasar a minusculas el texto recibido
        return result
