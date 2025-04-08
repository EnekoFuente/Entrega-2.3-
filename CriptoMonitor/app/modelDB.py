import sqlite3

DB_PATH = 'crypto.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_price(name, value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO prices (name, value) VALUES (?, ?)", (name, value))
    conn.commit()
    conn.close()

def get_all_prices():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, value FROM prices")
    prices = cursor.fetchall()
    conn.close()
    return [{'name': name, 'value': value} for name, value in prices]