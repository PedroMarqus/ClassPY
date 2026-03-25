import sqlite3

DB_PATH = "data/database.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # permite acessar por nome
    return conn