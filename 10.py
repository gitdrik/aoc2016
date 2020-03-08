def runbot(bot, bots, outs):
    if len(bots[bot]['chips']) == 2:
        a, b = bots[bot]['chips']
        if 61 in {a,b} and 17 in {a,b}:
            print('Part 1:', bot)
        if 'high' in bots[bot]:
            if bots[bot]['high'][0] == 'bot':
                nbot = bots[bot]['high'][1]
                if nbot not in bots:
                    bots[nbot] = {'chips':set()}
                bots[bot]['chips'].remove(max(a,b))
                bots[nbot]['chips'].add(max(a,b))
                bots, outs = runbot(nbot, bots, outs)
            else:
                out = bots[bot]['high'][1]
                if out not in outs:
                    outs[out] = []
                bots[bot]['chips'].remove(max(a,b))
                outs[out].append(max(a,b))
        if 'low' in bots[bot]:
            if bots[bot]['low'][0] == 'bot':
                nbot = bots[bot]['low'][1]
                if nbot not in bots:
                    bots[nbot] = {'chips':set()}
                bots[bot]['chips'].remove(min(a,b))
                bots[nbot]['chips'].add(min(a,b))
                bots, outs = runbot(nbot, bots, outs)
            else:
                out = bots[bot]['low'][1]
                if out not in outs:
                    outs[out] = []
                bots[bot]['chips'].remove(min(a,b))
                outs[out].append(min(a,b))
    return bots, outs

bots = {}
outs = {}
with open('10.txt') as f:
    for line in f:
        l = line.strip().split(' ')
        if l[0] == 'bot':
            bot = int(l[1])
            if bot not in bots:
                bots[bot] = {'chips':set()}
            bots[bot]['low'] = [l[5], int(l[6])]
            bots[bot]['high'] = [l[10], int(l[11])]
            bots, outs = runbot(bot, bots, outs)
        else:
            bot = int(l[5])
            if bot not in bots:
                bots[bot] = {'chips':set()}
            bots[bot]['chips'].add(int(l[1]))
            bots, outs = runbot(bot, bots, outs)

print('Part 2:', outs[0][0]*outs[1][0]*outs[2][0])
