import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QLineEdit, QHBoxLayout

from RegisterWindow import RegisterWindow
from LoginWindow import LoginWindow
from LoginWindow import check_login

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Autherization')
        self.setGeometry(300, 300, 500, 520)

        # Set the background color to white
        self.setStyleSheet('background-color: white;')
        # Add a login label and input box
      #  self.login_label = QLabel("Login:")
      #  self.login_input = QLineEdit()

        # Add a password label and input box
    #    self.password_label = QLabel("Password:")
    #    self.password_input = QLineEdit()
      #  self.password_input.setEchoMode(QLineEdit.Password)

        # Add a login button
        self.login_button = QPushButton('Login')
        self.login_button.setStyleSheet('background-color: green; color: white;')
        self.login_button.clicked.connect(self.handle_login)

        # Add a register button
        self.register_button = QPushButton('Register')
        self.register_button.setStyleSheet('background-color: blue; color: white;')
        self.register_button.clicked.connect(self.handle_register)

        # Add the login, password, login button, and register button widgets to a horizontal layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.login_button)
        hbox.addWidget(self.register_button)

        # Add the horizontal layout to a vertical layout
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        # Set the vertical layout as the main layout
        self.setLayout(vbox)



    def handle_register(self):
        # Create a new window for registration
        self.register_window = RegisterWindow()
        self.register_window.show()

    def handle_login(self):
        # Create a new window for registration
        self.login_window = LoginWindow(self)
        self.login_window.show()
        self.hide()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec())

