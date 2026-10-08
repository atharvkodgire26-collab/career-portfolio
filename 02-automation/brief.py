from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen
import argparse
import json
import time

parser = argparse.ArgumentParser(description="Build a daily brief from Hacker News")
parser.add_argument("keyword", help="Topic to search for")
parser.add_argument("--min-points", type=int, default=50, help="Minimum score to keep (default: 50)")
parser.add_argument("--days", type=int, default=7, help="How many days back to look (default: 7)")

args = parser.parse_args()

word = args.keyword.lower()
cutoff = int(time.time()) - args.days * 24 * 60 * 60
url = f"https://hn.algolia.com/api/v1/search?query={quote(args.keyword)}&tags=story&numericFilters=created_at_i%3E{cutoff}"

with urlopen(url) as response:
    data = json.load(response)

report = f"# Daily Brief: {args.keyword}\n\n"
kept = 0

for h in data["hits"]:
    if word in h["title"].lower() and h["points"] >= args.min_points:
        report += f'- {h["title"]} ({h["points"]} points)\n'
        kept += 1

if kept == 0:
    report += "_No matches. Try lowering --min-points or raising --days._\n"

Path("brief.md").write_text(report, encoding="utf-8")
print(f"Saved brief.md  |  {args.keyword}  |  {kept} stories  |  {args.days}d  |  min {args.min_points}")