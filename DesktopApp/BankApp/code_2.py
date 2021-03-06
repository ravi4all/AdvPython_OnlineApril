from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 120, 221, 91))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 330, 331, 91))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(410, 140, 351, 71))
        self.comboBox.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 340, 351, 71))
        self.comboBox_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(810, 140, 211, 61))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 340, 211, 61))
        self.pushButton_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1091, 691))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(340, 80, 161, 51))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(490, 80, 261, 51))
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(120, 200, 391, 61))
        self.label_5.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(120, 320, 391, 61))
        self.label_6.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(570, 190, 341, 71))
        self.lineEdit.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(570, 320, 341, 71))
        self.lineEdit_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 500, 241, 71))
        self.pushButton_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1081, 661))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(290, 10, 261, 51))
        self.label_7.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(530, 10, 261, 51))
        self.label_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(80, 100, 291, 51))
        self.label_9.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(80, 180, 291, 51))
        self.label_10.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(80, 260, 291, 51))
        self.label_11.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(80, 340, 291, 51))
        self.label_12.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(80, 430, 291, 51))
        self.label_13.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(480, 100, 411, 51))
        self.lineEdit_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(480, 180, 411, 51))
        self.lineEdit_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(480, 270, 411, 51))
        self.lineEdit_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(480, 350, 411, 51))
        self.lineEdit_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(480, 430, 411, 51))
        self.lineEdit_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 540, 341, 81))
        self.pushButton_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1081, 671))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(330, 20, 461, 61))
        self.label_14.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 140, 331, 131))
        self.pushButton_5.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 320, 331, 131))
        self.pushButton_6.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(560, 140, 331, 131))
        self.pushButton_7.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8.setGeometry(QtCore.QRect(560, 320, 331, 131))
        self.pushButton_8.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_st = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_st.setGeometry(QtCore.QRect(170, 500, 331, 131))
        self.pushButton_st.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(85, 170, 255);")
        self.pushButton_st.setObjectName("pushButton_st")

        self.pushButton_dl = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_dl.setGeometry(QtCore.QRect(560, 500, 331, 131))
        self.pushButton_dl.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(85, 170, 255);")
        self.pushButton_dl.setObjectName("pushButton_dl")

        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1091, 671))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(410, 10, 261, 51))
        self.label_15.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(80, 110, 321, 41))
        self.label_16.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(80, 230, 321, 41))
        self.label_17.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setGeometry(QtCore.QRect(80, 340, 321, 41))
        self.label_18.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(530, 90, 411, 81))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(530, 210, 411, 81))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_9.setGeometry(QtCore.QRect(580, 330, 271, 61))
        self.pushButton_9.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_10.setGeometry(QtCore.QRect(350, 520, 331, 81))
        self.pushButton_10.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 1081, 661))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(450, 10, 251, 41))
        self.label_19.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_5)
        self.tableWidget.setGeometry(QtCore.QRect(150, 110, 771, 501))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 1091, 671))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        self.label_20.setGeometry(QtCore.QRect(150, 150, 231, 61))
        self.label_20.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_6)
        self.label_21.setGeometry(QtCore.QRect(150, 250, 231, 61))
        self.label_21.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_6)
        self.label_22.setGeometry(QtCore.QRect(150, 350, 231, 61))
        self.label_22.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_6)
        self.label_23.setGeometry(QtCore.QRect(450, 150, 471, 71))
        self.label_23.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        self.label_24.setGeometry(QtCore.QRect(450, 250, 471, 71))
        self.label_24.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_6)
        self.label_25.setGeometry(QtCore.QRect(450, 360, 471, 71))
        self.label_25.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 31))
        self.menubar.setObjectName("menubar")
        self.menuLogin_Options = QtWidgets.QMenu(self.menubar)
        self.menuLogin_Options.setObjectName("menuLogin_Options")
        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")
        self.menuLoan_Management = QtWidgets.QMenu(self.menubar)
        self.menuLoan_Management.setObjectName("menuLoan_Management")
        self.menuApply_for_loan = QtWidgets.QMenu(self.menuLoan_Management)
        self.menuApply_for_loan.setObjectName("menuApply_for_loan")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_Account = QtWidgets.QAction(MainWindow)
        self.actionCreate_Account.setObjectName("actionCreate_Account")
        self.actionBalance_Enquiry = QtWidgets.QAction(MainWindow)
        self.actionBalance_Enquiry.setObjectName("actionBalance_Enquiry")
        self.actionDeposit = QtWidgets.QAction(MainWindow)
        self.actionDeposit.setObjectName("actionDeposit")
        self.actionFund_Transfer = QtWidgets.QAction(MainWindow)
        self.actionFund_Transfer.setObjectName("actionFund_Transfer")
        self.actionView_Customers = QtWidgets.QAction(MainWindow)
        self.actionView_Customers.setObjectName("actionView_Customers")
        self.actionUpdate_Customers = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Customers.setObjectName("actionUpdate_Customers")
        self.actionDelete_Customer = QtWidgets.QAction(MainWindow)
        self.actionDelete_Customer.setObjectName("actionDelete_Customer")
        self.actionMy_Loans = QtWidgets.QAction(MainWindow)
        self.actionMy_Loans.setObjectName("actionMy_Loans")
        self.actionCheck_Availability = QtWidgets.QAction(MainWindow)
        self.actionCheck_Availability.setObjectName("actionCheck_Availability")
        self.actionHome_Loan = QtWidgets.QAction(MainWindow)
        self.actionHome_Loan.setObjectName("actionHome_Loan")
        self.actionCar_Loan = QtWidgets.QAction(MainWindow)
        self.actionCar_Loan.setObjectName("actionCar_Loan")
        self.actionEducation_Loan = QtWidgets.QAction(MainWindow)
        self.actionEducation_Loan.setObjectName("actionEducation_Loan")
        self.actionStatement = QtWidgets.QAction(MainWindow)
        self.actionStatement.setObjectName("actionStatement")
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setObjectName("actionHome")
        self.menuLogin_Options.addAction(self.actionHome)
        self.menuLogin_Options.addAction(self.actionCreate_Account)
        self.menuLogin_Options.addAction(self.actionBalance_Enquiry)
        self.menuLogin_Options.addAction(self.actionDeposit)
        self.menuLogin_Options.addAction(self.actionFund_Transfer)
        self.menuLogin_Options.addAction(self.actionStatement)
        self.menuAdmin.addAction(self.actionView_Customers)
        self.menuAdmin.addAction(self.actionUpdate_Customers)
        self.menuAdmin.addAction(self.actionDelete_Customer)
        self.menuApply_for_loan.addAction(self.actionHome_Loan)
        self.menuApply_for_loan.addAction(self.actionCar_Loan)
        self.menuApply_for_loan.addAction(self.actionEducation_Loan)
        self.menuLoan_Management.addAction(self.actionMy_Loans)
        self.menuLoan_Management.addAction(self.menuApply_for_loan.menuAction())
        self.menuLoan_Management.addAction(self.actionCheck_Availability)
        self.menubar.addAction(self.menuLogin_Options.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuLoan_Management.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Login As"))
        self.label_2.setText(_translate("MainWindow", "Register As"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Customer"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Customer"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Register"))
        self.label_3.setText(_translate("MainWindow", "Login As"))
        self.label_5.setText(_translate("MainWindow", "Enter Login ID"))
        self.label_6.setText(_translate("MainWindow", "Enter Password"))
        self.pushButton_3.setText(_translate("MainWindow", "Login"))
        self.label_7.setText(_translate("MainWindow", "Register As"))
        self.label_9.setText(_translate("MainWindow", "Enter Name"))
        self.label_10.setText(_translate("MainWindow", "Enter Email ID"))
        self.label_11.setText(_translate("MainWindow", "Enter Password"))
        self.label_12.setText(_translate("MainWindow", "Enter Mobile No"))
        self.label_13.setText(_translate("MainWindow", "Select State"))
        self.pushButton_4.setText(_translate("MainWindow", "Register"))
        self.label_14.setText(_translate("MainWindow", "Welcome to ICICI Bank"))
        self.pushButton_5.setText(_translate("MainWindow", "Create Account"))
        self.pushButton_6.setText(_translate("MainWindow", "Balance Enquiry"))
        self.pushButton_7.setText(_translate("MainWindow", "Funds Transfer"))
        self.pushButton_8.setText(_translate("MainWindow", "Apply Loan"))
        self.label_15.setText(_translate("MainWindow", "Create Account"))
        self.label_16.setText(_translate("MainWindow", "Enter Name"))
        self.label_17.setText(_translate("MainWindow", "Enter Email ID"))
        self.label_18.setText(_translate("MainWindow", "Upload Photograph"))
        self.pushButton_9.setText(_translate("MainWindow", "Upload"))
        self.pushButton_10.setText(_translate("MainWindow", "Create Account"))
        self.label_19.setText(_translate("MainWindow", "Transactions"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Acc No"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cr / Dr"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "22 May 2020"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "324234234"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "4500"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Cr"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_20.setText(_translate("MainWindow", "Name"))
        self.label_21.setText(_translate("MainWindow", "Acc No"))
        self.label_22.setText(_translate("MainWindow", "Total Balance"))
        self.menuLogin_Options.setTitle(_translate("MainWindow", "User"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.menuLoan_Management.setTitle(_translate("MainWindow", "Loan Management"))
        self.menuApply_for_loan.setTitle(_translate("MainWindow", "Apply for loan"))
        self.actionCreate_Account.setText(_translate("MainWindow", "Create Account"))
        self.actionBalance_Enquiry.setText(_translate("MainWindow", "Balance Enquiry"))
        self.actionDeposit.setText(_translate("MainWindow", "Deposit"))
        self.actionFund_Transfer.setText(_translate("MainWindow", "Fund Transfer"))
        self.actionView_Customers.setText(_translate("MainWindow", "View Customers"))
        self.actionUpdate_Customers.setText(_translate("MainWindow", "Update Customers"))
        self.actionDelete_Customer.setText(_translate("MainWindow", "Delete Customer"))
        self.actionMy_Loans.setText(_translate("MainWindow", "My Loans"))
        self.actionCheck_Availability.setText(_translate("MainWindow", "Check Availability"))
        self.actionHome_Loan.setText(_translate("MainWindow", "Home Loan"))
        self.actionCar_Loan.setText(_translate("MainWindow", "Car Loan"))
        self.actionEducation_Loan.setText(_translate("MainWindow", "Education Loan"))
        self.actionStatement.setText(_translate("MainWindow", "Statement"))
        self.actionHome.setText(_translate("MainWindow", "Dashboard"))
        self.pushButton_st.setText(_translate("MainWindow", "View Statement"))
        self.pushButton_dl.setText(_translate("MainWindow", "Delete Account"))

        self.frame.hide()
        self.initEvents()

    def initEvents(self):
        self.pushButton.clicked.connect(self.loginPage)
        self.pushButton_2.clicked.connect(self.registerPage)
        self.pushButton_3.clicked.connect(self.loginCheck)

        self.actionStatement.triggered.connect(self.showStatement)

    def loginPage(self):
        self.frame.show()
        self.frame_2.hide()
        self.label_4.setText(self.comboBox.currentText())

    def registerPage(self):
        self.frame.show()
        self.frame_3.hide()
        self.label_4.setText(self.comboBox_2.currentText())

    def loginCheck(self):
        user_id = self.lineEdit.text()
        user_pwd = self.lineEdit_2.text()
        # print(user_id, user_pwd)
        self.frame_2.show()
        self.label_23.setText("Ram")
        self.label_24.setText("231231232")
        self.label_25.setText("5000")

    def showStatement(self):
        data = (('22/05/2020', '3435345353', '45453', 'Cr'),
                ('22/05/2020', '3454346768', '453', 'Dr'),
                ('22/05/2020', '3676423422', '15453', 'Dr'),
                ('22/05/2020', '1234343466', '454', 'Cr'))
        self.frame_5.show()
        self.frame_6.hide()

        try:
            row_count = len(data)
            self.tableWidget.setRowCount(row_count)
            for i in range(row_count):
                for j in range(4):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, j, item)
                    item.setText(data[i][j])
        except BaseException as ex:
            print(ex)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
