import argparse
import csv
import sys
from pathlib import Path
import pandas as pd
from jobspy import scrape_jobs


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        prog="jobspy-run",
        description="Run job searches via the jobspy library with proxy rotation and CSV export",
    )
    p.add_argument("--search", "--search-term", dest="search_term", required=True, help="Search term / job title")
    p.add_argument("--location", required=True, help="Job location (city, country, etc.)")
    p.add_argument("--sites", nargs="*", default=["linkedin"], help="Sites to query (default: linkedin)")
    p.add_argument("--results", type=int, default=100, help="Number of results wanted (default: 100)")
    p.add_argument("--proxies", type=Path, default=Path("Proxies/working_proxies.txt"), help="Path to working proxies file")
    p.add_argument("--out", type=Path, default=Path("jobs.csv"), help="Output CSV path (default: jobs.csv)")
    p.add_argument("--no-description", action="store_true", help="Disable fetching description text (LinkedIn)")
    p.add_argument("--numbered", action="store_true", help="Also write numbered CSV (jobs_numbered.csv)")
    p.add_argument("--drop-id", action="store_true", help="Drop original id column in numbered CSV")
    return p.parse_args(argv)


def load_proxies(path: Path):
    if not path.exists():
        print(f"[WARN] Proxy file not found: {path} (continuing without proxies)")
        return []
    with path.open() as f:
        return [ln.strip() for ln in f if ln.strip()]


def run(search_term: str, location: str, sites, results: int, proxies_file: Path, out: Path, fetch_description: bool, make_numbered: bool, drop_id: bool):
    proxies = load_proxies(proxies_file)
    jobs = scrape_jobs(
        site_name=sites,
        search_term=search_term,
        location=location,
        results_wanted=results,
        linkedin_fetch_description=fetch_description,
        proxies=proxies if proxies else None,
        rotate_proxies=bool(proxies),
    )
    print(f"Found {len(jobs)} jobs from {sites}")
    jobs.to_csv(out, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
    if make_numbered:
        df = jobs.copy()
        df.insert(0, "job_number", range(1, len(df) + 1))
        if drop_id and "id" in df.columns:
            df = df.drop(columns=["id"])
        numbered = out.parent / (out.stem + "_numbered" + out.suffix)
        df.to_csv(numbered, index=False)
        print(f"Wrote numbered CSV: {numbered}")
    print(f"Wrote jobs CSV: {out}")


def main(argv=None):
    args = parse_args(argv)
    run(
        search_term=args.search_term,
        location=args.location,
        sites=args.sites,
        results=args.results,
        proxies_file=args.proxies,
        out=args.out,
        fetch_description=not args.no_description,
        make_numbered=args.numbered,
        drop_id=args.drop_id,
    )
if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
