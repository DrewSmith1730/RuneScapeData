# Rune Scape Data Processing Project

# 
#
#
#
#


import sys
from PyQt5 import QtWidgets
import numpy
import matplotlib


def main():
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()

    windows.resize(500,500)
    windows.move(100,100)
    windows.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()