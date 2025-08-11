
# job-check (CLI)

`job-check` is a CLI tool for scraping job listings (e.g. LinkedIn) using the `jobspy` library, with proxy rotation and CSV export. Now available as a PyPI package.

## Features
- Proxy rotation
- CSV export (optionally numbered)
- Simple CLI interface


## Installation
Install the package directly from PyPI:
```bash
pip install job-check
pip install -U python-jobspy
```


## Usage

After installation, you can run the CLI tool from anywhere:
```bash
job-check --search "Software Engineer" --location "New York"
```

### Optional Arguments

- `--sites`, `-s` linkedin indeed (default: linkedin)
- `--results`, `-r` 20 (default: 10)
- `--proxies`, `-p` <your_proxies_file> (default: Proxies/proxies_list.txt)
- `--numbered`, `-n` (write numbered CSV)
- `--out`, `-o` jobs.csv (output path)
- `--description`, `-d` (fetch description text; no description by default)

See all options:
```bash
job-check --help
```


## Proxy Setup
1. Add proxies to `Proxies/proxies_list.txt` (one per line).
2. Test proxies:
   ```bash
   python Proxies/proxies_test.py
   ```
3. Use `Proxies/working_proxies.txt` for scraping.


## Project Structure
```
jobspy/cli.py             # CLI entry point
Proxies/                  # Proxy list & tester
requirements.txt          # Python dependencies
setup.py                  # Project metadata
```


## Notes
- Respect site Terms of Service.
- Use responsible scraping intervals.


## License
See LICENSE file.
