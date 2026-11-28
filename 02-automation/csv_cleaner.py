import csv
import re
from pathlib import Path

INPUT_FILE = "messy_leads.csv"
OUTPUT_FILE = "clean_leads.csv"

def clean_phone(phone):
    # Remove everything except digits
    digits = re.sub(r'\D', '', phone)
    # If it's 10 digits, format it nicely. Otherwise, mark as invalid.
    if len(digits) == 10:
        return f"{digits[:5]}-{digits[5:]}"
    return "INVALID"

def clean_email(email):
    return email.strip().lower()

def clean_name(name):
    # Title case and strip extra spaces
    return name.strip().title()

def main():
    input_path = Path(INPUT_FILE)
    if not input_path.exists():
        print(f"❌ Error: {INPUT_FILE} not found!")
        return

    cleaned_rows = []
    
    # 1. Read the messy data
    with open(input_path, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            # 2. Skip rows with missing critical data (like name)
            if not row['name'].strip():
                continue
            
            # 3. Clean the data
            clean_row = {
                'Name': clean_name(row['name']),
                'Email': clean_email(row['email']),
                'Phone': clean_phone(row['phone']),
                'Company': clean_name(row['company'])
            }
            cleaned_rows.append(clean_row)

    # 4. Write the clean data to a new file
    output_path = Path(OUTPUT_FILE)
    with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['Name', 'Email', 'Phone', 'Company']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(cleaned_rows)

    print(f"✅ Success! Cleaned {len(cleaned_rows)} rows.")
    print(f"📁 Saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()