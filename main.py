import random
import string
import sys

from PyQt6 import QtWidgets, QtGui, QtCore, uic
from PyQt6.QtWidgets import QFileDialog, QLabel

from Resource.PassGen import Ui_MainWindow


class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.rand_lower = None
        self.rand_upper = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_copy.clicked.connect(self.copyPass)
        self.ui.chb_number.stateChanged.connect(self.configPass)
        self.ui.chb_char.stateChanged.connect(self.configPass)
        self.ui.le_len_pass.textChanged.connect(self.configPass)
        self.ui.rb_one.clicked.connect(self.configPass)
        self.ui.rb_two.clicked.connect(self.configPass)
        self.ui.rb_three.clicked.connect(self.configPass)
        self.UPPERCASE_CHARACTERS = string.ascii_uppercase
        self.LOWERCASE_CHARACTERS = string.ascii_lowercase
        self.DIGITS = string.digits
        self.SYMBOLS = string.punctuation
        self.rand_digit = ''
        self.rand_symbol = ''
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
        if self.ui.chb_number.isChecked():
            self.rand_digit = random.choice(self.DIGITS)
        else:
            self.rand_digit = ''
        if self.ui.chb_char.isChecked():
            self.rand_symbol = random.choice(self.SYMBOLS)
        else:
            self.rand_symbol = ''
        self._typePassWord()
        self.genPass(self.typePassWord, self.lenPass)

    def _typePassWord(self):
        if self.ui.rb_one.isChecked():
            self.typePassWord = 1
        elif self.ui.rb_two.isChecked():
            self.typePassWord = 2
        else:
            self.typePassWord = 3

    def _random(self, types):
        return random.choice(types)

    def genPass(self, typePass, lenpass):
        word = ''
        for i in range(lenpass):
            self.rand_upper = self._random(self.UPPERCASE_CHARACTERS)
            self.rand_lower = self._random(self.LOWERCASE_CHARACTERS)
            if self.ui.chb_number.isChecked():
                self.rand_digit = self._random(self.DIGITS)
            if self.ui.chb_char.isChecked():
                self.rand_symbol = self._random(self.SYMBOLS)
            if typePass == 1:
                if len(word) != lenpass:
                    word = f"{word}{self.rand_upper}{self.rand_lower}{self.rand_digit}{self.rand_symbol}"
                    if len(word) < lenpass:
                        continue
                    else:
                        self.ui.passWord.setText(str(word[0:lenpass]))
                        break
                else:
                    break
            elif typePass == 2:
                if len(word) != lenpass:
                    word = f"{word}{self.rand_upper}{self.rand_lower}{self.rand_digit}{self.rand_symbol}"
                    if len(word) < lenpass:
                        continue
                    else:
                        self.ui.passWord.setText(f"{word[0:int(lenpass / 2)]}-{word[int(lenpass / 2):]}")
                        break
                else:
                    break
            else:
                if len(word) != lenpass:
                    word = f"{word}{self.rand_upper}{self.rand_lower}{self.rand_digit}{self.rand_symbol}"
                    if len(word) < lenpass:
                        continue
                    else:
                        self.ui.passWord.setText(
                            f"{word[0:int(lenpass / 3)]}-{word[int(lenpass / 3):int(lenpass / 3) + int(lenpass / 3)]}-{word[int(lenpass / 3) + int(lenpass / 3):]}")
                        break
                else:
                    break

    def copyPass(self):
        clipPass = self.ui.passWord.text()
        ccc = QtGui.QGuiApplication.clipboard()
        ccc.clear()
        ccc.setText(clipPass)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = myWindow()
    application.show()
    sys.exit(app.exec())
