mods, poss = [], []
with open('15.txt') as f:
    for line in f:
        l = line.split()
        n = int(l[1][1])
        m = int(l[3])
        mods += [m]
        poss += [int(l[-1][:-1])+n % m]

#Part 2 additions
mods += [11]
poss += [7]
t = 0
while sum(poss):
    t += 1
    poss = [(p+1) % m for p, m in zip(poss,mods)]

print(t)
