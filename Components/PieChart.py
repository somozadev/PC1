from PyQt5 import QtCore, QtChart
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import *


class Pie(QWidget):

    def __init__(self, values, parent=None):
        super(Pie, self).__init__(parent)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.series = QPieSeries()
        for value in values:
            self.series.append(value[0], value[1])
        self.series.setLabelsVisible(True)
        self.series.setLabelsPosition(QtChart.QPieSlice.LabelInsideHorizontal)

        self.chart = QChart()
        self.chart.legend()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)

        for slice in self.series.slices():
            slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
        i = 0
        for value in values:
            self.chart.legend().markers(self.series)[i].setLabel(value[0])
            i+=1


        self.setFixedSize(QtCore.QSize(350, 350))

        layout.addWidget(self.chartview)#,0,0

    def UpdateValues(self, values):
        self.chart.removeAllSeries()
        self.series = QPieSeries()
        for value in values:
            self.series.append(value[0], value[1])
        self.chart.addSeries(self.series)
        for slice in self.series.slices():
            slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
        i = 0
        for value in values:
            self.chart.legend().markers(self.series)[i].setLabel(value[0])
            i+=1

