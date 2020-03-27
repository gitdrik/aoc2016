def openSpace(x,y):
    n = x*x + 3*x + 2*x*y + y + y*y + 1352
    return (1 + sum([z == '1' for z in bin(n)[2:]])) % 2

q = [(1,1,0)]
seen = {(1,1)}
while q:
    (x, y, s) = q.pop(0)
    if (x, y) == (31, 39):
        print(s)
        break
    for (a, b) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if a >= 0 and b >= 0 and (a, b) not in seen and openSpace(a,b):
            seen.add((a,b))
            q.append((a,b,s+1))
