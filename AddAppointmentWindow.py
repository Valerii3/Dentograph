import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QLineEdit, \
    QHBoxLayout, QMessageBox, QGridLayout, QDateEdit, QTimeEdit
from appointments_db import create_table
from appointments_db import submit



class AddAppointmentWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI()

        # Create a database connection
        create_table()

    def initUI(self):
        self.setWindowTitle('Appointment')
        self.setGeometry(300, 300, 500, 520)

        # Set the background color to white
        self.setStyleSheet('background-color: white;')

        # Create labels and line edits for client name and surname
        client_name_label = QLabel('Client Name:')
        self.client_name_edit = QLineEdit()
        client_surname_label = QLabel('Client Surname:')
        self.client_surname_edit = QLineEdit()

        # Create date and time input widgets for the appointment
        appointment_date_label = QLabel('Appointment Date:')
        self.appointment_date_edit = QDateEdit()
        self.appointment_date_edit.setDisplayFormat('yyyy-MM-dd')
        self.appointment_time_edit = QTimeEdit()
        self.appointment_time_edit.setDisplayFormat('HH:mm')

        # Create a button to add the appointment
        add_appointment_button = QPushButton('Add Appointment')
        add_appointment_button.clicked.connect(self.add_appointment)

        # Create a grid layout to organize the widgets
        grid_layout = QGridLayout()
        grid_layout.addWidget(client_name_label, 0, 0)
        grid_layout.addWidget(self.client_name_edit, 0, 1)
        grid_layout.addWidget(client_surname_label, 1, 0)
        grid_layout.addWidget(self.client_surname_edit, 1, 1)
        grid_layout.addWidget(appointment_date_label, 2, 0)
        grid_layout.addWidget(self.appointment_date_edit, 2, 1)
        grid_layout.addWidget(self.appointment_time_edit, 3, 1)
        grid_layout.addWidget(add_appointment_button, 4, 0, 1, 2)

        # Set the main layout of the window
        main_layout = QVBoxLayout()
        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    def add_appointment(self):

        submit(self.client_name_edit.text(), self.client_surname_edit.text(),
               self.appointment_date_edit.text(), self.appointment_time_edit.text())
        self.parent.refresh_all_appointments()
        self.parent.show()
        self.close()
