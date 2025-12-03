data = ""
with open("input_day3.txt", "r") as file:
    data = file.readlines()

#data = ["987654321111111\n", "811111111111119\n","234234234234278\n","818181911112111\n"]
pw = 0
for line in data:
    c1 = "0"
    c2 = "0"
    for c in line[:-2]:
        if c>c1:
            c1 = c
            c2 = "0"
        elif c>c2:
            c2 = c

    if line[-2]>c2:
        c2=line[-2]
    pw+=int(c1+c2)
print(pw)


pw = 0
for line in data:
    line = line.strip()
    out = "000000000000"
    for i in range(len(line)):
        for n in range(0, 12):
            if 12-n + i > len(line):
                continue
            if line[i]>out[n]:
                out = out[:n] + line[i] + "0"*(11-n)
                break
    pw+=int(out)
print(pw)
