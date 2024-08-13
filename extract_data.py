import sqlite3

def extract_data():
    conn = sqlite3.connect('company_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT company_id, company_linkedin_url FROM companies")
    company_data = cursor.fetchall()

    conn.close()
    return company_data

if __name__ == '__main__':
    data = extract_data()
    for row in data:
        print(row)
