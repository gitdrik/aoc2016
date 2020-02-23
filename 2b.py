digs = []
with open('2.txt') as f:
    for line in f:
        digs.append(line.strip())

pad = ['XXXXXXX','XXX1XXX','XX234XX','X56789X','XXABCXX','XXXDXXX','XXXXXXX']
x = 1
y = 3
code = []
for steps in digs:
    for s in steps:
        if s == 'U':
            if pad[y-1][x] != 'X':
                y -= 1
        elif s == 'R':
            if pad[y][x+1] != 'X':
                x += 1
        elif s == 'D':
            if pad[y+1][x] != 'X':
                y += 1
        else:
            if pad[y][x-1] != 'X':
                x -= 1
    code.append(pad[y][x])
print(code)
