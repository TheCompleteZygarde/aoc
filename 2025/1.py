data = ""
with open("input_day1.txt", "r") as file:
    data = file.readlines()

pw = 0
c = 50
for line in data:
    if line[0]=='L':
        if c==0:
            pw-=1
        c -=int(line[1:])
    else:
        c +=int(line[1:])
    if c<1:
        pw+=abs(c//100)
        c%=100
        if c==0:
            pw+=1
    if c>99:
        pw+=c//100
        c%=100
print(pw)
