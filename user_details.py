import sys
import sqlite3

from PyQt6.QtGui import QAction
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QLineEdit, \
    QHBoxLayout, QMessageBox, QGridLayout, QToolBar, QSizePolicy, QTableView, QListWidget
from logins_db import create_table
from logins_db import submit
from logins_db import is_login_exists




class UserDetailWindow(QWidget):
    def __init__(self, parent, name, surname):
        super().__init__()
        self.parent = parent
        self.name_ = name
        self.surname_ = surname
        self.initUI()

       


    def initUI(self):
        self.setWindowTitle('Menu')
        self.setGeometry(300, 300, 500, 520)

        # Set the background color to white
        self.setStyleSheet('background-color: white;')

        #create a toolbar
        self.toolbar = QToolBar(self)
        self.toolbar.setStyleSheet("QToolBar {background-color: #F5F5F5; border: none;}")
        self.toolbar.setIconSize(self.toolbar.iconSize() * 1.5)


        self.calendar_button = QPushButton("Calendar", self)
        self.toolbar.addWidget(self.calendar_button)

        self.diagnostics_button = QPushButton("Diagnostics", self)
        self.toolbar.addWidget(self.diagnostics_button)

        self.log_out_button = QPushButton("Back", self)
        self.toolbar.addWidget(self.log_out_button)
        self.log_out_button.clicked.connect(self.log_out)

        # Create a widget to hold the patient search UI
        self.patient_search_widget = QWidget(self)
        self.patient_search_widget.setStyleSheet('background-color: white;')

        # Create a label to display the user's name and surname
        self.name_label = QLabel()
        self.name_label.setText('Patient: ' + str(self.name_) + ' ' + str(self.surname_))

        self.visit_label = QLabel()
        self.visit_label.setText('Last appointments: ')
        # Create a list widget to display patients
        self.patient_list_widget = QListWidget(self.patient_search_widget)

        # Create a layout to hold the patient search UI
        self.patient_search_layout = QVBoxLayout(self.patient_search_widget)
        self.patient_search_layout.addWidget(self.name_label)
        self.patient_search_layout.addWidget(self.visit_label)
        self.patient_search_layout.addWidget(self.patient_list_widget)

        # Set the patient search widget to be hidden by default
        self.patient_search_widget.setVisible(True)

        # Add the toolbar and patient search widget to the main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.patient_search_widget)



    #    self.patient_list_widget.itemClicked.connect(self.show_patient_details)



    def log_out(self):
        self.parent.show()
        self.close()





