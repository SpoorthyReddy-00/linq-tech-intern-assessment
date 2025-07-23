# Data Ingestion

## Overview

This script (`data_ingest.py`) populates the SQLite database (`data_store.db`) with mock records. Each record represents a data point in one of several real-world categories.

## Categories Used

We used five realistic, industry-relevant categories:

- **E-Commerce**
- **Healthcare**
- **Social Media**
- **Cryptocurrency**
- **Remote Work**

These categories reflect common sectors in today’s data-driven world.

## How It Works

- The script generates 100 fake entries.
- For each entry:
  - A `category` is picked at random.
  - A `value` is generated between 20 and 500.
  - A `timestamp` is assigned randomly within the past 30 days.
  - A small transformation is applied: the value is increased by 10% (simulating tax, inflation, or adjusted metrics).

## Output

All 100 records are inserted into the `data_entries` table.

## Run the Script

In the terminal:

```bash
python data_ingest.py
```