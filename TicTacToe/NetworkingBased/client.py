from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import socket,threading, json

class Ui_MainWindow(QtWidgets.QMainWindow):
    combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 110, 121, 111))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 110, 121, 111))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 110, 121, 111))
        self.pushButton_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 230, 121, 111))
        self.pushButton_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 230, 121, 111))
        self.pushButton_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(490, 230, 121, 111))
        self.pushButton_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 350, 121, 111))
        self.pushButton_7.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 350, 121, 111))
        self.pushButton_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(490, 350, 121, 111))
        self.pushButton_9.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(280, 10, 241, 51))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 421, 61))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(530, 200, 141, 51))
        self.comboBox.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 340, 341, 91))
        self.pushButton_10.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 127);")
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
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
        # self.label.setText(_translate("MainWindow", "Tic Tac Toe"))
        # self.label_2.setText(_translate("MainWindow", "Choose your Character"))
        # self.comboBox.setItemText(0, _translate("MainWindow", "0"))
        # self.comboBox.setItemText(1, _translate("MainWindow", "1"))
        # self.pushButton_10.setText(_translate("MainWindow", "Start Game"))
        #
        # self.pushButton_10.clicked.connect(self.startGame)

        threading.Thread(target=self.check).start()

        self.frame.hide()

        self.btns = [self.pushButton,self.pushButton_2,self.pushButton_3,
                     self.pushButton_4, self.pushButton_5, self.pushButton_6,
                     self.pushButton_7, self.pushButton_8, self.pushButton_9]

        for i in range(len(self.btns)):
            self.btns[i].clicked.connect(self.userPos)

    def userPos(self):
        try:
            btn = self.sender()
            btn.setText(self.clientCh)
            btn.setDisabled(True)
            self.pos = self.btns.index(btn)
            self.checkWinner(self.pos, self.clientCh)
            self.sendPosition(self.pos)
        except BaseException as ex:
            print(ex)

    def setServerPos(self,pos,ch):
        btn = self.btns[pos]
        btn.setText(ch)
        btn.setDisabled(True)
        self.pos = self.btns.index(btn)
        self.checkWinner(self.pos, self.serverCh)

    def sendPosition(self,pos):
        msg = {"pos": pos}
        msg = json.dumps(msg)
        self.s.send(msg.encode())

    def checkWinner(self, pos, ch):
        for i in range(len(self.combinations)):
            if pos in self.combinations[i]:
                index = self.combinations[i].index(pos)
                self.combinations[i][index] = ch

        for i in range(len(self.combinations)):
            if self.combinations[i][0] == ch and self.combinations[i][1] == ch and self.combinations[i][2] == ch:
                QMessageBox.about(self, "Game Over", "{} win".format(ch))

    def check(self):
        self.s = socket.socket()
        port = 9001
        self.s.connect(('127.0.0.1', port))
        while True:
            recv_msg = self.s.recv(10000)
            print("Client : ", recv_msg)
            recv_msg = json.loads(recv_msg)
            self.serverPos = recv_msg['pos']
            self.clientCh = recv_msg['clientCh']
            self.serverCh = recv_msg['serverCh']
            self.setServerPos(self.serverPos,self.serverCh)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
