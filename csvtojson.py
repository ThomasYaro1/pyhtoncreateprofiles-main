import csv
import json

import csv
import json
import sys

def csv_to_json(csv_file, json_file):
    try:
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
            print(f"DEBUG: Read {len(data)} rows from {csv_file}")  # Loggning

        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"DEBUG: Successfully wrote {json_file}")  # Bekräftelse

    except Exception as e:
        print(f"ERROR in csv_to_json: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    csv_to_json('profiles1.csv', 'data.json')