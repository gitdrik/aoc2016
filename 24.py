import math

m =[]
ns = {}
with open('24.txt') as f:
    for y, line in enumerate(f):
        l = line.strip()
        m.append(l)
        for x, c in enumerate(l):
            if c in {'0','1','2','3','4','5','6','7'}:
                ns[int(c)] = (y,x)
nsteps = {}
for i in range(8):
    for j in range(i+1,8,1):
        q = [(*ns[i],0)]
        seen = set(ns[i])
        while q:
            (y,x,steps) = q.pop(0)
            if (y,x) == ns[j]: break
            for (yn, xn) in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
                if (yn,xn) not in seen and m[yn][xn] != '#':
                    seen.add((yn,xn))
                    q.append((yn,xn,steps+1))
        nsteps[(i,j)] = steps
        nsteps[(j,i)] = steps

def spath(start, rest, steps, minsteps):
    if len(rest)==1:
        last = rest.pop()
        #part 1: return steps+nsteps[(start,last)]
        return steps+nsteps[(start,last)]+nsteps[(last,0)]
    for n in rest:
        minsteps = min(minsteps,
                       spath(n,rest-{n},steps+nsteps[(start,n)],minsteps))
    return minsteps

print(spath(0, {1,2,3,4,5,6,7}, 0, math.inf))
