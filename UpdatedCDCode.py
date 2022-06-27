# imports for qtapplications and widegets
from PyQt5.QtWidgets import QLabel, QGroupBox, QSpinBox, QMainWindow, QApplication, QFileDialog, QTableWidget, QTableWidgetItem, QPushButton, QWidget, QFrame
from PyQt5 import uic
from PyQt5.uic import loadUiType
from os.path import dirname, join
import sys
import os
import csv


From_Main, _= loadUiType(join(dirname(__file__), "SplashPage.ui"))

class SplashUI(QMainWindow):
    def __init__(self, parent=None):
        super(SplashUI, self).__init__(parent)
        QWidget.__init__(self)

        # load the ui file
        uic.loadUi(join(dirname(__file__), "SplashPage.ui"), self)

        # uic.loadUi("SplashPage.ui", self)
        # show the app

        # define our widgets
        self.labelA=self.findChild(QLabel, "label")
        self.labelA=self.findChild(QLabel, "label_2")
        self.labelA=self.findChild(QLabel, "label_3")
        self.labelA=self.findChild(QLabel, "label_4")
        self.GroupBox=self.findChild(QGroupBox, "groupBox")

        self.StartButton = self.findChild(QPushButton, "startButton")
        self.show()

        self.StartButton.clicked.connect(self.Start_Button_Clicked)
        self.dialog = UI(self)

    def Start_Button_Clicked(self):
        
        self.dialog.show()

class UI(QMainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        QWidget.__init__(self)

        # load the ui file
        uic.loadUi(join(dirname(__file__), "UpdatedCDMetaPOP.ui"), self)
        
        # show the app

        # define our widgets
        # empty table
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

        self.RowValue.valueChanged.connect(self.changeTableRows)
        self.ColumnValue.valueChanged.connect(self.changeTableColumns)


        self.importButton.clicked.connect(self.openImportFile)

        # Show the app
        #self.show()

    # adds rows/columns to empty table ok and decreases size - need to reset spinboxes to counts of imports also need to protect data after importing if resize needs to happen.
    def changeTableColumns(self):
        columns=self.ColumnValue.value()
        self.InputTable.setColumnCount(columns)
    def changeTableRows(self):
        rows = self.RowValue.value()
        self.InputTable.setRowCount(rows)
        # numColumn=self.ColumnValue.value()

    # def openMain(self):


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
        # need an insert ot grow table size after import - refer to scrollwheel video - empty table OK - Import not OK
        # Need to allow user to change column and row names - TO DO

        # open the output file into output table. - TO DO
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
UIWindow = SplashUI()
app.exec_()