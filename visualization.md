# Visualization

## Overview

This script (`visualization.py`) reads data from the SQLite database (`data_store.db`) and creates an interactive line chart to display value trends over time, grouped by category.

The chart helps visualize how different categories perform over the past month, highlighting temporal changes in the mock data.

## Technologies Used

- **Pandas:** for loading and manipulating data  
- **Plotly Express:** for creating interactive, user-friendly visualizations  
- **Kaleido:** to export the Plotly chart as a static PNG image  

## How It Works

1. Connects to the SQLite database and retrieves all records from the `data_entries` table.  
2. Converts timestamps to datetime objects for accurate sorting and plotting.  
3. Sorts the data by timestamp to ensure the line chart flows correctly over time.  
4. Plots a multi-line chart with categories as distinct colors, showing the `value` trend for each over time.  
5. Saves the chart as `dashboard.png` and opens an interactive version in your web browser.

## Setup & Run Instructions
In the terminal:
Before running, install dependencies:

```bash

pip install pandas plotly kaleido 
```

```bash
python visualization.py
```