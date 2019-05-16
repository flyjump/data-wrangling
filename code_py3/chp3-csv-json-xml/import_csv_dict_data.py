import csv

csvfile = open('../../data/chp3/data-text.csv', 'r', encoding='utf-8')
reader = csv.DictReader(csvfile)

d = None
for row in reader:
    print(row)
    d = row
print(dict(d))
