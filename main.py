import random
import string
import sys

from PyQt6 import QtWidgets, QtGui, QtCore, uic
from PyQt6.QtWidgets import QFileDialog, QLabel

from Resource.PassGen import Ui_MainWindow


class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.genPass()
        self.ui.btn_copy.clicked.connect(self.copy)
        self.ui.chb_number.stateChanged.connect(self.configPass)
        self.ui.chb_char.stateChanged.connect(self.configPass)
        self.ui.le_len_pass.textChanged.connect(self.configPass)
        self.ui.rb_one.clicked.connect(self.configPass)
        self.ui.rb_two.clicked.connect(self.configPass)
        self.ui.rb_three.clicked.connect(self.configPass)
        self.UPPERCASE_CHARACTERS = string.ascii_uppercase
        self.LOWERCASE_CHARACTERS = string.ascii_lowercase
        self.rand_upper = random.choice(self.UPPERCASE_CHARACTERS)
        self.rand_lower = random.choice(self.LOWERCASE_CHARACTERS)
        self.DIGITS = string.digits
        self.SYMBOLS = string.punctuation
        self.rand_digit = None
        self.rand_symbol = None
        self.lenPass = None
        self.configPass()

    def configPass(self):
        if self.ui.le_len_pass.text() == '':
            self.ui.le_len_pass.setText('0')
            self.lenPass = 0
        elif int(self.ui.le_len_pass.text()) <= 12 and self.ui.le_len_pass.text() != '':
            if self.ui.le_len_pass.text()[0] == '0' and len(self.ui.le_len_pass.text()) == 2:
                self.ui.le_len_pass.setText(self.ui.le_len_pass.text()[1])
            self.lenPass = int(self.ui.le_len_pass.text())
        elif int(self.ui.le_len_pass.text()) > 12 and self.ui.le_len_pass.text() != '':
            self.ui.le_len_pass.setText('12')
            self.lenPass = 12
        else:
            self.lenPass = 0
        if self.ui.chb_number.checkState() == 2:
            self.rand_digit = random.choice(self.DIGITS)
        else:
            self.rand_digit = None
        if self.ui.chb_char.checkState() == 2:
            self.rand_symbol = random.choice(self.SYMBOLS)
        else:
            self.rand_symbol = None
        self._typePassWord()

    def _typePassWord(self):
        if self.ui.rb_one.isChecked():
            self.typePassWord = 1
        elif self.ui.rb_two.isChecked():
            self.typePassWord = 2
        else:
            self.typePassWord = 2

    def genPass(self):
        pass

    def copy(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = myWindow()
    application.show()
    sys.exit(app.exec())
