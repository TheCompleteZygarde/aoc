data = ""
with open("input_day4.txt", "r") as file:
    data = file.readlines()

pw = 0
for y in range(len(data)):
    for x in range(len(data[y])-1):
        c = 0
        if data[y][x] != '@':
            continue
        for yi in range(y-1, y+2):
            for xi in range(x-1, x+2):
                if (xi == x and yi == y) or xi < 0 or yi < 0 or yi >= len(data) or xi >= len(data[0]):
                    continue
                if data[yi][xi] == '@':
                    c += 1
        if c<4:
            pw += 1
print(pw)


pw = 0
done = False
while not done:
    done = True
    for y in range(len(data)):
        for x in range(len(data[y])-1):
            c = 0
            if data[y][x] != '@':
                continue
            for yi in range(y-1, y+2):
                for xi in range(x-1, x+2):
                    if (xi == x and yi == y) or xi < 0 or yi < 0 or yi >= len(data) or xi >= len(data[0]):
                        continue
                    if data[yi][xi] == '@':
                        c += 1
            if c<4:
                pw += 1
                data[y] = data[y][0:x] + '.' + data[y][x+1:]
                done = False
print(pw)
