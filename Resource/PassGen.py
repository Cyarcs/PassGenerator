# Form implementation generated from reading ui file '.\PassGen_ui.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 200)
        MainWindow.setMinimumSize(QtCore.QSize(450, 200))
        MainWindow.setMaximumSize(QtCore.QSize(450, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 411, 58))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rb_three = QtWidgets.QRadioButton(self.groupBox)
        self.rb_three.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rb_three.setFont(font)
        self.rb_three.setObjectName("rb_three")
        self.horizontalLayout_4.addWidget(self.rb_three)
        self.rb_two = QtWidgets.QRadioButton(self.groupBox)
        self.rb_two.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rb_two.setFont(font)
        self.rb_two.setObjectName("rb_two")
        self.horizontalLayout_4.addWidget(self.rb_two)
        self.rb_one = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rb_one.setFont(font)
        self.rb_one.setChecked(True)
        self.rb_one.setObjectName("rb_one")
        self.horizontalLayout_4.addWidget(self.rb_one)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(70, 120, 271, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.passWord = QtWidgets.QLineEdit(self.widget)
        self.passWord.setMinimumSize(QtCore.QSize(0, 30))
        self.passWord.setMaxLength(20)
        self.passWord.setReadOnly(True)
        self.passWord.setObjectName("passWord")
        self.horizontalLayout.addWidget(self.passWord)
        self.btn_copy = QtWidgets.QPushButton(self.widget)
        self.btn_copy.setObjectName("btn_copy")
        self.horizontalLayout.addWidget(self.btn_copy)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 411, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.len_pass = QtWidgets.QLabel(self.widget1)
        self.len_pass.setMaximumSize(QtCore.QSize(80, 16777215))
        self.len_pass.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.len_pass.setObjectName("len_pass")
        self.horizontalLayout_2.addWidget(self.len_pass)
        self.le_len_pass = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_len_pass.sizePolicy().hasHeightForWidth())
        self.le_len_pass.setSizePolicy(sizePolicy)
        self.le_len_pass.setMaximumSize(QtCore.QSize(50, 25))
        self.le_len_pass.setInputMask("")
        self.le_len_pass.setMaxLength(2)
        self.le_len_pass.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.le_len_pass.setObjectName("le_len_pass")
        self.horizontalLayout_2.addWidget(self.le_len_pass)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.chb_number = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chb_number.setFont(font)
        self.chb_number.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.chb_number.setObjectName("chb_number")
        self.horizontalLayout_3.addWidget(self.chb_number)
        self.chb_char = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chb_char.setFont(font)
        self.chb_char.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.chb_char.setObjectName("chb_char")
        self.horizontalLayout_3.addWidget(self.chb_char)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pass gen"))
        self.groupBox.setTitle(_translate("MainWindow", "Type"))
        self.rb_three.setText(_translate("MainWindow", "xxx-xxx-xxx"))
        self.rb_two.setText(_translate("MainWindow", "xxx-xxx"))
        self.rb_one.setText(_translate("MainWindow", "xxx"))
        self.btn_copy.setText(_translate("MainWindow", "Copy"))
        self.len_pass.setText(_translate("MainWindow", "Length pass"))
        self.le_len_pass.setText(_translate("MainWindow", "6"))
        self.chb_number.setText(_translate("MainWindow", "Numbers"))
        self.chb_char.setText(_translate("MainWindow", "Symbols"))
