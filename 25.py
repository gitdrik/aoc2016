import sys
l = []
with open('25.txt') as f:
    for line in f:
        l.append(line.strip().split())

seed = 0
while 1:
    seed += 1
    regs = {'a':seed,'b':0,'c':0,'d':0}
    i = 0
    prevout = 1
    outs = 0
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
        elif l[i][0] == 'out':
            if l[i][1] in regs:
                out = regs[l[i][1]]
            else:
                out = l[i][1]
            if out in {0,1} and out != prevout:
                prevout = out
                outs +=1
            else:
                break
            if outs > 7:
                print(seed)
                sys.exit()
        i += inc
