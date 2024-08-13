import sqlite3

def setup_database():
    conn = sqlite3.connect('company_data.db')
    cursor = conn.cursor()

    # Create companies table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        company_id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_linkedin_url TEXT
    )
    ''')

    # Create enriched_companies table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS enriched_companies (
        company_id INTEGER PRIMARY KEY,
        enriched_field_1 TEXT,
        enriched_field_2 TEXT,
        FOREIGN KEY (company_id) REFERENCES companies (company_id)
    )
    ''')

    # Insert sample data
    cursor.executemany('''
    INSERT INTO companies (company_linkedin_url) VALUES (?)
    ''', [
        ('https://www.linkedin.com/company/microsoft',),
        ('https://www.linkedin.com/company/facebook',),
        ('https://www.linkedin.com/company/adobe',),
        ('https://www.linkedin.com/company/ibm',),
        ('https://www.linkedin.com/company/intel-corporation',),
        ('https://www.linkedin.com/company/amazon',)
    ])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
