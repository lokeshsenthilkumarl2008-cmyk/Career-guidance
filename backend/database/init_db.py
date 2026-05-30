# Initialize the database
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from database.db import init_db

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")
