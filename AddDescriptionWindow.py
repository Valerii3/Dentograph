from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QGridLayout
from clients_db import add_description

class AddDescriptionWindow(QWidget):
    def __init__(self, parent, name_, surname_):
        super().__init__()
        self.parent = parent
        self.name_ = name_
        self.surname_ = surname_
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Registration')
        self.setGeometry(300, 300, 500, 520)

        # Set the background color to white
        # self.setStyleSheet('background-color: white;')

        # Add a login label and input box
        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Description </font>')
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setFixedSize(300, 300)
        self.lineEdit_name.setPlaceholderText('Please add description')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_name, 0, 1)



        button_add = QPushButton('Add description')
        button_add.clicked.connect(self.add)
        layout.addWidget(button_add, 1, 0, 1, 2)
        layout.setRowMinimumHeight(1, 75)
        # layout.addWidget(button_login, 2, 0, 1, 2)
        # layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def add(self):
        descr = self.lineEdit_name.text()


        add_description(descr, self.name_, self.surname_)
        self.parent.refresh_description()
        self.close()