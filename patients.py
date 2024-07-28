import sys
import sqlite3


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QLineEdit, \
    QHBoxLayout, QMessageBox, QGridLayout, QToolBar, QSizePolicy, QTableView, QListWidget
from clients_db import create_table
from add_user import AddUserWindow
from clients_db import get_patients
from user_details import UserDetailWindow


class PatientsWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.initUI()
        self.parent = parent
        self.show_all_patients()

     #   create_table()


    def initUI(self):
        self.setWindowTitle('Menu')
        self.setGeometry(300, 300, 500, 520)

        # Set the background color to white
        self.setStyleSheet('background-color: white;')

        #create a toolbar
        self.toolbar = QToolBar(self)
        self.toolbar.setStyleSheet("QToolBar {background-color: #F5F5F5; border: none;}")
        self.toolbar.setIconSize(self.toolbar.iconSize() * 1.5)

        self.patients_button = QPushButton("Patients", self)
        self.toolbar.addWidget(self.patients_button)

        self.calendar_button = QPushButton("Calendar", self)
        self.toolbar.addWidget(self.calendar_button)

        self.diagnostics_button = QPushButton("Diagnostics", self)
        self.toolbar.addWidget(self.diagnostics_button)

        self.log_out_button = QPushButton("Log out", self)
        self.toolbar.addWidget(self.log_out_button)
        self.log_out_button.clicked.connect(self.log_out)

        # Create a widget to hold the patient search UI
        self.patient_search_widget = QWidget(self)
        self.patient_search_widget.setStyleSheet('background-color: white;')

        # Create a line edit and search button
        self.patient_search_edit = QLineEdit(self.patient_search_widget)
        self.patient_search_edit.setPlaceholderText('Search for patients...')
        self.patient_search_button = QPushButton('Search', self.patient_search_widget)
        self.patient_search_button.clicked.connect(self.search_patients)

        # Create a button to add a new patient
        self.add_patient_button = QPushButton('Add new patient', self.patient_search_widget)
        self.add_patient_button.clicked.connect(self.add_new_patient)

        # Create a list widget to display patients
        self.patient_list_widget = QListWidget(self.patient_search_widget)

        # Create a layout to hold the patient search UI
        self.patient_search_layout = QVBoxLayout(self.patient_search_widget)
        self.patient_search_layout.addWidget(self.patient_search_edit)
        self.patient_search_layout.addWidget(self.patient_search_button)
        self.patient_search_layout.addWidget(self.add_patient_button)
        self.patient_search_layout.addWidget(self.patient_list_widget)

        # Set the patient search widget to be hidden by default
        self.patient_search_widget.setVisible(True)

        # Add the toolbar and patient search widget to the main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.patient_search_widget)

        # Connect the patients button to show the patient search UI
        self.patients_button.clicked.connect(self.show_patient_search)

        self.patient_list_widget.itemClicked.connect(self.show_patient_details)


    def log_out(self):
        self.parent.show()
        self.close()

    def show_patient_search(self):
        self.patient_search_widget.setVisible(True)

    def show_patient_details(self):


        selected_item = self.patient_list_widget.currentItem()
        if selected_item is not None:
            name, surname = selected_item.text().split(' ')
            self.patient_details_window = UserDetailWindow(self, name, surname)
            self.patient_details_window.show()


    def show_all_patients(self):

        patients = get_patients()
        for patient in patients:
            name, surname = patient[1], patient[2]
            self.patient_list_widget.addItem(f'{name} {surname}')

    def refresh_all_patients(self):

        self.patient_list_widget.clear()
        self.show_all_patients()

    def add_new_patient(self):

        self.add_patient_window = AddUserWindow(self)
        self.add_patient_window.show()

    def search_patients(self):
        pass