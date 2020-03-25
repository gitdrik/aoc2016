l = []
with open('12.txt') as f:
    for line in f:
        l.append(line.strip().split())

regs = {'a':0,'b':0,'c':1,'d':0}
i = 0
while i < len(l):
    inc = 1
    if l[i][0] == 'jnz':
        if l[i][1] in regs:
            if regs[l[i][1]] != 0:
                inc = int(l[i][2])
        elif l[i][1] != '0':
            inc = int(l[i][2])
    elif l[i][0] == 'cpy':
        if l[i][1] in regs:
            regs[l[i][2]] = regs[l[i][1]]
        else:
            regs[l[i][2]] = int(l[i][1])
    elif l[i][0] == 'inc':
        regs[l[i][1]] += 1
    elif l[i][0] == 'dec':
        regs[l[i][1]] -= 1
    i += inc

print(regs['a'])
