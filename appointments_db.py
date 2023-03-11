import sqlite3
import bcrypt

def create_table():
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             cl_name TEXT NOT NULL,
                             cl_surname TEXT NOT NULL,
                             appointment_date TEXT NOT NULL,
                             appointment_time TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def submit(name, surname, ap_date, ap_time):
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()

    # Insert the login and password into the database
    cursor.execute("INSERT INTO appointments (cl_name, cl_surname, appointment_date, appointment_time)"
                   " VALUES (?, ?, ?, ?)", (name, surname, ap_date, ap_time))
    conn.commit()
    conn.close()

def get_appointments(cur_date):
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM appointments WHERE appointment_date = ? "
                   "ORDER BY appointment_time", (cur_date, ))
    rows = cursor.fetchall()
    conn.close()
    return rows





