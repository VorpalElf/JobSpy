# JobSpy

JobSpy is a Python-based tool designed to help users collect, analyze, and manage job listings efficiently. It supports proxy management for scraping, provides CSV exports, and includes utilities for testing proxies.

## Features
- Scrape and store job listings in CSV format
- Manage and test proxy lists for reliable scraping
- Export jobs with or without numbering
- Simple command-line interface

## File Descriptions
- `job.py`: Main script for scraping and managing job listings.
- `jobs.csv`: Output file containing scraped job data.
- `jobs_numbered.csv`: Output file with numbered job entries.
- `proxies_list.txt`: List of proxies to be used for scraping.
- `proxies_test.py`: Script to test the validity of proxies.
- `working_proxies.txt`: List of proxies that have been verified as working.

## Getting Started
1. **Clone the repository**
   ```sh
   git clone <repository-url>
   cd JobSpy
   ```
2. **Install dependencies**
   Ensure you have Python 3.10+ installed. Install any required packages (if applicable):
   ```sh
   pip install -r requirements.txt
   ```
   *(If no requirements.txt is present, install any needed packages manually.)*
3. **Prepare proxy list**
   - Add your proxies to `proxies_list.txt`, one per line.
4. **Test proxies**
   ```sh
   python proxies_test.py
   ```
   - Working proxies will be saved to `working_proxies.txt`.
5. **Run the job scraper**
   ```sh
   python job.py
   ```
   - Output will be saved to `jobs.csv` and/or `jobs_numbered.csv`.

## Customisation
- You can change parameters in Line 8~16 to suit your need.
- Search Term: job title you want to search
- Location: Work location
- Results_wanted: Number of results returned
- proxies: your proxies list

## Notes
- Make sure to comply with the terms of service of any job site you scrape.
- Use proxies responsibly to avoid being blocked.

## License
This project is for educational purposes. Please check the repository for license details.
