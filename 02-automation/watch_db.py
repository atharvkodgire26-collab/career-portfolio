from pathlib import Path
from urllib.request import urlopen
import argparse
import gzip
import hashlib
import json
import sqlite3
from datetime import datetime
import ssl

# 1. Setup Database
conn = sqlite3.connect("watch_history.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        status TEXT,
        checked_at TEXT
    )
""")
conn.commit()

# 2. Setup Argparse
parser = argparse.ArgumentParser(description="Watch a web page and log to database")
parser.add_argument("url", help="The page to watch")
args = parser.parse_args()

# 3. Fetch and Hash (with SSL bypass for Windows)
context = ssl._create_unverified_context()
with urlopen(args.url, context=context) as response:
    raw = response.read()
    if response.headers.get("Content-Encoding") == "gzip":
        raw = gzip.decompress(raw)
    html = raw.decode("utf-8", errors="replace")
    fingerprint = hashlib.sha256(html.encode("utf-8")).hexdigest()

# 4. Check State
STATE = Path("watch-state.json")
if STATE.exists():
    state = json.loads(STATE.read_text())
else:
    state = {}

previous = state.get(args.url)
if previous is None:
    status = "FIRST_CHECK"
    print(f"First check — now watching {args.url}")
elif previous == fingerprint:
    status = "NO_CHANGE"
    print("No change.")
else:
    status = "CHANGED"
    print(f"CHANGED — {args.url}")

# 5. Save to JSON and Database
state[args.url] = fingerprint
STATE.write_text(json.dumps(state, indent=2))

now = datetime.now().isoformat()
cursor.execute(
    "INSERT INTO logs (url, status, checked_at) VALUES (?, ?, ?)",
    (args.url, status, now)
)
conn.commit()
conn.close()

print(f"Logged to database. Tracking {len(state)} page(s) total.")