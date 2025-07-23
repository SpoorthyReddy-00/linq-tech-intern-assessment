# linq-tech-intern-assessment
Technology Intern Take-Home Assessment for Linq
#  Technology Intern Take-Home Assessment

This project demonstrates a simple data pipeline using Python, SQLite, and Plotly.

##  What It Does

- Sets up a database
- Generates mock data with real-world categories
- Visualizes the data in a time-based line chart

##  Project Structure

| File | Description |
|------|-------------|
| `datastore_setup.py` | Creates the SQLite database and table |
| `data_ingest.py` | Generates and inserts 100 fake records |
| `visualization.py` | Creates a chart from the data |
| `dashboard.png` | Screenshot of the generated graph |
| `datastore-setup.md` | Why SQLite was chosen |
| `data-ingestion.md` | How mock data is generated and transformed |
| `visualization.md` | How the chart was built and how to run it |

##  How to Run

1. Clone the repo
2. Run:

```bash
python datastore_setup.py
python data_ingest.py
python visualization.py
