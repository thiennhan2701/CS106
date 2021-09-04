import csv

with open('result1.txt') as f:
    lines = f.readlines()
    lines = map(lambda s: s.replace('\n', ''), lines)
    lines = filter(lambda s: s != '', lines)
    lines = list(lines)
    rows = []
    for i in range(0, len(lines), 4):
        title = lines[i].split()[2].split('/')
        group = title[1]
        n = int(title[2][1:])
        result = lines[i+3].split()
        weight = int(result[4].replace(',', ''))
        value = int(result[-1])
        rows.append([group, n, weight, value])
    with open('resultmaxgen100.csv', mode='w', newline='', encoding='utf-8') as csvf:
        csv_writer = csv.writer(csvf, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['group', 'n', 'weight', 'value'])
        for row in rows:
            csv_writer.writerow(row)
