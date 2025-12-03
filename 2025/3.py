data = ""
with open("input_day3.txt", "r") as file:
    data = file.readlines()

#data = ["987654321111111", "811111111111119","234234234234278","818181911112111"]
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
    print(line)
    out = line[0:12]
    print(out)
    for i in range(len(line)):
        n = len(line)-i
        if n > 12:
            n = 12
        if line[i]>out[12-n]:
            out = out[:12-n] + line[i:i+n+1]
            print(out)
    pw+=int(out)
print(pw)
