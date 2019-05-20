from csv import DictReader
import time

data_rdr = DictReader(open('../../data/unicef/mn.csv', 'r', encoding='utf-8'))
header_rdr = DictReader(open('../../data/unicef/mn_headers.csv', 'r', encoding='utf-8'))

data_rows = [dict(d) for d in data_rdr]
header_rows = [dict(h) for h in header_rdr]
new_rows = []
print(len(data_rows))
print(data_rows[0])
print(len(data_rows[0]))
print(len(header_rows))
print(header_rows[0:2])

start_time = time.time()
# 代码复杂度太高 9008*159*200
for data_dict in data_rows:
    new_row = {}
    for dkey, dval in data_dict.items():
        for header_dict in header_rows:
            if dkey in header_dict.values():
                new_row[header_dict.get('Label')] = dval
    new_rows.append(new_row)
end_time = time.time()
print(new_rows[0])
print('cost time: %.2f' % (end_time - start_time))
