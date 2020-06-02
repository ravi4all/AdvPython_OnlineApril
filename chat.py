from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    chatData = {
        "Ram" : [
            {"msg" : "hello"},
            {"msg" : "hi there"},
            {"rply" : "hello"},
            {"rply" : "how are you ?"},
            {"msg" : "I am fine.."},
            {"rply" : "Good"}
        ],
        "Shyam" : [
            {"msg" : "hey"},
            {"rply" : "hello"},
            {"msg" : "how are you ?"},
            {"rply" : "I am good.."},
            {"rply" : "How about you ?"},
            {"msg" : "Good"}
        ]
    }

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1187, 790)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 401, 711))
        self.listWidget.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(420, 10, 751, 461))
        self.listWidget_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.listWidget_2.setObjectName("listWidget_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(420, 490, 751, 141))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 660, 201, 61))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 660, 201, 61))
        self.pushButton_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(910, 660, 261, 61))
        self.pushButton_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1187, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton_2.setText(_translate("MainWindow", "Attach File"))
        self.pushButton_3.setText(_translate("MainWindow", "Voice Message"))

        self.showUsers()
        self.listWidget.itemClicked.connect(self.changeUser)
        self.pushButton.clicked.connect(self.sendMessage)

    def showUsers(self):
        self.users = list(self.chatData.keys())
        n = len(self.users)
        for i in range(n):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            item.setText(self.users[i])

    def changeUser(self, item):
        self.listWidget_2.clear()
        try:
            self.current_user = item.text()
            chat = self.chatData[self.current_user]
            for data in chat:
                for key in data:
                    item = QtWidgets.QListWidgetItem()
                    self.listWidget_2.addItem(item)
                    if key == 'msg':
                        item.setText(data[key])
                        item.setTextAlignment(QtCore.Qt.AlignLeft)
                    else:
                        item.setText(data[key])
                        item.setTextAlignment(QtCore.Qt.AlignRight)
        except BaseException as ex:
            print(ex)

    def sendMessage(self):
        msg = self.textEdit.toPlainText()
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item.setText(msg)
        item.setTextAlignment(QtCore.Qt.AlignRight)
        self.textEdit.setText("")
        chat = self.chatData[self.current_user]
        chat.append({'rply':msg})

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
