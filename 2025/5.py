with open("input_day5.txt", "r") as file:
    data = file.readlines()

ranges = []
r = True
pw = 0
for line in data:
    line = line.strip()
    if r:
        if line == "":
            r1 = 0
            while r1 < len(ranges):
                r2 = r1 + 1
                while r2 < len(ranges):
                    if ranges[r1][0]<=ranges[r2][0] and ranges[r2][0]<=ranges[r1][1]:
                        if ranges[r1][1] < ranges[r2][1]:
                            ranges[r1][1] = ranges[r2][1]
                        ranges.remove(ranges[r2])
                        r2 = r1+1
                        continue
                    elif ranges[r1][0]<=ranges[r2][1] and ranges[r2][1]<=ranges[r1][1]:
                        if ranges[r1][0] > ranges[r2][0]:
                            ranges[r1][0] = ranges[r2][0]
                        ranges.remove(ranges[r2])
                        r2 = r1+1
                        continue
                    elif ranges[r1][0]>=ranges[r2][0] and ranges[r1][1]<=ranges[r2][1]:
                        ranges[r1] = ranges[r2]
                        ranges.remove(ranges[r2])
                        r2 = r1+1
                        continue
                    r2 += 1
                r1 += 1
            r = False
            continue
        l = list(map(int, line.split('-')))
        ranges.append(l)
    else:
        n = int(line)
        for ra in ranges:
            if ra[0]<=n and n<=ra[1]:
                pw += 1
                break

print(pw)

pw2 = 0
for r in ranges:
    pw2 += r[1] - r[0] +1

print(pw2)
