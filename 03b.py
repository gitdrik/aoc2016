ts = []
with open('03.txt') as f:
    for line in f:
        t = [int(line[0:5]), int(line[5:10]), int(line[10:])]
        ts.append(t)

ts = ([ts[x][0] for x in range(len(ts))]+
      [ts[x][1] for x in range(len(ts))]+
      [ts[x][2] for x in range(len(ts))])

p = 0
for i in range(0,len(ts),3):
    t = ts[i:i+3]
    if (t[0]+t[1]>t[2]) & (t[0]+t[2]>t[1]) & (t[1]+t[2]>t[0]):
        print(t)
        p +=1
print(p)
