from collections import defaultdict
from nltk import FreqDist
from IA.PLN.StopWords import StopWords
from IA.PLN.Tokenizer import Tokenizer
from IA.PLN.TextPreparation import TextPreparation
class ToupleList:

    #lee el csv generado y crea una lista de tuplas con la categoría y el contenido de cada receta
    def GenerateToupleList(self, name):
        docs = []
        with open('CSV/'+name+'.csv', 'r', encoding='utf8') as datafile:
           for row in datafile:
               parts = row.split('\t')
               doc = (parts[0], parts[2].strip())
               docs.append(doc)

        return docs

    def PrintFrequencyDistribution(self, docs):
        tokens = defaultdict(list)
        for doc in docs:
            doc_label = doc[0]
            doc_text = doc[1]

            doc_text = TextPreparation.ClearText(self,doc_text)
            doc_tokens = Tokenizer.Tokenize(self,doc_text)
            doc_tokens = StopWords.FilterStopWord(self,doc_tokens)

            tokens[doc_label].extend(doc_tokens)

        for category_label, category_tokens in tokens.items():
            print(category_label)
            frequency_distance = FreqDist(category_tokens)
            print(frequency_distance.most_common(20))
