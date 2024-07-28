import sqlite3
import bcrypt

def create_table():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS clients
                            (id INTEGER PRIMARY KEY,
                             cl_name TEXT NOT NULL,
                             cl_surname TEXT NOT NULL,
                             cl_description TEXT NUll,
                             cl_diagnostic INTEGER NULL, 
                             cl_file_name TEXT NULL)''')
    conn.commit()
    conn.close()

def submit(name, surname):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    name_ = name
    surname_ = surname

    # Insert the login and password into the database
    cursor.execute("INSERT INTO clients (cl_name, cl_surname, cl_description, cl_diagnostic, cl_file_name) VALUES (?, ?, ?, ?, ?)", (name_, surname_, " ", 0, " "))
    conn.commit()
    conn.close()


def get_patients():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clients")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_description(description, name, surname):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    # Get the current description for the given client
    cursor.execute("SELECT cl_description FROM clients WHERE cl_name = ? AND cl_surname = ?", (name, surname))
    current_description = cursor.fetchone()[0]

    # Concatenate the new description with the current description
    new_description = current_description + '\n' + description

    # Update the clients table with the new description
    cursor.execute("UPDATE clients SET cl_description = ? WHERE cl_name = ? AND cl_surname = ?",
                   (new_description, name, surname))
    conn.commit()
    conn.close()

def get_description(name, surname):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute("SELECT cl_description FROM clients WHERE cl_name = ? AND cl_surname = ?", (name, surname))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_diagnostic(name, surname):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute("SELECT cl_diagnostic FROM clients WHERE cl_name = ? AND cl_surname = ?", (name, surname))
    rows = cursor.fetchall()
    conn.close()
    return rows


def add_diagnostic(diagnostic, name, surname):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE clients SET cl_diagnostic = ? WHERE cl_name = ? AND cl_surname = ?",
                   (diagnostic, name, surname))
    conn.commit()

    conn.close()

def add_file_path(file_path, name, surname):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE clients SET cl_file_name = ? WHERE cl_name = ? AND cl_surname = ?",
                   (file_path, name, surname))
    conn.commit()
    conn.close()


def get_file_path(name, surname):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute("SELECT cl_file_name FROM clients WHERE cl_name = ? AND cl_surname = ?", (name, surname))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_diagnostics():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    # select where the diagnostic is not 0
    cursor.execute("SELECT * FROM clients WHERE cl_diagnostic != 0")
    rows = cursor.fetchall()
    conn.close()
    return rows