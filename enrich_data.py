import requests
import sqlite3

API_URL = 'https://linkedin-bulk-data-scraper.p.rapidapi.com/company'
API_KEY = 'baeddbbaccmsh6819bc6f1419165p140dddjsndd18de2792dd'  # Replace with your actual API key

def enrich_data():
    conn = sqlite3.connect('company_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT company_id, company_linkedin_url FROM companies")
    company_data = cursor.fetchall()

    headers = {
        'X-RapidAPI-Key': API_KEY,
        'X-RapidAPI-Host': 'linkedin-bulk-data-scraper.p.rapidapi.com',
        'Content-Type': 'application/json'
    }

    for company_id, linkedin_url in company_data:
        response = requests.post(API_URL, headers=headers, json={"link": linkedin_url})

        print("Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("Response Text:", response.text[:500])  # Print first 500 chars for debugging

        if response.status_code == 200:
            try:
                enriched_data = response.json()
                if enriched_data['success']:
                    data = enriched_data['data']
                    # Extract relevant fields from 'data'
                    company_name = data.get('companyName', '')
                    locations = data.get('locations', [])
                    
                    # Process locations or other nested data as needed
                    location_info = ', '.join([f"{loc['city']}, {loc['country']}" for loc in locations])

                    # Insert or update the enriched data
                    cursor.execute('''
                    INSERT OR REPLACE INTO enriched_companies (company_id, enriched_field_1, enriched_field_2)
                    VALUES (?, ?, ?)
                    ''', (company_id, company_name, location_info))
                else:
                    print("API response success is False:", enriched_data)
            except ValueError as e:
                print("Error decoding JSON:", e)
        else:
            print("API request failed. Status code:", response.status_code)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    enrich_data()
