# Rune Scape Data Processing Project

# At this point for xp loggint im going to have to create my own plugin to store and save that data
# Logger for Combat and Grand exchange already added to my 
#
# Us GE logger to log data for kill trips along with loot tracker to keep accurate info on kill numbers and money per hour minus cost of supplies
#
# Use a jason file to save all data from prior runs of program so i dont have to reinit all my accounts over and over again


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon

import numpy
import matplotlib
import account




class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'OSRS Data Processing Project'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())