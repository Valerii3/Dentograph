import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QLineEdit, \
    QHBoxLayout, QMessageBox, QGridLayout
from logins_db import create_table
from logins_db import submit
from logins_db import is_login_exists


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # Create a database connection
        create_table()

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
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        label_password_repeat = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password_repeat = QLineEdit()
        self.lineEdit_password_repeat.setPlaceholderText('Please repeat your password')
        layout.addWidget(label_password_repeat, 2, 0)
        layout.addWidget(self.lineEdit_password_repeat, 2, 1)

        label_user_name = QLabel('<font size="4"> Name </font>')
        self.lineEdit_user_name = QLineEdit()
        self.lineEdit_user_name.setPlaceholderText('Please enter your name')
        layout.addWidget(label_user_name, 3, 0)
        layout.addWidget(self.lineEdit_user_name, 3, 1)

        label_user_surname = QLabel('<font size="4"> Surname </font>')
        self.lineEdit_user_surname = QLineEdit()
        self.lineEdit_user_surname.setPlaceholderText('Please enter your Surname')
        layout.addWidget(label_user_surname, 4, 0)
        layout.addWidget(self.lineEdit_user_surname, 4, 1)

        button_login = QPushButton('Add user')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 5, 0, 1, 2)
        layout.setRowMinimumHeight(5, 75)
       # layout.addWidget(button_login, 2, 0, 1, 2)
        #layout.setRowMinimumHeight(2, 75)




        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()

        if (self.check_empty_data() == False):
            return

        if (is_login_exists(self.lineEdit_login.text())):
            msg.setText('Login already exists')
            msg.exec()
            return

        if (self.lineEdit_password.text() != self.lineEdit_password_repeat.text()):
            msg.setText('Passwords do not match')
            msg.exec()

        else:
            msg.setText('Success!')
            msg.exec()
            submit(self.lineEdit_login.text(), self.lineEdit_password.text())
            self.close()

    def check_empty_data(self):
        msg = QMessageBox()

        if (self.lineEdit_login.text() == ""):
            msg.setText('Login is empty')
            msg.exec()
            return False
        elif (self.lineEdit_password.text() == "" or self.lineEdit_password_repeat == ""):
            msg.setText('Password is empty')
            msg.exec()
            return False
        elif (self.lineEdit_user_name.text() == ""):
            msg.setText('Name is empty')
            msg.exec()
            return False
        elif (self.lineEdit_user_surname.text() == ""):
            msg.setText('Surname is empty')
            msg.exec()
            return False
        return True