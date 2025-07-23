import sqlite3

# Create a new SQLite database file
conn = sqlite3.connect("data_store.db")
cursor = conn.cursor()

# Create a table with category, value, timestamp
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        value REAL NOT NULL,
        timestamp TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
print("Database and the table created successfully.")
