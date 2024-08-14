# LinkedIn Data Enrichment Project

## Overview

This project interacts with a database and an external API to enrich company data. It includes scripts to set up the database, extract data, and enrich it using the LinkedIn Bulk Data Scraper API.

## Features

- **Database Setup**: Creates necessary tables and inserts sample data.
- **Data Extraction**: Fetches company data from the database.
- **Data Enrichment**: Enriches company data using an external API and updates the database.

## Prerequisites

- Python 3.x
- SQLite3 (comes with Python standard library)
- API Key for LinkedIn Bulk Data Scraper API (available from RapidAPI)

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/your-repo.git
cd your-repo

2. Install dependencies:
This project uses only the Python standard library, so no additional packages are required.

3. Set up the database:
Run the following script to create the necessary tables and insert sample data:
python setup_database.py
4. Extract Data:
Run the extract_data.py script to fetch company data from the database:
Sample Output:
(1, 'https://www.linkedin.com/company/microsoft')
(2, 'https://www.linkedin.com/company/facebook')
(3, 'https://www.linkedin.com/company/adobe')
5. Enrich Data:
Run the enrich_data.py script to enrich company data using the LinkedIn Bulk Data Scraper API:
python enrich_data.py
Ensure you replace `API_KEY` in enrich_data.py with your actual API key.

Sample Output:
Status Code: 200
Response Headers: {'Content-Type': 'application/json', ...}
Response Text: {"success": true, "data": {"companyName": "Microsoft", "industry": "Software", "websiteUrl": "https://www.microsoft.com"}}
Status Code: 200
Response Headers: {'Content-Type': 'application/json', ...}
Response Text: {"success": true, "data": {"companyName": "Facebook", "industry": "Social Media", "websiteUrl": "https://www.facebook.com"}}
Status Code: 200
Response Headers: {'Content-Type': 'application/json', ...}
Response Text: {"success": true, "data": {"companyName": "Adobe", "industry": "Software", "websiteUrl": "https://www.adobe.com"}}
## Code Explanation

- `setup_database.py`: Sets up the SQLite database with the required tables and inserts sample data.
- `extract_data.py`: Connects to the SQLite database, extracts company data, and prints it.
- `enrich_data.py`: Connects to the LinkedIn API, enriches company data, and updates the database.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes.
4. Commit your changes: `git commit -am 'Add new feature'`
5. Push to the branch: `git push origin feature-branch`
6. Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions, please contact jombinoy24@gmail.com.