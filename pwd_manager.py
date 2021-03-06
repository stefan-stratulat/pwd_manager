import random
import string
import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widget_gui import Ui_manager_widget

#charachters to form password
letters = string.ascii_letters #all upper and lower case letters
numbers = random.randint(0,9) #random number 0 to 9
special = "@$!%*#?&" #special charachters

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

        self.manage_pwd = QtWidgets.QPushButton(self.centralwidget)
        self.manage_pwd.setGeometry(QtCore.QRect(30, 290, 161, 51))
        self.manage_pwd.setObjectName("manage_pwd")

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
        #save password and website to db when clicked
        self.save_pwd_btn.clicked.connect(self.save)
        #open manage passwords widgets
        self.manage_pwd.clicked.connect(self.show_manage_passwords)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PWD Manager"))
        self.gen_pwd_btn.setText(_translate("MainWindow", "Generate Password"))
        self.pwd_label.setText(_translate("MainWindow", "Your password will appear here"))
        self.save_pwd_btn.setText(_translate("MainWindow", "Save Password"))
        self.website_info_label.setText(_translate("MainWindow", "Add website to the box below"))
        self.manage_pwd.setText(_translate("MainWindow", "Manage passwords"))

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
        #clear website info and add new text on the password label
        self.website_info.clear()
        self.pwd_label.setText("Generate a new password")

    #open a new widget that shows all saved passwords
    def show_manage_passwords(self):
        self.manager_widget = QtWidgets.QWidget()
        self.ui = Ui_manager_widget()
        self.ui.setupUi(self.manager_widget)
        self.manager_widget.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())