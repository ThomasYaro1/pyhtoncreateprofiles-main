import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            if 'Birthday' in row:
                row['Birthday'] = str(row['Birthday'])
            data.append(row)
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)