import sqlite3

def delete_schema():
    conn = sqlite3.connect('company_data.db')
    cursor = conn.cursor()

    # Drop tables if they exist
    cursor.execute("DROP TABLE IF EXISTS enriched_companies")
    cursor.execute("DROP TABLE IF EXISTS companies")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    delete_schema()
