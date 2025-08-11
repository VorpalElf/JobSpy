# JobSpy (Runner / CLI)

JobSpy Runner is a lightweight command‑line wrapper around the upstream `jobspy` library that lets you quickly scrape job listings (e.g. LinkedIn) with proxy rotation and export them to CSV (optionally with numbered rows).

> NOTE: This repository adds a CLI helper package named `jobspy-runner` to avoid clashing with the existing `jobspy` dependency on PyPI.

## Features
* Proxy list + rotation support
* CSV export + optional numbered CSV
* Simple CLI: `jobspy-run --search "Data Analyst" --location "United Kingdom"`

## Installation

### From PyPI (after you publish)
```bash
pip install jobspy-runner
```

### From source (this repository)
```bash
git clone https://github.com/VorpalElf/JobSpy.git
cd JobSpy
pip install .
```

### Dev (editable) install
```bash
pip install -e .
```

### Using pipx
```bash
pipx install jobspy-runner
```

## Quick Start
```bash
jobspy-run \
   --search "Data Analyst" \
   --location "United Kingdom" \
   --results 200 \
   --proxies Proxies/working_proxies.txt \
   --numbered --drop-id
```
Outputs:
* `jobs.csv`
* `jobs_numbered.csv` (if `--numbered`)

## CLI Options
| Option | Description |
|--------|-------------|
| `--search` | Job title / keywords (required) |
| `--location` | Location text (required) |
| `--sites` | Space separated site names (default: linkedin) |
| `--results` | Number of results wanted (default 100) |
| `--proxies` | Path to working proxies file (default Proxies/working_proxies.txt) |
| `--no-description` | Skip fetching description text |
| `--numbered` | Emit a second numbered CSV |
| `--drop-id` | Drop the original id column in numbered CSV |
| `--out` | Output CSV path (default jobs.csv) |

## Preparing & Testing Proxies
1. Put candidate proxies (HTTPS, low latency) in `Proxies/proxies_list.txt`.
2. Test them:
```bash
python Proxies/proxies_test.py
```
3. Use generated `Proxies/working_proxies.txt` for scraping.

## Library Usage Example
```python
from jobspy import scrape_jobs
jobs = scrape_jobs(site_name=["linkedin"], search_term="Data Analyst", location="United Kingdom", results_wanted=50, linkedin_fetch_description=True)
jobs.to_csv("jobs.csv", index=False)
```

## Packaging & Publishing
Build and upload wheels instead of providing a video demo:
```bash
python -m pip install --upgrade build twine
python -m build
python -m twine upload dist/*  # or --repository testpypi first
```
After publishing, users can run:
```bash
pip install jobspy-runner
jobspy-run --search "Data Analyst" --location "United Kingdom"
```

## Standalone Executable (Alternative)
Create a binary for a GitHub Release:
```bash
pip install pyinstaller
pyinstaller -F -n jobspy-runner jobspy_runner/cli.py
```
Executable appears in `dist/`.

## Project Structure
```
jobspy_runner/        # CLI package
   cli.py              # Entry point
job.py                # Original script
job_multi.py          # Multithread example
Proxies/              # Proxy list + tester
```

## Notes
* Respect site Terms of Service.
* Use responsible scraping intervals.

## License
Add a LICENSE file and update `pyproject.toml` before publishing.
