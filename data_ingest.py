import sqlite3
import random
from datetime import datetime, timedelta

# Predefined categories to simulate real data
categories = ["E-Commerce", "Healthcare", "Social Media", "Cryptocurrency", "Remote Work"]

# Connect to the existing SQLite database
conn = sqlite3.connect("data_store.db")
cursor = conn.cursor()

# Insert 100 mock records into the data_entries table
for i in range(100):
    category = random.choice(categories)
    value = round(random.uniform(20, 500), 2)

    # Generate a timestamp within the last 30 days
    days_ago = random.randint(0, 30)
    timestamp = (datetime.now() - timedelta(days=days_ago)).isoformat()

    # Apply a simple transformation (10% increase, e.g., tax or inflation)
    adjusted_value = round(value * 1.1, 2)

    # Insert the record into the table
    cursor.execute(
        "INSERT INTO data_entries (category, value, timestamp) VALUES (?, ?, ?)",
        (category, adjusted_value, timestamp)
    )

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Done: 100 mock records inserted into the database.")
