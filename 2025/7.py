with open("input_day7.txt", "r") as file:
    data = file.readlines()

rays = {data[0].find('S')}
pw = 0
for line in data:
    new_rays = set()
    for i in rays:
        if line[i] == '^':
            new_rays.add(i-1)
            new_rays.add(i+1)
            pw += 1
        else:
            new_rays.add(i)
    rays = new_rays
print(pw)

rays = {data[0].find('S') : 1}
for line in data:
    new_rays = {}
    for (i, v) in rays.items():
        if line[i] == '^':
            if i-1 in new_rays.keys():
                new_rays[i-1] += v
            else:
                new_rays[i-1] = v
            if i+1 in new_rays.keys():
                new_rays[i+1] += v
            else:
                new_rays[i+1] = v
        else:
            if i in new_rays.keys():
                new_rays[i] += v
            else:
                new_rays[i] = v
    rays = new_rays
print(sum(rays.values()))
