from itertools import combinations
import numpy
import scipy.optimize as op
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


pw2 = 0
for line in data:
    line = line.strip().split()
    targets = numpy.array(list(map(int, line[-1][1:-1].split(','))))
    buttons = [set(map(int, val[1:-1].split(','))) for val in line[1:-1]]
    nbuttons = numpy.array([[1 if i in buttons[n] else 0 for i in range(len(targets))] for n in range(len(buttons))])
    nbuttons = numpy.transpose(nbuttons)
    solution = op.milp(
        numpy.ones(len(nbuttons[0])), 
        integrality=numpy.ones(nbuttons.shape[1], dtype=int), 
        constraints=op.LinearConstraint(nbuttons, targets, targets), 
        bounds=op.Bounds(0, numpy.inf))
    pw2 += int(solution.fun)
print(pw2)
