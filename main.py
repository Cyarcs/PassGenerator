import sys

from PyQt6 import QtWidgets, QtGui, QtCore, uic
from PyQt6.QtWidgets import QFileDialog, QLabel

from Resource.PassGen import Ui_MainWindow


class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())
