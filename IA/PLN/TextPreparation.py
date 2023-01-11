import string


class TextPreparation:
    def ClearText(self, text):
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = text.lower()
        return text

