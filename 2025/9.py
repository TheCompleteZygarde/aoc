with open("input_day9.txt", "r") as file:
    data = file.readlines()

pw = 0
for i, line in enumerate(data):
    c1 = [int(elem.strip()) for elem in line.split(',')]
    for line2 in data[i:]:
        c2 = [int(elem.strip()) for elem in line2.split(',')]
        size = (abs(c1[0]-c2[0])+1) * (abs(c1[1]-c2[1])+1)
        if size > pw:
            pw = size
print(pw)

data = [[int(elem.strip()) for elem in line.split(',')] for line in data]

pw = 0
for i, point in enumerate(data[:-1]):
    for point2 in data[i:]:
        valid = True
        for n, point3 in enumerate(data):
            if point3[0] == data[n-1][0]:
                #Vertical
                if point3[0] <= min(point[0], point2[0]) or point3[0] >= max(point[0], point2[0]):
                    continue
                if max(point3[1], data[n-1][1]) > min(point[1], point2[1]) and min(point3[1], data[n-1][1]) < max(point[1], point2[1]):
                    valid = False
                    break
            else:
                #Horizontal
                if point3[1] <= min(point[1], point2[1]) or point3[1] >= max(point[1], point2[1]):
                    continue
                if max(point3[0], data[n-1][0]) > min(point[0], point2[0]) and min(point3[0], data[n-1][0]) < max(point[0], point2[0]):
                    valid = False
                    break
        if valid:
            size = (abs(point[0]-point2[0])+1) * (abs(point[1]-point2[1])+1)
            if size > pw:
                pw = size

print(pw)
