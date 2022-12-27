import requests
import webbrowser

from PyQt5 import QtCore
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *

class CustomQListItem(QWidget):
    def __init__(self, name,content,url, parent=None):
        super(CustomQListItem, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.label_name = QLabel(name)
        self.label_content = QLabel(content)
        self.button_view = QPushButton("Ver")
        self.url = url
        self.button_view.clicked.connect(self.OpenUrl)

        self.label_name.setFixedSize(200,25)
        self.label_content.setFixedSize(500,25)
        self.button_view.setFixedSize(100,25)

        self.label_name.setObjectName('WebscrapingItemName')
        self.label_content.setObjectName('WebscrapingItemContent')
        self.button_view.setObjectName('WebscrapingItemViewButton')

        self.layout.addWidget(self.label_name)
        self.layout.addWidget(self.label_content)
        self.layout.addWidget(self.button_view)
        self.setLayout(self.layout)
    def OpenUrl(self):
        webbrowser.open(self.url)

class WebScrap(QWidget):

    def __init__(self, parent=None):
        super(WebScrap, self).__init__(parent)

        layout = QGridLayout()
        self.setLayout(layout)

        self.result_names = []
        self.result_contents = []
        self.result_links = []

        self.results_list = QListWidget()

        self.input_field = QLineEdit()
        self.search_button = QPushButton("Buscar")
        self.query = self.input_field.text()
        self.search_button.clicked.connect(self.OnSearch)

        layout.addWidget(self.input_field, 0,0)
        layout.addWidget(self.search_button,0,1)
        layout.addWidget(self.results_list,2,0)



    def GetSearchUrl(self, stringGiven):
        search_page = "https://www.recetasgratis.net/busqueda?q={}".format(stringGiven)
        return search_page

    def OnSearch(self):
        self.query = self.input_field.text()
        page = requests.get('https://www.recetasgratis.net/')
        soup = BeautifulSoup(page.text, 'html.parser')

        searchbar_id_q = soup.find("input", {"id": "q"})
        print(searchbar_id_q)

        new_url = self.GetSearchUrl(self.query)
        search_recipe = requests.post(new_url)
        soup = BeautifulSoup(search_recipe.text, 'html.parser')

        results = soup.find_all("div", {"class": "resultado link"})

        self.results_list.clear()
        for result in results:
            result_name = result.find(class_="titulo titulo--resultado").text
            result_content = result.find(class_="intro").text[:82] + "..."
            result_link = result.find('a', href=True)['href']

            self.result_names.append(result_name)
            self.result_contents.append(result_content)
            self.result_links.append(result_link)

            myCustomWidget = CustomQListItem(result_name,result_content,result_link)
            customListItem = QListWidgetItem(self.results_list)
            customListItem.setSizeHint(myCustomWidget.sizeHint())
            self.results_list.addItem(customListItem)
            self.results_list.setItemWidget(customListItem,myCustomWidget)




        print(len(results))
