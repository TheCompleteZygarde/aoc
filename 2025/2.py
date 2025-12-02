data = ""
with open("input_day2.txt", "r") as file:
    data = file.readline().split(',')

pw = 0
for line in data:
    line = line.split('-')
    for i in range(int(line[0]), int(line[1])):
        n = str(i)
        if len(n)%2:
            continue
        if n[0:(len(n)//2)] == n[len(n)//2:]:
            pw += i
print(pw)

pw = 0
for line in data:
    line = line.split('-')
    for i in range(int(line[0]), int(line[1])):
        s = str(i)
        for n in range(1, len(str(s))//2 +1):
            if len(s)%n:
                continue
            l = [s[a:a+n] for a in range(0, len(s), n)]
            check = True
            for a in l[1:]:
                if a != l[0]:
                    check = False
                    break
            if check:
                pw += i
                break
print(pw)
