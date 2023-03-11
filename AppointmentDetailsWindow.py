import sys
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QLineEdit, \
    QHBoxLayout, QMessageBox, QGridLayout, QToolBar, QSizePolicy, QTableView, QListWidget
from AddDescriptionWindow import AddDescriptionWindow
from DiagnosticDetailsWindow import DiagnosticDetailsWindow
from clients_db import get_description
from clients_db import get_diagnostic
from clients_db import add_diagnostic
from clients_db import get_file_path
from detect import detect



class AppointmentDetailsWindow(QWidget):
    def __init__(self, parent, name, surname):
        super().__init__()
        self.parent = parent
        self.name_ = name
        self.surname_ = surname
        self.initUI()

        self.show_description()

    def initUI(self):
        self.setWindowTitle('Menu')
        self.setGeometry(300, 300, 500, 520)

        # Set the background color to white
        self.setStyleSheet('background-color: white;')

        # Create a toolbar
        self.toolbar = QToolBar(self)
        self.toolbar.setStyleSheet("QToolBar {background-color: #F5F5F5; border: none;}")
        self.toolbar.setIconSize(self.toolbar.iconSize() * 1.5)

        self.log_out_button = QPushButton("Back", self)
        self.toolbar.addWidget(self.log_out_button)
        self.log_out_button.clicked.connect(self.log_out)

        # Create a widget to hold the appointments UI
        self.appointments_widget = QWidget(self)
        self.appointments_widget.setStyleSheet('background-color: white;')

        # Create a label and diagnostic button
        self.appointment_label = QLabel(self.appointments_widget)
        self.appointment_label.setText('Appointments: ' + str(self.name_) + ' ' + str(self.surname_))
        self.appointment_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        is_diagnostic = get_diagnostic(self.name_, self.surname_)

        if is_diagnostic and is_diagnostic[0][0] == 0:
          self.diagnostic_button = QPushButton('Diagnostic', self.appointments_widget)
          self.diagnostic_button.clicked.connect(self.diagnostic)
        else:
          self.show_diagnostic_button = QPushButton('Show Diagnostic', self.appointments_widget)
          self.show_diagnostic_button.clicked.connect(self.show_diagnostic)


        # Create a button to add a new description
        self.add_description_button = QPushButton('Add new description', self.appointments_widget)
        self.add_description_button.clicked.connect(self.add_new_description)


        # Create a list widget to display appointments
        self.appointments_list_widget = QListWidget(self.appointments_widget)

        # Create a layout to hold the appointments UI
        self.appointments_layout = QVBoxLayout(self.appointments_widget)
        self.appointments_layout.addWidget(self.appointment_label)
        if is_diagnostic and is_diagnostic[0][0] == 0:
            self.appointments_layout.addWidget(self.diagnostic_button)
        else:
            self.appointments_layout.addWidget(self.show_diagnostic_button)
        self.appointments_layout.addWidget(self.add_description_button)
        self.appointments_layout.addWidget(self.appointments_list_widget)

        # Set the appointments widget to be hidden by default
        self.appointments_widget.setVisible(True)

        # Add the toolbar and appointments widget to the main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.appointments_widget)

        # Connect the appointments button to show the appointments UI
        # self.appointments_button.clicked.connect(self.show_appointments)

        self.appointments_list_widget.itemClicked.connect(self.show_appointment_details)

    def log_out(self):
        self.parent.show()
        self.close()

    def show_appointments(self):
        # Show the appointments UI when the appointments button is clicked
         self.appointments_widget.setVisible(True)


    def diagnostic(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Video files (*.mp4 *.avi)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            # Get the selected file path
            file_path = file_dialog.selectedFiles()[0]
            detect(file_path, self.name_, self.surname_)
            add_diagnostic(1, self.name_, self.surname_)




    def add_new_description(self):
        self.add_description_window = AddDescriptionWindow(self, self.name_, self.surname_)
        self.add_description_window.show()


    def show_description(self):
        descr_ = get_description(self.name_, self.surname_)
        if descr_:
            description_str = str(descr_[0][0])
            self.appointments_list_widget.addItem(description_str)

    def show_appointment_details(self):
        pass

    def refresh_description(self):

        self.appointments_list_widget.clear()
        self.show_description()

    def show_diagnostic(self):
        file_path_ = get_file_path(self.name_, self.surname_)
        file_path_str = str(file_path_[0][0])
        self.diagnostic_details_window = DiagnosticDetailsWindow(file_path_str)
        self.diagnostic_details_window.show()



