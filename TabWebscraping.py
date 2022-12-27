from PyQt5.QtWidgets import *
import Components.FileDialogOpen as FileDialogOpen
import Components.FileDialogSave as FileDialogSave
import Components.WebScrapper as ws
from pathlib import Path
import sys


class WebScraping(QWidget):
    def __init__(self, parent=None):
        super(WebScraping, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        #Webscrapper funcionality and it's corresponding UI
        self.scraper = ws.WebScrap(self)
        layout.addWidget(self.scraper)


        self.show()

