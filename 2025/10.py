from itertools import combinations
with open("input_day10.txt", "r") as file:
    data = file.readlines()

def loop(lights, buttons):
    for i in range(len(buttons)+1):
        for l in combinations(buttons, i+1):
            newLights = list(lights)
            for button in l:
                newLights = [not newLights[i] if i in button else newLights[i] for i in range(len(lights))]
            if not any(newLights):
                return i+1
    return 0


pw = 0
for line in data:
    line = line.strip().split()
    lights = list(map(lambda a: a == '#', line[0][1:-1]))
    buttons = [list(map(int, val[1:-1].split(','))) for val in line[1:-1]]
    pw += loop(lights, buttons)
print(pw)
