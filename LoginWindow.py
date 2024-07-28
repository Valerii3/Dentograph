import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QLineEdit, \
    QHBoxLayout, QMessageBox, QGridLayout
from logins_db import create_table
from logins_db import submit
from logins_db import is_user_exists
from menu import MenuWindow



is_success = False


class LoginWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.initUI()
        self.parent = parent

    def initUI(self):
        self.setWindowTitle('Registration')
        self.setGeometry(300, 300, 500, 520)

        # Set the background color to white
        self.setStyleSheet('background-color: white;')

        # Add a login label and input box
        layout = QGridLayout()

        label_login = QLabel('<font size="4"> Login </font>')
        self.lineEdit_login = QLineEdit()
        self.lineEdit_login.setPlaceholderText('Please enter your username')
        layout.addWidget(label_login, 0, 0)
        layout.addWidget(self.lineEdit_login, 0, 1)


        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)


        button_login = QPushButton('Log in')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        button_back = QPushButton('Back')
        button_back.clicked.connect(self.go_back)
        layout.addWidget(button_back, 3, 0, 1, 2)
        layout.setRowMinimumHeight(3, 75)
        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()

        if (self.check_empty_data() == False):
            return

        if (is_user_exists(self.lineEdit_login.text(), self.lineEdit_password.text())):
            self.menu_window = MenuWindow(self.parent)
            self.menu_window.show()
            self.close()
        else:
            msg.setText('User does not exist')
            msg.exec()
            return


    def check_empty_data(self):
        msg = QMessageBox()

        if (self.lineEdit_login.text() == ""):
            msg.setText('Login is empty')
            msg.exec()
            return False
        elif (self.lineEdit_password.text() == ""):
            msg.setText('Password is empty')
            msg.exec()
            return False

        return True

    def go_back(self):
        self.parent.show()
        self.close()

def check_login():
    return is_success == True