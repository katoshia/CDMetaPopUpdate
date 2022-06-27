# imports for qtapplications and widegets
import fileinput
from PyQt5.QtWidgets import QFrame, QMainWindow, QApplication, QPushButton, QWidget
from PyQt5 import uic
from PyQt5.uic import loadUiType
from os.path import dirname, join
import sys

From_Main, _= loadUiType(join(dirname(__file__), "SplashPage.ui"))


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        QWidget.__init__(self)

        # load the ui file
        uic.loadUi(join(dirname(__file__), "SplashPage.ui"), self)

        # uic.loadUi("SplashPage.ui", self)
        # show the app

        # define our widgets
        self.PicOne = self.findChild(QFrame, "picFrameOne")
        self.StartButton = self.findChild(QPushButton, "pushButton")

        self.show()


# initialize the app

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()