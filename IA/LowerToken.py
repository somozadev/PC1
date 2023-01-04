from nltk.tokenize import RegexpTokenizer       # Para tokenizar un texto

class LowerToken():
    def __init__(self, parent=None):
        super(LowerToken, self).__init__(parent)

    def lower_token(self, texto):
        tokensA = RegexpTokenizer(r'\w+').tokenize(texto.lower())  # Tokenizar y pasar a minusculas el texto recibido
        return tokensA
