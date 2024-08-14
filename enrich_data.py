import http.client
import json
import sqlite3

API_HOST = 'linkedin-bulk-data-scraper.p.rapidapi.com'
API_KEY = '586d0454f3msh326cc876bfd964ep1ef269jsn2ad4b1013205'  # Replace with your actual API key

def enrich_data():
    conn = sqlite3.connect('company_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT company_id, company_linkedin_url FROM companies")
    company_data = cursor.fetchall()

    for company_id, linkedin_url in company_data:
        conn_http = http.client.HTTPSConnection(API_HOST)

        payload = json.dumps({"link": linkedin_url})
        headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': API_HOST,
            'Content-Type': 'application/json'
        }

        conn_http.request("POST", "/company", payload, headers)

        response = conn_http.getresponse()
        response_data = response.read().decode("utf-8")

        print("Status Code:", response.status)
        print("Response Headers:", response.headers)
        print("Response Text:", response_data[:500])  # Print first 500 chars for debugging

        if response.status == 200:
            try:
                enriched_data = json.loads(response_data)
                if enriched_data['success']:
                    data = enriched_data['data']
                    
                    # Filter out unwanted fields
                    filtered_data = {k: v for k, v in data.items() if not any(sub in k for sub in ['affiliatedOrganizations', 'locations', 'similarOrganizations'])}
                    
                    # Extract relevant fields from 'filtered_data'
                    company_name = filtered_data.get('companyName', '')
                    industry = filtered_data.get('industry', '')
                    website_url = filtered_data.get('websiteUrl', '')

                    # Insert or update the enriched data in the database
                    cursor.execute('''
                    INSERT OR REPLACE INTO enriched_companies (company_id, company_name, industry, website_url)
                    VALUES (?, ?, ?, ?)
                    ''', (company_id, company_name, industry, website_url))
                else:
                    print("API response success is False:", enriched_data)
            except ValueError as e:
                print("Error decoding JSON:", e)
        else:
            print("API request failed. Status code:", response.status)

        conn_http.close()

    conn.commit()
    conn.close()

if __name__ == '__main__':
    enrich_data()
