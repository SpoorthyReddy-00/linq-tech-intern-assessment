# linq-tech-intern-assessment
Technology Intern Take-Home Assessment for Linq

This project demonstrates a basic data pipeline and visualization workflow using **Python**, **SQLite**, **Plotly**, and **Docker**.

---

##  Project Overview

The project simulates a real-world data scenario where:
- A datastore is set up
- Mock data is generated and inserted
- Data is visualized in a line chart grouped by category
- (Bonus) The entire setup is containerized using Docker for easy portability

---

##  Files Included

| File | Description |
|------|-------------|
| `datastore_setup.py` | Creates an SQLite database and a table |
| `data_ingest.py` | Generates 100 records with realistic categories and inserts into DB |
| `visualization.py` | Plots a time-series line chart from the stored data |
| `dashboard.png` | Saved output image of the chart |
| `datastore-setup.md` | Explains the choice of SQLite |
| `data-ingestion.md` | Explains how mock data is generated and transformed |
| `visualization.md` | Describes the visualization process and output |
| `Dockerfile` | Defines a Python environment with Chrome for Plotly image export |
| `docker-compose.yml` | Orchestrates the container build and runtime environment |
| `Docker.md` |  Explains how to use Docker with this project |

---

##  Categories Used

Mock data is generated using realistic, high-impact categories:

- E-Commerce  
- Healthcare  
- Social Media  
- Cryptocurrency  
- Remote Work  

These categories reflect commonly analyzed sectors in today’s tech landscape.

---

##  How to Run

###  Run Locally (Without Docker)

1. Make sure Python 3 is installed
2. Clone the repo
3. Install dependencies:
4. Run:

```bash
pip install pandas plotly kaleido
```

```bash
python datastore_setup.py
python data_ingest.py
python visualization.py
```
###  Run (With Docker)

```bash
docker-compose up --build -d
docker-compose exec app bash
```
Run all the below python scripts inside the container

```bash
python datastore_setup.py
python data_ingest.py
python visualization.py
```

