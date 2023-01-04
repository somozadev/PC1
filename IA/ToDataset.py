import os
import pandas as pd

class ToDataset():
    def __init__(self, paths, parent=None):#    def __init__(self, VALORES, parent=None):    <-  donde valores es el input que recibe al llamar a la clase
        super(ToDataset, self).__init__(parent)


#Devuelve el nombre de los archivos que hay en x ruta
    def NombresArchivos(self, carpeta):
        contenido = os.listdir(carpeta)
        nombres = []
        for fichero in contenido:
            if os.path.isfile(os.path.join(carpeta, fichero)) and fichero.endswith('.txt'):
                nombres.append(fichero)
        return nombres

#Crea un dataframe con los títulos y textos de las recetas de la categoría que se le especifíca
    def GetDataFrame(self, ruta):
        df = pd.DataFrame()
        entrantes = self.NombresArchivos(ruta)
        df['Titulo'] = entrantes

        listaTextos = []
        for i in range(len(df)):
            with open(ruta + '/' + df.Titulo[i], "r") as f:
                textoReceta = f.read()
                listaTextos.append(textoReceta)
                f.close()
        df["Texto"] = listaTextos
        return df

