digs = []
with open('2.txt') as f:
    for line in f:
        digs.append(line.strip())

pad = [[1,2,3],[4,5,6],[7,8,9]]
posx = 1
posy = 1
code = []
for steps in digs:
    for s in steps:
        if s == 'U':
            posy = max(0, posy-1)
        elif s == 'R':
            posx = min(2, posx+1)
        elif s == 'D':
            posy = min(2, posy+1)
        else:
            posx = max(0, posx-1)
    code.append(pad[posy][posx])
print(code)
