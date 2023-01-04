from nltk.stem.snowball import SnowballStemmer  # Para stemizar los tokens


class Stemming():
    def __init__(self,
                 parent=None):  # def __init__(self, VALORES, parent=None):    <-  donde valores es el input que recibe al llamar a la clase
        super(Stemming, self).__init__(parent)

    def GetStemming(self, tokens_b=[]):
        tokens_c = []  # Lista que guardara la nueva lista de tokens stemizados
        for tok in tokens_b:  # Recorrer los tokens token uno a uno
            tokens_c.append(
                SnowballStemmer(language="spanish").stem(tok))  # Transformar cada token a su correspondiente stem
        return tokens_c
