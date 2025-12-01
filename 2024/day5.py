from functools import cmp_to_key

data = ""
with open("input_day5.txt", "r") as file:
    data = file.readlines()

rules = {}
i = 0
tota = 0
totb = 0

for rule in data:
    try:
        rule[2]
    except IndexError:
        i = data.index(rule) + 1
        break
    if rule[:2] in rules:
        rules[rule[:2]].append(rule[3:5])
    else:
        rules[rule[:2]] = [rule[3:5]]

for line in data[i:]:
    lst = line.split(",")
    lst[-1] = lst[-1][:2]
    check = True
    for elem in lst[::-1]:
        if elem in rules:
            for rule in rules[elem]:
                if rule in lst[:lst.index(elem)]:
                    check = False
                    break
        if not check:
            break
    if check:
        tota += int(lst[len(lst)//2])

def comp(a, b):
    if a in rules and b in rules[a]:
        return -1
    else:
        return 1

new_lines = []
for line in data[i:]:
    lst = line.split(",")
    lst[-1] = lst[-1][:2]
    check = True
    for elem in lst[::-1]:
        if elem in rules:
            for rule in rules[elem]:
                if rule in lst[:lst.index(elem)]:
                    totb += int(sorted(lst, key=cmp_to_key(comp))[len(lst)//2])
                    check = False
                    break
        if not check:
            break

print(tota, totb)
