import os
import pandas as pd

class ToDataset():
    def __init__(self, paths, parent=None):#    def __init__(self, VALORES, parent=None):    <-  donde valores es el input que recibe al llamar a la clase
        super(ToDataset, self).__init__(parent)


#Devuelve el nombre de los archivos que hay en x ruta
    def FileNames(self, folder):
        files = os.listdir(folder)
        names = []
        for file in files:
            if os.path.isfile(os.path.join(folder, file)) and file.endswith('.txt'):
                names.append(file)
        return names

#Crea un dataframe con los títulos y textos de las recetas de la categoría que se le especifíca
    def GetDataFrame(self, path):
        df = pd.DataFrame()
        entrances = self.FileNames(path)
        df['Title'] = entrances

        textList = []
        for i in range(len(df)):
            with open(path + '/' + df.Title[i], "r") as f:
                textRecipe = f.read()
                textList.append(textRecipe)
                f.close()
        df["Text"] = textList
        return df

