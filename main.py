import os
from pathlib import Path
import Tabs
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class window(QMainWindow):
   def __init__(self, parent = None):
      super(window, self).__init__(parent)
      self.resize(1000,800)
      self.setWindowTitle("Recomendador de recetas")
      font = QFont()
      font.setFamily("Arial")
      font.setPointSize(16)
      self.tabs_widget = Tabs.TabsWidget(self)
      self.setCentralWidget(self.tabs_widget)


def resource_path(relative):
   return os.path.join(
      os.environ.get(
         "_MEIPASS2",
         os.path.abspath(".")
      ),
      relative
   )
def main():
   app = QApplication(sys.argv)

   app.setStyleSheet(Path(resource_path("stylesheets.css")).read_text())
   ex = window()
   ex.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   main()