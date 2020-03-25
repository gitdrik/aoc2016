import math
import copy
import collections

def go(floor, steps, minsteps, pairs, hist):
    
    # om vi gått för långt
    if steps >= minsteps:
        return hist, math.inf
    # om det skiter sig
    genfloors = set([x[0] for x in pairs])
    for p in pairs:
        if p[0]!=p[1] and p[1] in genfloors:
            return hist, math.inf

    # om historien upprepar sig utan att det blivit bättre
    phash = frozenset({(a,b,c) for (a,b),c in collections.Counter(pairs).items()})
    if phash in hist and hist[phash] <= steps:
        return hist, math.inf
    hist[phash] = steps

    # om vi är klara
    if phash == {(3,3,len(pairs))}:
        return hist, steps

    # annars, gå vidare
    gens = [i for i,(g,m) in enumerate(pairs) if g == floor]
    mics = [i for i,(g,m) in enumerate(pairs) if m == floor]
    for newfloor in [x for x in range(3,-1,-1) if abs(floor-x)==1]:
        #print(pairs, gens, mics, newfloor)
        for i, g1 in enumerate(gens):
            newps = copy.deepcopy(pairs)
            newps[g1] = (newfloor,newps[g1][1])
            hist, ns = go(newfloor, steps+1, minsteps, newps, hist)
            minsteps = min(minsteps, ns)
            if pairs[g1][1] == floor:
                newps[g1] = (newfloor, newfloor)
                hist, ns = go(newfloor, steps+1, minsteps, newps, hist)
                minsteps = min(minsteps, ns)
            for g2 in gens[i+1:]:
                newps = copy.deepcopy(pairs)
                newps[g1] = (newfloor,newps[g1][1])
                newps[g2] = (newfloor,newps[g2][1])
                hist, ns = go(newfloor, steps+1, minsteps, newps, hist)
                minsteps = min(minsteps, ns)
        for i, m1 in enumerate(mics):
            newps = copy.deepcopy(pairs)
            newps[m1] = (newps[m1][0], newfloor)
            hist, ns = go(newfloor, steps+1, minsteps, newps, hist)
            minsteps = min(minsteps, ns)
            for m2 in mics[i+1:]:
                newps = copy.deepcopy(pairs)
                newps[m1] = (newps[m1][0], newfloor)
                newps[m2] = (newps[m2][0], newfloor)
                hist, ns = go(newfloor, steps+1, minsteps, newps, hist)
                minsteps = min(minsteps, ns)

    return hist, minsteps

# (genfloor, microchipfloor) order is co, po, pr, ru, th
pairs = [(0, 0), (0, 1), (0, 1), (0, 0), (0, 0)]
hist, steps = go(0,0,100,pairs,{})
print('Part 1: ',steps)

pairs = [(0, 0), (0, 1), (0, 1), (0, 0), (0, 0), (0, 0), (0, 0)]
hist, steps = go(0,0,100,pairs,{})
print('Part 2: ',steps)
