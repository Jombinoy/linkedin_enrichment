import sqlite3

def setup_database():
    conn = sqlite3.connect('company_data.db')
    cursor = conn.cursor()

    # Create companies table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        company_id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_linkedin_url TEXT UNIQUE
    )
    ''')

    # Create enriched_companies table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS enriched_companies (
        company_id INTEGER PRIMARY KEY,
        company_name TEXT,
        industry TEXT,
        website_url TEXT,
        FOREIGN KEY (company_id) REFERENCES companies (company_id)
    )
    ''')

    # Insert sample data
    cursor.executemany('''
    INSERT OR IGNORE INTO companies (company_linkedin_url) VALUES (?)
    ''', [
        ('https://www.linkedin.com/company/microsoft',),
        ('https://www.linkedin.com/company/facebook',),
        ('https://www.linkedin.com/company/adobe',),
    ])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
