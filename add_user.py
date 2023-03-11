import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QLineEdit, \
    QHBoxLayout, QMessageBox, QGridLayout
from clients_db import create_table
from clients_db import submit



class AddUserWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
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

        label_name = QLabel('<font size="4"> Name </font>')
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText('Please enter client name')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_name, 0, 1)

        label_surname = QLabel('<font size="4"> Surname </font>')
        self.lineEdit_surname = QLineEdit()
        self.lineEdit_surname.setPlaceholderText('Please enter client surname')
        layout.addWidget(label_surname, 1, 0)
        layout.addWidget(self.lineEdit_surname, 1, 1)



        button_add = QPushButton('Add user')
        button_add.clicked.connect(self.add)
        layout.addWidget(button_add, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
       # layout.addWidget(button_login, 2, 0, 1, 2)
        #layout.setRowMinimumHeight(2, 75)




        self.setLayout(layout)

    def add(self):
        name = self.lineEdit_name.text()
        surname = self.lineEdit_surname.text()

        submit(name, surname)
        self.parent.refresh_all_patients()
        self.close()