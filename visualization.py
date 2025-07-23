import sqlite3
import pandas as pd
import plotly.express as px

connection = sqlite3.connect("data_store.db")

query = "SELECT category, value, timestamp FROM data_entries"
df = pd.read_sql_query(query, connection)

connection.close()

df['timestamp'] = pd.to_datetime(df['timestamp'])

df = df.sort_values('timestamp')

# Create a line chart showing value over time, grouped by category
fig = px.line(
    df,
    x='timestamp',
    y='value',
    color='category',
    title='Value Trend Over Time by Category'
)

fig.write_image("dashboard.png")


fig.show()

print("Visualization created and saved as dashboard.png")
