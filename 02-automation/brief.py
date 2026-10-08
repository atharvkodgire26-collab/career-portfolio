from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen
import argparse
import json

parser = argparse.ArgumentParser(description="Build a daily brief from Hacker News")
parser.add_argument("keyword", help="Topic to search for")
parser.add_argument("--min-points", type=int, default=600, help="Minimum score to keep (default: 600)")

args = parser.parse_args()

url = f"https://hn.algolia.com/api/v1/search?query={quote(args.keyword)}&tags=story"

with urlopen(url) as response:
    data = json.load(response)

report = f"# Daily Brief: {args.keyword}\n\n"

for h in data["hits"]:
    if h["points"] >= args.min_points:
        report += f'- {h["title"]} ({h["points"]} points)\n'

Path("brief.md").write_text(report, encoding="utf-8")
print(f"Saved brief.md  |  keyword: {args.keyword}  |  min points: {args.min_points}")
