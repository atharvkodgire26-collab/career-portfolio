from pathlib import Path
from urllib.request import urlopen
import argparse
import gzip
import hashlib
import json

STATE = Path("watch-state.json")

parser = argparse.ArgumentParser(description="Watch a web page for changes")
parser.add_argument("url", help="The page to watch")
args = parser.parse_args()

with urlopen(args.url) as response:
    raw = response.read()
    if response.headers.get("Content-Encoding") == "gzip":
        raw = gzip.decompress(raw)

html = raw.decode("utf-8", errors="replace")
fingerprint = hashlib.sha256(html.encode("utf-8")).hexdigest()

if STATE.exists():
    state = json.loads(STATE.read_text())
else:
    state = {}

previous = state.get(args.url)

if previous is None:
    print(f"First check — now watching {args.url}")
elif previous == fingerprint:
    print("No change.")
else:
    print(f"CHANGED — {args.url}")

state[args.url] = fingerprint
STATE.write_text(json.dumps(state, indent=2))
print(f"Tracking {len(state)} page(s)")