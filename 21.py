pwd = 'abcdefgh'
ls = []
with open('21.txt') as f:
    for line in f:
        l = line.strip().split()
        ls.append(l)
        if l[0] == 'swap':
            if l[1] == 'position':
                x, y = int(l[2]), int(l[5])
                a = pwd[x]
                b = pwd[y]
            else:
                a, b = l[2], l[5]
            pwd = pwd.replace(a, 'x')
            pwd = pwd.replace(b, a)
            pwd = pwd.replace('x', b)
        elif l[0] == 'reverse':
            a, b = int(l[2]), int(l[4])
            if a == 0:
                pwd = pwd[b::-1] + pwd[b+1:]
            else:
                pwd = pwd[:a] + pwd[b:a-1:-1] + pwd[b+1:]
        elif l[0] == 'rotate':
            if l[1] == 'left':
                a = int(l[2])
            elif l[1] == 'right':
                a = -int(l[2])
            else:
                a = pwd.find(l[6])
                if a >= 4:
                    a +=1
                a = -((a+1) % len(pwd))
            pwd = pwd[a:] + pwd[:a]
        elif l[0] == 'move':
            a, b = int(l[2]), int(l[5])
            c = pwd[a]
            pwd = pwd[:a] + pwd[a+1:]
            pwd = pwd[:b] + c + pwd[b:]
print('Part 1: ',pwd)

pwd = 'fbgdceah'
for l in ls[::-1]:
    if l[0] == 'swap':
        if l[1] == 'position':
            x, y = int(l[2]), int(l[5])
            a = pwd[x]
            b = pwd[y]
        else:
            a, b = l[2], l[5]
        pwd = pwd.replace(a, 'x')
        pwd = pwd.replace(b, a)
        pwd = pwd.replace('x', b)
    elif l[0] == 'reverse':
        a, b = int(l[2]), int(l[4])
        if a == 0:
            pwd = pwd[b::-1] + pwd[b+1:]
        else:
            pwd = pwd[:a] + pwd[b:a-1:-1] + pwd[b+1:]
    elif l[0] == 'rotate':
        if l[1] == 'left':
            a = -int(l[2])
        elif l[1] == 'right':
            a = int(l[2])
        else:
            a = pwd.find(l[6])
            if a in [2,4,6]:
                a = a//2+5
            else:
                a = a//2+1
        pwd = pwd[a:] + pwd[:a]
    elif l[0] == 'move':
        b, a = int(l[2]), int(l[5])
        c = pwd[a]
        pwd = pwd[:a] + pwd[a+1:]
        pwd = pwd[:b] + c + pwd[b:]
print('Part 2: ',pwd)
