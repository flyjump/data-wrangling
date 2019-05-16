import json

json_data = open('../../data/chp3/data-text.json', encoding='utf-8').read()

data = json.loads(json_data)

for item in data:
    print(item)
print(type(json_data))
