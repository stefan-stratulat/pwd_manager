import random
import string
import re
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

#charachters to form password
letters = string.ascii_letters #all upper and lower case letters
numbers = random.randint(0,9) #random number 0 to 9
special = "@$!%*#?&" #special charachters


# def validator():
#     reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
#     #compiling regex
#     pat = re.compile(reg)
#     #searching regex
#     match = re.search(pat, pwd)
#     #validation
#     if match:
#         print("Password is valid!")
#     else:
#         print('Password is invalid!')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(223, 436)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gen_pwd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.gen_pwd_btn.setGeometry(QtCore.QRect(30, 90, 161, 51))
        self.gen_pwd_btn.setObjectName("gen_pwd_btn")

        self.pwd_label = QtWidgets.QLabel(self.centralwidget)
        self.pwd_label.setGeometry(QtCore.QRect(20, 160, 191, 51))
        self.pwd_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pwd_label.setScaledContents(True)
        self.pwd_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pwd_label.setObjectName("pwd_label")

        self.save_pwd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_pwd_btn.setGeometry(QtCore.QRect(30, 240, 161, 51))
        self.save_pwd_btn.setObjectName("save_pwd_btn")

        self.website_info = QtWidgets.QLineEdit(self.centralwidget)
        self.website_info.setGeometry(QtCore.QRect(30, 60, 161, 20))
        self.website_info.setObjectName("website_info")
        self.website_info_label = QtWidgets.QLabel(self.centralwidget)
        self.website_info_label.setGeometry(QtCore.QRect(40, 30, 151, 16))
        self.website_info_label.setObjectName("website_info_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 223, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #generate a new pwd everytime is clicked
        self.gen_pwd_btn.clicked.connect(self.pwd_generate)

        self.save_pwd_btn.clicked.connect(self.save)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PWD Manager"))
        self.gen_pwd_btn.setText(_translate("MainWindow", "Generate Password"))
        self.pwd_label.setText(_translate("MainWindow", "Your password will appear here"))
        self.save_pwd_btn.setText(_translate("MainWindow", "Save Password"))
        self.website_info_label.setText(_translate("MainWindow", "Add website to the box below"))

    #password generator
    def pwd_generate(self):
        pwd = ''
        while len(pwd)<15:
            pwd = pwd + random.choice(random.choice(letters)+str(numbers)+random.choice(special))
        #change pwd_label with the current pwd, once the gen_pwd_btn is clicked
        self.pwd_label.setText(pwd)

    #save password and wesbite info in db
    def save(self):
        conn = sqlite3.connect('pwd_store.db')
        c = conn.cursor()
        c.execute('INSERT INTO pwd_storage VALUES(:website,:password)',
                {"website": self.website_info.text(),
                "password": self.pwd_label.text()
                })
        conn.commit()
        conn.close()

        self.website_info.clear()
        self.pwd_label.setText("Generate a new password")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


