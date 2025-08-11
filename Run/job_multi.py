import csv
from jobspy import scrape_jobs
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

with open("Proxies/working_proxies.txt") as f:
    proxy_list = [line.strip() for line in f if line.strip()]

def fetch_jobs(chunk_size, proxy_sublist):
    return scrape_jobs(
        site_name=["linkedin"],
        search_term="Data Analyst",
        location="United Kingdom",
        results_wanted=chunk_size,
        linkedin_fetch_description=True,
        proxies=proxy_sublist,
        rotate_proxies=True
    )

total_results = 300
num_threads = 10
chunk_size = total_results // num_threads
jobs_list = []

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = []
    for i in range(num_threads):
        futures.append(executor.submit(fetch_jobs, chunk_size, proxy_list))
    for future in as_completed(futures):
        jobs = future.result()
        jobs_list.append(jobs)

if jobs_list:
    all_jobs = pd.concat(jobs_list, ignore_index=True)
    print(f"Found {len(all_jobs)} jobs")
    print(all_jobs.head())
    all_jobs.to_csv("jobs_2.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)

    # Read the CSV
    df = pd.read_csv("jobs_2.csv")

    # Add a new column 'job_number' with values 1 to len(df)
    df.insert(0, "job_number", range(1, len(df) + 1))

    # Optionally, drop the original 'id' column
    if "id" in df.columns:
        df = df.drop(columns=["id"])

    # Save to a new CSV
    df.to_csv("jobs_2_num.csv", index=False)
else:
    print("No jobs found.")