import sqlite3
import bcrypt

def create_table():
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS login
                            (id INTEGER PRIMARY KEY,
                             username TEXT NOT NULL,
                             password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def submit(login, password):
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()

    username = login
    password = password

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Insert the login and password into the database
    cursor.execute("INSERT INTO login (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

def is_login_exists(login):
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM login WHERE username=?", (login,))
    data = cursor.fetchall()
    conn.close()

    if data:
        return True
    else:
        return False



def is_user_exists(login, password):
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM login WHERE username = ?", (login,))
    result = cursor.fetchone()
    conn.close()

    if result is not None:
        stored_hash = result[0]
        # Hash the entered password with the same salt used for the stored hash
        entered_hash = bcrypt.hashpw(password.encode('utf-8'), stored_hash)

        if entered_hash == stored_hash:
            return True
        else:
            return False
    else:
        return False;

