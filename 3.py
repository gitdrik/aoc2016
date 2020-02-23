ts = []
with open('3.txt') as f:
    for line in f:
        t = [int(line[0:5]), int(line[5:10]), int(line[10:])]
        ts.append(t)

p = 0
for t in ts:
    if (t[0]+t[1]>t[2]) & (t[0]+t[2]>t[1]) & (t[1]+t[2]>t[0]):
        print(t)
        p +=1
print(p)
