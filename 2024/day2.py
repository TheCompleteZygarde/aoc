
#from aocd.models import Puzzle

#puzzle = Puzzle(2024, int("02"))
#data = puzzle.input_data
#lines = data.splitlines()

def cond(val1, val2):
    return val1 < val2 and val2 - val1 < 4

def ev(line, first=False):
    for i, value in enumerate(line[:-1]):
        if not cond(int(value), int(line[i+1])):
            if first:
                return ev(line[:i] + line[i+1:], False) or ev(line[:i+1] + line[i+2:], False)
            else:
                return False
    return True

lines = []
while True:
    line = input()
    if line == " ":
        break
    lines.append(line)

safe = 0

for line in lines:
    values = line.split()

    check = False

    for n in range(len(values)):
        if ev([values[i] for i in range(len(values)) if i != n]):
            check = True
            break

    values = values[::-1]

    for n in range(len(values)):
        if ev([values[i] for i in range(len(values)) if i != n]):
            check = True
            break

    if check:
        safe += 1
        print(safe)
    else:
        print(line)
print(safe)
