import math
with open("input_day6.txt", "r") as file:
    data = file.readlines()
rows = []
for line in data:
    rows.append(line.split())
columns = zip(*rows)

pw = 0
for column in columns:
    res = int(column[0])
    op = column[-1]
    for elem in column[1:-1]:
        if op == '+':
            res += int(elem)
        else:
            res *= int(elem)
    pw += res
print(pw)

pw = 0
elems = []
for i in range(len(data[0]) - 2, -1, -1):
    elem = ''
    for row in data[:-1]:
        elem += row[i]
    try: elems.append(int(elem))
    except: pass

    if data[-1][i] != ' ':
        pw += sum(elems) if data[-1][i] == '+' else math.prod(elems)
        elems = []
print(pw)
