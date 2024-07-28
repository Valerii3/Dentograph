import sys
import sqlite3

from PyQt5.QtCore import QDate, Qt
from PyQt6.QtGui import QAction
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QLineEdit, \
    QHBoxLayout, QMessageBox, QGridLayout, QToolBar, QSizePolicy, QTableView, QListWidget
from logins_db import create_table
from logins_db import submit
from logins_db import is_login_exists
from AddAppointmentWindow import AddAppointmentWindow
from appointments_db import get_appointments
from AppointmentDetailsWindow import AppointmentDetailsWindow


class CalendarWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.initUI()
        self.parent = parent
        self.show_all_appointments()



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

        self.log_out_button = QPushButton("Back", self)
        self.toolbar.addWidget(self.log_out_button)
        self.log_out_button.clicked.connect(self.log_out)

        # create a layout for the date widget
        self.date_layout = QHBoxLayout()

        # create two buttons to add to the date layout
        self.left_button = QPushButton("<", self)
        self.right_button = QPushButton(">", self)

        # create a label to display the current date
        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # add the label and buttons to the date layout
        self.date_layout.addWidget(self.left_button)
        self.date_layout.addWidget(self.date_label)
        self.date_layout.addWidget(self.right_button)

        self.today_list_appointments = QListWidget()

        self.label_appointments = QLabel("Appointments for today:")
        self.label_appointments.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #add button for adding new appointment
        self.add_appointment_button = QPushButton("Add appointment", self)
        self.add_appointment_button.clicked.connect(self.add_appointment)


        # set the layout for the main window
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.add_appointment_button)
     #   self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.date_layout)
     #   self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.label_appointments)
        self.main_layout.addWidget(self.today_list_appointments)

        # set the current date
        self.current_date = QDate.currentDate()
        self.date_label.setText(self.current_date.toString("MMM dd"))

        # connect the button signals to their respective slots
        self.left_button.clicked.connect(self.prev_date)
        self.right_button.clicked.connect(self.next_date)

        self.today_list_appointments.itemClicked.connect(self.appointment_details)

    def log_out(self):
        self.parent.show()
        self.close()

    def update_date_label(self):
        self.date_label.setText(self.current_date.toString("MMM dd"))

    def prev_date(self):
        self.current_date = self.current_date.addDays(-1)
        self.update_date_label()
        self.refresh_all_appointments()

    def next_date(self):
        self.current_date = self.current_date.addDays(1)
        self.update_date_label()
        self.refresh_all_appointments()

    def add_appointment(self):
        self.add_appointment_window = AddAppointmentWindow(self)
        self.add_appointment_window.show()
        self.hide()

    def show_all_appointments(self):

        appointments = get_appointments(self.current_date.toString("yyyy-MM-dd"))
        for app in appointments:
            name, surname, time_ = app[1], app[2], app[4]
            self.today_list_appointments.addItem(f'{time_} {name} {surname}')


    def refresh_all_appointments(self):
        self.today_list_appointments.clear()
        self.show_all_appointments()

    def appointment_details(self):
        selected_item = self.today_list_appointments.currentItem()
        if selected_item is not None:
            time_, name, surname = selected_item.text().split()

            self.appointment_detail_window = AppointmentDetailsWindow(self, name, surname)
            self.appointment_detail_window.show()
