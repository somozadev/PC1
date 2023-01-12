from PyQt5.QtWidgets import QPushButton, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
import TabTraining
import TabClassification
import TabWebscraping

class TabsWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.trainTab = QWidget()
        self.classificationTab = QWidget()
        self.webscrapingTab = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.trainTab, "Entrenamiento")
        self.tabs.addTab(self.classificationTab, "Clasificación")
        self.tabs.addTab(self.webscrapingTab, "Web scraping")

        # Training tab
        self.trainTab.layout = QVBoxLayout(self)
        self.trainTab.setLayout(self.trainTab.layout)
        self.trainTab.layout.addWidget(TabTraining.Training(self))

        # Classification tab
        self.classificationTab.layout = QVBoxLayout(self)
        self.classificationTab.setLayout(self.classificationTab.layout)
        self.classificationTab.layout.addWidget(TabClassification.Classification(self))

        # Webscraping tab
        self.webscrapingTab.layout = QVBoxLayout(self)
        self.webscrapingTab.setLayout(self.webscrapingTab.layout)
        self.webscrapingTab.layout.addWidget(TabWebscraping.WebScraping(self))

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
