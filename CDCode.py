# doesn't need smpecific object names since QTWidgets is used.
import fileinput
from PyQt5.QtWidgets import QTableView,QSpinBox, QMainWindow, QApplication, QFileDialog, QTableWidget, QTableWidgetItem, QPushButton, QWidget
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
        self.ResizeButton = self.findChild(QPushButton,"ResizeButton")
        self.InputTable = self.findChild(QTableWidget, "InputTable")
        self.InputTable.setRowCount(100)
        self.InputTable.setColumnCount(100)
        self.ColumnValue=self.findChild(QSpinBox, "ColumnsSpinBox")
        self.ColumnValue.setMaximum(1000000)
        self.ColumnValue.setValue(100)
        self.RowValue=self.findChild(QSpinBox, "RowsSpinBox")
        self.RowValue.setMaximum(1000000)
        self.RowValue.setValue(100)
        self.QTableOne = self.findChild(QTableWidget, "OutputTable")
        self.importButton = self.findChild(QPushButton, "ImportCSVButton")
        self.tryButton = self.findChild(QPushButton, "tryButton")
        self.EmigrationButton = self.findChild(QPushButton, "EmigrationButton")
        self.ImmigrationButton = self.findChild(QPushButton, "ImmigrationButton")
        self.MateButton = self.findChild(QPushButton, "MateButton")
        self.ModulesButton = self.findChild(QPushButton, "ModuleButton")
        self.MortalityButton = self.findChild(QPushButton, "MortalityButton")
        self.OffSpringButton = self.findChild(QPushButton, "OffSpringButton")
        self.PreProcessButton = self.findChild(QPushButton, "PreProcessButton")
        self.PostProcessButton = self.findChild(QPushButton, "PostProcessButton")

        # self.ResizeButton.clicked.connect(self.tableResize)
        self.importButton.clicked.connect(self.openImportFile)
        #self.tryButllton.clicked.connect(self.openOutputFile)

        # Show the app
        self.show()

    def tableResize(self):
        numColumn=self.ColumnValue.value()
        self.ColumnValue.setValue(numColumn)
        self.InputTable.setColumnCount(numColumn)
        numRows=self.RowValue.value()
        self.RowValue.setValue(numRows)
        self.InputTable.setRowCount(numRows)

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
        # need an insert ot grow table size after import - refer to scrollwheel video 
        # Need to allow user to change column and row names 

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
    
# initialize the app

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()