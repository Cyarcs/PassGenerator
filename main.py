import random
import string
import sys

from PyQt6 import QtWidgets, QtGui

from Resource.PassGen import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.rand_lower = None
        self.rand_upper = None
        self.typePasWord = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_copy.clicked.connect(self.copypass)
        self.ui.chb_number.stateChanged.connect(self.configpass)
        self.ui.chb_char.stateChanged.connect(self.configpass)
        self.ui.le_len_pass.textChanged.connect(self.configpass)
        self.ui.rb_one.clicked.connect(self.configpass)
        self.ui.rb_two.clicked.connect(self.configpass)
        self.ui.rb_three.clicked.connect(self.configpass)
        self.UPPERCASE_CHARACTERS = string.ascii_uppercase
        self.LOWERCASE_CHARACTERS = string.ascii_lowercase
        self.DIGITS = string.digits
        self.SYMBOLS = string.punctuation
        self.rand_digit = ''
        self.rand_symbol = ''
        self.lenPass = None
        self.configpass()

    def configpass(self):
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
        self.typepassword()
        self.genpass(self.typePasWord, self.lenPass)

    def typepassword(self):
        if self.ui.rb_one.isChecked():
            self.typePasWord = 1
        elif self.ui.rb_two.isChecked():
            self.typePasWord = 2
        else:
            self.typePasWord = 3

    @staticmethod
    def randomchoice(types):
        return random.choice(types)

    def genpass(self, typepass, lenpass):
        word = ''
        for i in range(lenpass):
            self.rand_upper = self.randomchoice(self.UPPERCASE_CHARACTERS)
            self.rand_lower = self.randomchoice(self.LOWERCASE_CHARACTERS)
            if self.ui.chb_number.isChecked():
                self.rand_digit = self.randomchoice(self.DIGITS)
            if self.ui.chb_char.isChecked():
                self.rand_symbol = self.randomchoice(self.SYMBOLS)
            if typepass == 1:
                if len(word) != lenpass:
                    word = f"{word}{self.rand_upper}{self.rand_lower}{self.rand_digit}{self.rand_symbol}"
                    if len(word) < lenpass:
                        continue
                    else:
                        self.ui.passWord.setText(str(word[0:lenpass]))
                        break
                else:
                    break
            elif typepass == 2:
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
                            f"{word[0:int(lenpass / 3)]}-{word[int(lenpass / 3):int(lenpass / 3) + int(lenpass / 3)]}"
                            f"-{word[int(lenpass / 3) + int(lenpass / 3):]}")
                        break
                else:
                    break

    def copypass(self):
        clippass = self.ui.passWord.text()
        ccc = QtGui.QGuiApplication.clipboard()
        ccc.clear()
        ccc.setText(clippass)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
