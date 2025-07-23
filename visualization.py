import sqlite3
import pandas as pd
import plotly.express as px

# Connect to the SQLite database
connection = sqlite3.connect("data_store.db")

# Load data into a pandas DataFrame
query = "SELECT category, value, timestamp FROM data_entries"
df = pd.read_sql_query(query, connection)

# Close the DB connection
connection.close()

# Convert timestamp column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Sort the data so the line chart flows properly
df = df.sort_values('timestamp')

# Create a line chart showing value over time, grouped by category
fig = px.line(
    df,
    x='timestamp',
    y='value',
    color='category',
    title='Value Trend Over Time by Category'
)

# Save the chart as an image
fig.write_image("dashboard.png")

# Also show the chart in browser
fig.show()

print("Visualization created and saved as dashboard.png")
