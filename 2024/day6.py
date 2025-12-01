data = ""
with open("input_day6.txt", "r") as file:
    data = file.readlines()

dir = {0: (-1, 0),
       1: (0, 1),
       2: (1, 0),
       3: (0, -1)}

x = len(data[0])
y = len(data)
l = (y, x)
d = 0
i = [0, 0]

for line in data:
    if "^" in line:
        i = [data.index(line), line.index("^")]

while True:
    if i[0] < 0 or i[0] >= l[0] or i[1] < 0 or i[1] >= l[1]:
        break
    next_pos = [i[0] + dir[d][0], i[1] + dir[d][1]]
    try:
        if data[next_pos[0]][next_pos[1]] == "#":
            d = (d+1)%4
    except IndexError:
        pass
    else:
        new_i = i
        new_d = (d+1)%4
        loops = 0
        while True:
            if new_i[0] < 0 or new_i[0] > l[0] or new_i[1] < 0 or new_i[1] > l[1]:
                break
            new_next_pos = [new_i[0] + dir[new_d][0], new_i[1] + dir[new_d][1]]
            try:
                if data[new_next_pos[0]][new_next_pos[1]] == "#":
                    new_d = (new_d+1)%4
                    if (i == new_i and d == new_d) or loops > 1000:
                        new_i = [new_i[0] + dir[new_d][0], new_i[1] + dir[new_d][1]]
                        data[new_i[0]] = data[new_i[0]][:new_i[1]] + "O" + data[new_i[0]][new_i[1] + 1:]
                        break
            except IndexError:
                pass
            else:
                new_i = new_next_pos
                if (i == new_i and d == new_d) or loops > 1000:
                    new_i = [new_i[0] + dir[new_d][0], new_i[1] + dir[new_d][1]]
                    data[new_i[0]] = data[new_i[0]][:new_i[1]] + "O" + data[new_i[0]][new_i[1] + 1:]
                    break
                loops += 1
        if data[i[0]][i[1]] != "O":
            data[i[0]] = data[i[0]][:i[1]] + "X" + data[i[0]][i[1] + 1:]
        i = next_pos

tota = 0
totb = 0
for line in data:
    print(line)
    tota += line.count("X")
    totb += line.count("O")

tota += totb

print(tota, totb)

