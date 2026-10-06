from pathlib import Path
import argparse

PROMPTS = Path("prompts")

def cmd_list():
    files = sorted(PROMPTS.glob("*.txt"))
    for f in files:
        print(f.name)

def cmd_search(word):
    for f in sorted(PROMPTS.glob("*.txt")):
        if word.lower() in f.read_text().lower():
            print(f.name)

parser = argparse.ArgumentParser(description="Manage my prompts library")
commands = parser.add_subparsers(dest="command", required=True)
commands.add_parser("list", help="List all prompts files")

sub_search = commands.add_parser("search", help="Find prompts containing a word")
sub_search.add_argument("word", help="Word to search for")

args = parser.parse_args()

if args.command == "list":
    cmd_list()
elif args.command == "search":
    cmd_search(args.word)