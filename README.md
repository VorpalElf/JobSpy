
# JobSpy Runner (CLI)

JobSpy Runner is a CLI tool for scraping job listings (e.g. LinkedIn) using the `jobspy` library, with proxy rotation and CSV export.

## Features
- Proxy rotation
- CSV export (optionally numbered)
- Simple CLI interface

## Installation & Setup
Recommended: use a Python virtual environment.

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required modules
pip install -r requirements.txt
```

If you need the latest `jobspy`:
```bash
<<<<<<< HEAD
git clone https://github.com/VorpalElf/JobSpy.git
cd JobSpy
pip install .
=======
pip install -U python-jobspy
>>>>>>> 6a49e12 (Add proxy testing functionality and update README with usage instructions)
```

## Usage
Run the CLI with required arguments:
```bash
python3 jobspy_runner/cli.py --search "Software Engineer" --location "New York"
```


Optional arguments:

Optional arguments (short flags available):
- `--sites`, `-s` linkedin indeed (default: linkedin)
- `--results`, `-r` 20 (default: 10)
- `--proxies`, `-p` <your_proxies_file> (default: Proxies/proxies_list.txt)
- `--numbered`, `-n` (write numbered CSV)
- `--out`, `-o` jobs.csv (output path)
- `--description`, `-d` (fetch description text; no description by default)

See all options:
```bash
python jobspy_runner/cli.py --help
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
jobspy_runner/cli.py      # CLI entry point
Proxies/                  # Proxy list & tester
requirements.txt          # Python dependencies
pyproject.toml            # Project metadata
```

## Notes
- Respect site Terms of Service.
- Use responsible scraping intervals.

## License
See LICENSE file.
