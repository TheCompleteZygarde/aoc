data = ""
with open("input_day4.txt", "r") as file:
    data = file.readlines()

num_a = 0
num_b = 0
for n, line in enumerate(data):
    for i, c in enumerate(line):
        if c == "X":
            if line[i-3:i+1] == "SAMX":
                num_a += 1
            if line[i:i+4] == "XMAS":
                num_a += 1
            if n > 2:
                if data[n-1][i] == "M" and data[n-2][i] == "A" and data[n-3][i] == "S":
                    num_a += 1
                if i > 2 and data[n-1][i-1] == "M" and data[n-2][i-2] == "A" and data[n-3][i-3] == "S":
                    num_a += 1
                if i < len(line)-3 and data[n-1][i+1] == "M" and data[n-2][i+2] == "A" and data[n-3][i+3] == "S":
                    num_a += 1
            if n < len(data)-3:
                if data[n+1][i] == "M" and data[n+2][i] == "A" and data[n+3][i] == "S":
                    num_a += 1
                if i > 2 and data[n+1][i-1] == "M" and data[n+2][i-2] == "A" and data[n+3][i-3] == "S":
                    num_a += 1
                if i < len(line)-3 and data[n+1][i+1] == "M" and data[n+2][i+2] == "A" and data[n+3][i+3] == "S":
                    num_a += 1
        if c == "A" and 0 < n < len(data)-1 and 0 < i < len(line)-1:
            if (data[n-1][i-1] == "M" and data[n+1][i+1] == "S") or (data[n-1][i-1] == "S" and data[n+1][i+1] == "M"):
                if (data[n+1][i-1] == "M" and data[n-1][i+1] == "S") or (data[n+1][i-1] == "S" and data[n-1][i+1] == "M"):
                    num_b += 1

print(num_b)
