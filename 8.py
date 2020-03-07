import copy
display = [[0]*50,[0]*50,[0]*50,[0]*50,[0]*50,[0]*50]

with open('8.txt') as f:
    for line in f:
        l = line.strip().replace('x=','').replace('y=','').replace('x',' ').replace('by ','').split(' ')
        a, b = int(l[-2]), int(l[-1])
        if l[0] == 'rect':
            for i in range(b):
                display[i] = [1]*a + display[i][a:]
        elif l[1] == 'row':
            display[a] = display[a][-b:] + display[a][:-b]
        else:
            newdisplay = copy.deepcopy(display)
            for i in range(6):
                newdisplay[i][a] = display[(i-b)][a]
            display = newdisplay

print(sum([sum(x) for x in display]))

for i in range(6):
    for j in range(50):
        if display[i][j]:
            print('O',end='')
        else:
            print(' ',end='')
    print('')
