from typing import NoDefault
#from aocd.models import Puzzle

#puzzle = Puzzle(2024, 3)
#data = puzzle.input_data
data = ""
with open("input_day3.txt", "r") as file:
    data = file.readlines()

line = ""
for elem in data:
    line += elem

total = 0
num1 = ""
num2 = ""
i = 0
while i < len(line):
    if line[i:i+7] == "don't()":
        while line[i:i+4] != "do()":
            i += 1
            if i > len(line):
                break
    if line[i:i+4]== "mul(":
        num1 = ""
        i += 4
        c = line[i]
        while c.isdigit():
            num1 += c
            i += 1
            c = line[i]
        if 0 < len(num1) < 4 and c == ",":
            num1 = int(num1)

            num2 = ""
            i += 1
            c = line[i]
            while c.isdigit():
                num2 += c
                i += 1
                c = line[i]
            if 0 < len(num2) < 4 and c == ")":
                num2 = int(num2)
                total += num1*num2
    i += 1
print(total)
