# TiBot

TiBot is a small Korean school assistant originally distributed as a zip archive.
The repository now contains the recoverable source files and a stable command-line
entry point for NEIS school data.

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:TIBOT_NEIS_API_KEY = "your-neis-key"
```

The key can also be supplied with `--api-key`. Never commit `api_key.json`.

## Usage

```powershell
python app.py --school "서울고등학교" --action school
python app.py --school "서울고등학교" --action meal --date 20260727
python app.py --school "서울고등학교" --action schedule --date 20260727
python app.py --school "서울고등학교" --action timetable --date 20260727 --grade 1 --class-name 3
```

The original interactive modules remain available for reference. `app.py` is the
portable, documented entry point and uses timeouts plus explicit API errors.
