# Setup SQLite database connection
# Create connection function
# Ensure connection reuse and proper closing
# Define functions to execute queries and fetch results
# Handle database initialization and migrations if needed
# Example functions:
# - connect_db() → returns connection
# - execute_query(query, params) → executes query with parameters
# - fetch_one(query, params) → returns single result
# - fetch_all(query, params) → returns list of results

import sqlite3
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'database.db')

def connect_db():
    return sqlite3.connect(DATABASE_PATH)

def execute_query(query, params=None):
    conn = connect_db()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    conn.close()

def fetch_one(query, params=None):
    conn = connect_db()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

def fetch_all(query, params=None):
    conn = connect_db()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def execute_sql_file(file_path):
    """Execute SQL commands from a file"""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        cursor.executescript(sql_script)
        conn.commit()
        print("SQL file executed successfully")
    except Exception as e:
        print(f"Error executing SQL file: {e}")
        conn.rollback()
    finally:
        conn.close()

def init_db():
    """Initialize database by executing the schema SQL file"""
    sql_file_path = os.path.join(os.path.dirname(__file__), 'carrer.sql')
    if os.path.exists(sql_file_path):
        execute_sql_file(sql_file_path)
    else:
        print("Warning: carrer.sql file not found. Using fallback table creation.")
        # Fallback to hardcoded tables if SQL file is missing
        execute_query('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                skills TEXT,
                interests TEXT,
                education TEXT,
                progress TEXT
            )
        ''')
        execute_query('''
            CREATE TABLE IF NOT EXISTS progress (
                user_id INTEGER PRIMARY KEY,
                completed_skills TEXT,
                current_step TEXT,
                progress_percentage REAL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        execute_query('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                rating INTEGER,
                comments TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')      
