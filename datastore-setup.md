#  Datastore Setup: SQLite

## Why I Chose SQLite

I chose SQLite because it's lightweight, file-based, and easy to use for small-scale projects or prototyping. For this assessment, where all the data is local and doesn't require server hosting, SQLite is a practical and efficient choice.

It comes pre-installed with Python, so there's no need to manage external servers or dependencies. This makes the setup process simple and fast.

## Setup Details

I created a script called `datastore_setup.py` that:
- Creates a new SQLite database file (`data_store.db`)
- Adds a table called `data_entries` with the following columns:
  - `id`: a unique identifier for each entry
  - `category`: a text field for the data category
  - `value`: a number representing a value (e.g., metric, cost, etc.)
  - `timestamp`: a date and time string

You can run the script with:

```bash
python datastore_setup.py

