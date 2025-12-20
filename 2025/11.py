from functools import cache
with open("input_day11.txt", "r") as file:
    data = file.readlines()

connections = {}
for line in data:
    line = line.strip().split(':')
    connections[line[0]] = line[1].strip().split(' ')


def rec(current, visited):
    if current == 'out':
        return 1
    ret = 0
    for node in connections[current]:
        if node in visited:
            continue
        ret += rec(node, visited | {node})
    return ret

print(rec('you', {'you'}))

@cache
def rec2(current, goal):
    if current == goal:
        return 1
    if current not in connections:
        return 0
    ret = 0
    for node in connections[current]:
        ret += rec2(node, goal)
    return ret

svrfft = rec2('svr', 'fft')
print(svrfft)
fftdac = rec2('fft', 'dac')
print(fftdac)
dacout = rec2('dac', 'out')
print(dacout)
print(svrfft * fftdac * dacout)
