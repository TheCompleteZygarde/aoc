def compare(left, right):
    return max(left, right) - min(left, right)


def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)


def ui():
    tot = 0
    all_inputs = []
    while True:
        line = input()
        if line == " ":
            break

        lst = line.split()
        all_inputs.append([int(lst[0]), int(lst[1])])

    all_inputs = list(zip(*all_inputs))
    lst_sorted = [sorted(all_inputs[0]), sorted(all_inputs[1])]

    for i in range(len(lst_sorted[0])):
        tot += lst_sorted[0][i] * len(indices(lst_sorted[1], lst_sorted[0][i]))  #+= compare(int(lst_sorted[0][i]), int(lst_sorted[1][i]))


    print(tot)

