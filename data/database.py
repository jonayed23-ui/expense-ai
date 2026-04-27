import sqlite3

conn = sqlite3.connect("expense.db")
cursor = conn.cursor()

def init_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        type TEXT,
        date TEXT)''')
    conn.commit()

def add_transaction(amount, category, ttype, date):
    cursor.execute("INSERT INTO transactions (amount, category, type, date) VALUES (?,?,?,?)",
                   (amount, category, ttype, date))
    conn.commit()

def get_all():
    cursor.execute("SELECT * FROM transactions")
    return cursor.fetchall()
