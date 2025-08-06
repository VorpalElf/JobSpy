import csv
from jobspy import scrape_jobs
import pandas as pd

with open("Proxies/working_proxies.txt") as f:
    proxy_list = [line.strip() for line in f if line.strip()]

jobs = scrape_jobs(
    site_name=["linkedin"], # "glassdoor", "bayt", "naukri", "bdjobs"
    search_term="Data Analyst",
    location="United Kingdom",
    results_wanted=10,
    linkedin_fetch_description=True,
    proxies=proxy_list,
    rotate_proxies=True
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel

# Read the CSV
df = pd.read_csv("jobs.csv")

# Add a new column 'job_number' with values 1 to len(df)
df.insert(0, "job_number", range(1, len(df) + 1))

# Optionally, drop the original 'id' column
df = df.drop(columns=["id"])

# Save to a new CSV
df.to_csv("jobs_numbered.csv", index=False)