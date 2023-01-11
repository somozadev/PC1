from nltk.tokenize import word_tokenize

class Tokenizer:
    def Tokenize(self, text):
        text = word_tokenize(text, language='spanish')
        return text
