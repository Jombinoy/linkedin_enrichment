# db_maintenance.py

import sqlite3

def clear_table(table_name):
    conn = sqlite3.connect('company_data.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name}")
    conn.commit()
    conn.close()

def clean_database():
    clear_table('companies')
    clear_table('enriched_companies')

if __name__ == '__main__':
    clean_database()
