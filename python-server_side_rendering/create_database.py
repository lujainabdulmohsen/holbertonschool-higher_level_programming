#!/usr/bin/python3
import sqlite3


def create_database():
    with sqlite3.connect('products.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        conn.executemany(
            'INSERT OR REPLACE INTO Products VALUES (?, ?, ?, ?)',
            [
                (1, 'Laptop', 'Electronics', 799.99),
                (2, 'Coffee Mug', 'Home Goods', 15.99)
            ]
        )


if __name__ == '__main__':
    create_database()
