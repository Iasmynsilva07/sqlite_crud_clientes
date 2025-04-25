import sqlite3
from pathlib import Path
import os

ROOT_DIR = Path(__file__).parent.parent
DB_DIR = ROOT_DIR / 'data'
DB_FILE = ROOT_DIR / 'data' / 'db.sqlite3'
TABLE_NAME = 'customers'

def connect():
    os.makedirs(DB_DIR, exist_ok=True)
    connection = sqlite3.connect(DB_FILE)
    return connection

def create_table():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            f'''CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                weight REAL NOT NULL
            )'''
        )
        conn.commit()
