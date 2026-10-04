from pathlib import Path

files = Path("prompts").glob("*.txt")
for f in sorted(files):
    print(f.name)