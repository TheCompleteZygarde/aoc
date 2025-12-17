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

def rec2(current, visited):
    if current == 'out':
        return 'dac' in visited and 'fft' in visited
    ret = 0
    for node in connections[current]:
        if node in visited:
            continue
        ret += rec2(node, visited | {node})
    return ret

print(rec2('svr', {'svr'}))
