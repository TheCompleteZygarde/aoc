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
            if s[0:n]*(len(s)//n) == s:
                pw+=i
                break
print(pw)
