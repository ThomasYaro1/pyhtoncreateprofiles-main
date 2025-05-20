import csv
import json

def test_csv_column_count():
    with open('profiles1.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        assert len(header) == 12

def test_csv_row_count():
    with open('profiles1.csv', newline='', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile))[1:]
        assert len(reader) > 900

def test_json_properties():
    with open('data.json', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        keys = data[0].keys()
        assert 'name' in keys and 'email' in keys

def test_json_row_count():
    with open('data.json', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        assert len(data) > 900
