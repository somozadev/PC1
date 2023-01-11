import os
from PyQt5.QtWidgets import *
class ToCsv(QWidget):
    def __init__(self, parent=None):
        super(ToCsv, self).__init__(parent)

    #en base a los directorios seleccionados de las carpetas, genera un fichero CSV de todos ellos ordenándolos por categoría, nombre y cotnenido
    def GenerateCSV(self, name, paths, categories):
        with open('CSV/'+name+'.csv', 'w', encoding='utf8') as outfile:
            # outfile.write('%s\t%s\t%s\n' % ('label', 'name', 'recipe'))
            for i in range(len(paths)):
                path = paths[i]
                label = categories[i]
                print(path)
                print(label)
                for file in os.listdir(path):
                    print(str(file))
                    filename = '%s/%s' % (path,str(file))
                    with open(filename, 'rb') as f:
                        text = f.read().decode(errors='replace').replace('\n', '')
                        outfile.write('%s\t%s\t%s\n' % (label, str(file) ,text))