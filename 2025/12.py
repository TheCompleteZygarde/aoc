with open("input_day12.txt", "r") as file:
    data = file.readlines()

counter = 0
pw = 0
for line in data:
    line = line.strip()
    if line == '':
        counter += 1
        continue
    if counter < 6:
        continue
    l = line.split(':')
    x = int(l[0].split('x')[0])
    y = int(l[0].split('x')[1])
    if (x//3) * (y//3) >= sum([int(i) for i in l[1].strip().split(' ')]):
        pw += 1
print(counter)
print(pw)

