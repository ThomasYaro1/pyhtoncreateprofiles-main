import json

def test_json_properties():
    with open('data.json', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        keys = data[0].keys()
        assert 'Givenname' in keys and 'Surname' in keys
