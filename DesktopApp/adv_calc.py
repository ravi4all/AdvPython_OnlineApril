from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    expression = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 742)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 520, 121, 91))
        self.pushButton_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(570, 170, 421, 91))
        self.lineEdit.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(570, 330, 421, 91))
        self.lineEdit_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 451, 71))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 520, 121, 91))
        self.pushButton_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 340, 451, 71))
        self.label_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 520, 121, 91))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 520, 121, 91))
        self.pushButton_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 60, 541, 61))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1011, 701))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 20, 931, 101))
        self.lineEdit_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 260, 121, 71))
        self.pushButton_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 260, 121, 71))
        self.pushButton_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(420, 260, 121, 71))
        self.pushButton_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 360, 121, 71))
        self.pushButton_8.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(230, 360, 121, 71))
        self.pushButton_9.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(50, 360, 121, 71))
        self.pushButton_10.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(420, 470, 121, 71))
        self.pushButton_11.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(230, 470, 121, 71))
        self.pushButton_12.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(50, 470, 121, 71))
        self.pushButton_13.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(420, 580, 121, 71))
        self.pushButton_14.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(230, 580, 121, 71))
        self.pushButton_15.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(50, 580, 121, 71))
        self.pushButton_16.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(600, 260, 151, 71))
        self.pushButton_17.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 165, 165);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setGeometry(QtCore.QRect(600, 360, 151, 71))
        self.pushButton_18.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 165, 165);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setGeometry(QtCore.QRect(600, 470, 151, 71))
        self.pushButton_19.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 165, 165);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame)
        self.pushButton_20.setGeometry(QtCore.QRect(600, 580, 151, 71))
        self.pushButton_20.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 165, 165);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame)
        self.pushButton_21.setGeometry(QtCore.QRect(800, 580, 151, 71))
        self.pushButton_21.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 165, 165);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame)
        self.pushButton_22.setGeometry(QtCore.QRect(800, 360, 151, 71))
        self.pushButton_22.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 165, 165);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame)
        self.pushButton_23.setGeometry(QtCore.QRect(800, 470, 151, 71))
        self.pushButton_23.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 165, 165);")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame)
        self.pushButton_24.setGeometry(QtCore.QRect(800, 260, 151, 71))
        self.pushButton_24.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 165, 165);")
        self.pushButton_24.setObjectName("pushButton_24")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 31))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBasic_Calculator = QtWidgets.QAction(MainWindow)
        self.actionBasic_Calculator.setObjectName("actionBasic_Calculator")
        self.actionAdvance_Calculator = QtWidgets.QAction(MainWindow)
        self.actionAdvance_Calculator.setObjectName("actionAdvance_Calculator")
        self.actionScientific_Calculator = QtWidgets.QAction(MainWindow)
        self.actionScientific_Calculator.setObjectName("actionScientific_Calculator")
        self.menuOptions.addAction(self.actionBasic_Calculator)
        self.menuOptions.addAction(self.actionAdvance_Calculator)
        self.menuOptions.addAction(self.actionScientific_Calculator)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "/"))
        self.label_2.setText(_translate("MainWindow", "Enter first number"))
        self.pushButton_4.setText(_translate("MainWindow", "*"))
        self.label_3.setText(_translate("MainWindow", "Enter second number"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "Welcome to Basic Calculator"))
        self.pushButton_5.setText(_translate("MainWindow", "7"))
        self.pushButton_6.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "9"))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_9.setText(_translate("MainWindow", "5"))
        self.pushButton_10.setText(_translate("MainWindow", "4"))
        self.pushButton_11.setText(_translate("MainWindow", "3"))
        self.pushButton_12.setText(_translate("MainWindow", "2"))
        self.pushButton_13.setText(_translate("MainWindow", "1"))
        self.pushButton_14.setText(_translate("MainWindow", "%"))
        self.pushButton_15.setText(_translate("MainWindow", "0"))
        self.pushButton_16.setText(_translate("MainWindow", "."))
        self.pushButton_17.setText(_translate("MainWindow", "+"))
        self.pushButton_18.setText(_translate("MainWindow", "-"))
        self.pushButton_19.setText(_translate("MainWindow", "/"))
        self.pushButton_20.setText(_translate("MainWindow", "*"))
        self.pushButton_21.setText(_translate("MainWindow", "="))
        self.pushButton_22.setText(_translate("MainWindow", "+/-"))
        self.pushButton_23.setText(_translate("MainWindow", "1/x"))
        self.pushButton_24.setText(_translate("MainWindow", "C"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionBasic_Calculator.setText(_translate("MainWindow", "Basic Calculator"))
        self.actionAdvance_Calculator.setText(_translate("MainWindow", "Advance Calculator"))
        self.actionScientific_Calculator.setText(_translate("MainWindow", "Scientific Calculator"))

        self.frame.hide()
        self.initEvents()
        self.lineEdit_3.setReadOnly(True)

    def initEvents(self):
        self.actionAdvance_Calculator.triggered.connect(self.showAdvCalc)
        self.actionBasic_Calculator.triggered.connect(self.showBasicCalc)

        buttons = [self.pushButton_5,self.pushButton_6,self.pushButton_7,
                   self.pushButton_8,self.pushButton_9,self.pushButton_10,
                   self.pushButton_11,self.pushButton_12,self.pushButton_13,
                   self.pushButton_15]

        operators = [self.pushButton_17,self.pushButton_18,self.pushButton_19,
                     self.pushButton_20]

        for i in range(len(buttons)):
            buttons[i].clicked.connect(self.appendNumbers)

        for i in range(len(operators)):
            operators[i].clicked.connect(self.appendOperators)

        self.pushButton_21.clicked.connect(self.calculate)

    def showBasicCalc(self):
        self.frame.hide()

    def showAdvCalc(self):
        self.frame.show()

    def appendNumbers(self):
        btn = self.sender()
        num = btn.text()
        self.expression += num
        self.lineEdit_3.setText(self.expression)
        self.temp = self.lineEdit_3.text()

    def appendOperators(self):
        btn = self.sender()
        opr = btn.text()
        self.expression = self.temp + opr
        self.lineEdit_3.setText(self.expression)


    def calculate(self):
        result = eval(self.expression)
        self.lineEdit_3.setText(str(result))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
