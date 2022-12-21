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

        # Create first tab
        self.trainTab.layout = QVBoxLayout(self)
        self.trainTab.setLayout(self.trainTab.layout)
        self.trainTab.layout.addWidget(TabTraining.Training(self))

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
