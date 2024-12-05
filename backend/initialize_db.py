import sqlite3

def initialize_database():
    """
    Initializes the SQLite database and creates the 'logs' table.
    """
    conn = sqlite3.connect('log190.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            log_level TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.close()

if __name__ == '__main__':
    initialize_database()
