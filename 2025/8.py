import math
import operator
with open("input_day8.txt", "r") as file:
    data = file.readlines()

data = [tuple([int(x) for x in line.split(',')]) for line in data]
dist = {}
for i, coord in enumerate(data[:-1]):
    for coord2 in data[i+1:]:
        dist[(coord, coord2)] = math.sqrt(
                (coord[0]-coord2[0])**2 + 
                (coord[1]-coord2[1])**2 +
                (coord[2]-coord2[2])**2)

dists = sorted(dist.items(), key=operator.itemgetter(1))

circuits = [{coord} for coord in data]
index = dict(zip(data, range(len(data))))
for d in dists[:1000]:
    if index[d[0][0]] == index[d[0][1]]:
        continue
    smallest_index = min(index[d[0][0]], index[d[0][1]])
    biggest_index = max(index[d[0][0]], index[d[0][1]])
    circuits[smallest_index] = circuits[smallest_index] | circuits[biggest_index]
    circuits.remove(circuits[biggest_index])
    for key, value in index.items():
        if value == biggest_index:
            index[key] = smallest_index
        if value > biggest_index:
            index[key] -= 1

biggest = []
for c in circuits:
    biggest.append(len(c))
    if len(biggest) > 3:
        biggest.remove(min(biggest))

circuits.sort(key=len)
print(math.prod(map(len, circuits[-3:])))

coords = ((0,), (0,))
for d in dists[1000:]:
    if len(circuits) <= 1:
        break
    if index[d[0][0]] == index[d[0][1]]:
        continue
    coords = d[0]
    smallest_index = min(index[d[0][0]], index[d[0][1]])
    biggest_index = max(index[d[0][0]], index[d[0][1]])
    circuits[smallest_index] = circuits[smallest_index] | circuits[biggest_index]
    circuits.remove(circuits[biggest_index])
    for key, value in index.items():
        if value == biggest_index:
            index[key] = smallest_index
        if value > biggest_index:
            index[key] -= 1
print(coords)
print(coords[0][0] * coords[1][0])
