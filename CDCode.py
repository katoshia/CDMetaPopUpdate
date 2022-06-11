# doesn't need smpecific object names since QTWidgets is used.
import fileinput
from PyQt5.QtWidgets import QTableView, QMainWindow, QApplication, QFileDialog, QTableWidget, QTableWidgetItem, QPushButton, QWidget
from PyQt5 import uic
from PyQt5.uic import loadUiType
from os.path import dirname, join
import sys
import os
import pandas as pd
import csv

From_Main, _= loadUiType(join(dirname(__file__), "CDMetaPop.ui"))

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        QWidget.__init__(self)

        # load the ui file
        uic.loadUi("CDMetaPop.ui", self)
        # show the app

        # define our widgets
        self.QTable = self.findChild(QTableWidget, "tableWidget")
        self.QTable1 = self.findChild(QTableWidget, "mainTable")
        self.pushButton = self.findChild(QPushButton, "pushButton")
        self.tryButton = self.findChild(QPushButton, "tryButton")

        # do something

        # self.pushButton.clicked.connect(self.clicker)
        self.pushButton.clicked.connect(self.openFile)
        self.tryButton.clicked.connect(self.openFile)

        # Show the app
        self.show()

  
    # tried below
    def openFile(self):
        path =QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != "":
            with open(path[0], newline='\n') as csv_file:
                self.QTable.setRowCount(0)
                #self.QTable.setRowCount(len(csv_file))
                self.QTable.setColumnCount(10)
                my_file=csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row=self.QTable.rowCount()
                    self.QTable.insertRow(row)
                    
                    if len(row_data)>10:
                        self.QTable.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item=QTableWidgetItem(stuff)
                        self.QTable.setItem(row, column, item)
                      

    def clicker(self):
        self.pushButton.setText("Pressed")
    
# initialize the app

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()