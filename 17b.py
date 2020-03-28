from hashlib import md5

def openDoors(path):
    s = md5(('vkjiggvb'+path).encode()).hexdigest()
    od = ''
    if s[0] in 'bcdef': od += 'U'
    if s[1] in 'bcdef': od += 'D'
    if s[2] in 'bcdef': od += 'L'
    if s[3] in 'bcdef': od += 'R'
    return od

q = [(0,0,'')]
while q:
    (x, y, path) = q.pop(0)
    ods = openDoors(path)
    for (a, b, p) in [(x,y-1,'U'),(x,y+1,'D'),(x-1,y,'L'),(x+1,y,'R')]:
        if a in range(4) and b in range(4) and p in ods:
            if (a,b) == (3,3):
                l = len(path)+1
            else:
                q.append((a,b,path+p))
print(l)
