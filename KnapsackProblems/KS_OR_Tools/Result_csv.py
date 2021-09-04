import csv

with open('Result_ORTOOLS.txt') as f:
    lines = f.readlines()
    lines = map(lambda s: s.replace('\n', ''), lines)
    lines = filter(lambda s: s != '', lines)
    lines = list(lines)
    rows = []
    for i in range(0, len(lines), 3):
        title = lines[i].split('-')
        print(title)
        group = title[0]
        n = int(title[1][1:])
        weight = int(lines[i+2].split()[2])
        print(weight)
        value = int(lines[i+1].split()[3])
        rows.append([group, n, weight, value])
    with open('result.csv', mode='w', newline='', encoding='utf-8') as csvf:
        csv_writer = csv.writer(csvf, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['group', 'n', 'weight', 'value'])
        for row in rows:
            csv_writer.writerow(row)
