import csv

csvfile = open('../../data/chp3/data-text.csv', 'r', encoding='utf-8')
reader = csv.reader(csvfile)

for row in reader:
    print(row)
