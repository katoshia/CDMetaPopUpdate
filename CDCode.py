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
        # empty table
        self.InputTable = self.findChild(QTableWidget, "InputTable")
        #preset table
        self.QTableOne = self.findChild(QTableWidget, "OutputTable")
        self.pushButton = self.findChild(QPushButton, "pushButton")
        self.tryButton = self.findChild(QPushButton, "tryButton")
        # do something

        # self.pushButton.clicked.connect(self.clicker)
        self.pushButton.clicked.connect(self.openImportFile)
        #self.tryButton.clicked.connect(self.openOutputFile)

        # Show the app
        self.show()

  
    # tried below - NEEDS CORRECTING FOR COLUMN HEADERS. - CORRECTED
    def openImportFile(self):
        path =QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != "":
            with open(path[0], newline='\n') as csv_file:
                self.InputTable.setRowCount(0)
                self.InputTable.setColumnCount(0)
                my_file=csv.reader(csv_file, delimiter=',', quotechar='|')
                
                for row_data in my_file:
                    row=self.InputTable.rowCount()
                    self.InputTable.insertRow(row)
                    
                    if len(row_data)> self.InputTable.columnCount():
                        self.InputTable.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item=QTableWidgetItem(stuff)
                        self.InputTable.setItem(row, column, item)
        # will need an empty table not a preset one - use preset one for input into program versus import  -CORRECTED

        # open the output file into output table.
    def openOutputFile(self):
        path =QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != "":
            with open(path[0], newline='\n') as csv_file:
                #self.QTableOne.setRowCount(0)
                #self.InputTable.setRowCount(len(csv_file))
                #self.QTableOne.setColumnCount(10)
                my_file=csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    #row=self.QTableOne.rowCount()
                    #self.QTableOne.insertRow(row)x
                    
                    #if len(row_data)>10:
                     #   self.QTableOne.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item=QTableWidgetItem(stuff)
                        self.QTableOne.setItem(row, column, item)

    # practice for click event
    def clicker(self):
        self.pushButton.setText("Pressed")
    
# initialize the app

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()