import sqlite3
import os

def connect_to_database():
    # Connecting to SQLite database
    db_file = os.path.join(os.path.dirname(__file__),'sqlite3', 'crypto-db.db')
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    # Create a table to store cryptocurrency data if it doesn't exist
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cryptocurrency_data (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        symbol TEXT,
                        price REAL,
                        normalized_price REAL
                    )''')
    conn.commit()

def insert_data(conn, transformed_data):
    # Insert data into the cryptocurrency_data table
    cursor = conn.cursor()
    for item in transformed_data:
        cursor.execute('''INSERT INTO cryptocurrency_data (name, symbol, price, normalized_price) 
                          VALUES (?, ?, ?, ?)''', (item['name'], item['symbol'], item['price'], item['normalized_price']))
    conn.commit()

def close_connection(conn):
    # Close the database connection
    conn.close()
