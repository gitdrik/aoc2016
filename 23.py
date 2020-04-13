l = []
with open('23.txt') as f:
    for line in f:
        l.append(line.strip().split())
#Part1 regs = {'a':12,'b':0,'c':0,'d':0}
regs = {'a':12,'b':0,'c':0,'d':0}
i = 0
while i < len(l):
    inc = 1
    if l[i][0] == 'jnz':
        if l[i][1] in regs:
            if regs[l[i][1]] != 0:
                if l[i][2] not in regs:
                    inc = int(l[i][2])
                else:
                    inc = regs[l[i][2]]
        elif l[i][1] != '0':
            if l[i][2] not in regs:
                inc = int(l[i][2])
            else:
                inc = regs[l[i][2]]
    elif l[i][0] == 'cpy':
        if l[i][1] in regs and l[i][2] in regs:
            regs[l[i][2]] = regs[l[i][1]]
        elif l[i][2] in regs and l[i][1] not in regs:
            regs[l[i][2]] = int(l[i][1])
    elif l[i][0] == 'inc':
        if l[i][1] in regs: regs[l[i][1]] += 1
    elif l[i][0] == 'dec':
        if l[i][1] in regs: regs[l[i][1]] -= 1
    elif l[i][0] == 'tgl':
        if l[i][1] in regs:
            j = i + regs[l[i][1]]
            if j in range(len(l)):
                if   l[j][0] == 'jnz': l[j][0] = 'cpy'
                elif l[j][0] == 'cpy': l[j][0] = 'jnz'
                elif l[j][0] == 'inc': l[j][0] = 'dec'
                elif l[j][0] == 'dec': l[j][0] = 'inc'
                elif l[j][0] == 'tgl': l[j][0] = 'inc'
    i += inc
print(regs['a'])
