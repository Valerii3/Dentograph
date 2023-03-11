import sys
import sqlite3


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QLineEdit, \
    QHBoxLayout, QMessageBox, QGridLayout, QToolBar, QSizePolicy, QTableView, QListWidget
from logins_db import create_table
from logins_db import submit
from logins_db import is_login_exists
from patients import PatientsWindow
from CalendarWindow import CalendarWindow
from DiagnosticsWindow import DiagnosticsWindow


class MenuWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.initUI()
        self.parent = parent


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
        self.patients_button.clicked.connect(self.show_patients)

        self.calendar_button = QPushButton("Calendar", self)
        self.toolbar.addWidget(self.calendar_button)
        self.calendar_button.clicked.connect(self.show_calendar)

        self.diagnostics_button = QPushButton("Diagnostics", self)
        self.toolbar.addWidget(self.diagnostics_button)
        self.diagnostics_button.clicked.connect(self.show_diagnostics)

        self.log_out_button = QPushButton("Log out", self)
        self.toolbar.addWidget(self.log_out_button)
        self.log_out_button.clicked.connect(self.log_out)





    def log_out(self):
        self.parent.show()
        self.close()

    def show_patients(self):
        self.patients_window = PatientsWindow(self.parent)
        self.patients_window.show()
        self.close()

    def show_calendar(self):
        self.calendar_window = CalendarWindow(self.parent)
        self.calendar_window.show()
        self.close()

    def show_diagnostics(self):
        self.diagnostics_window = DiagnosticsWindow(self.parent)
        self.diagnostics_window.show()
        self.close()



