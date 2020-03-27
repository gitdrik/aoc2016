import hashlib

salt = 'qzyelonm'
hs = []

def stretch(s):
    for i in range(2017):
        s = hashlib.md5(s.encode()).hexdigest()
    return s

for i in range(1000):
    hs.append(stretch(salt+str(i)))

i = 0
keys = []
while len(keys) < 64:
    hs.append(stretch(salt+str(i+1000)))
    g = hs.pop(0)
    for j, c in enumerate(g[:-2]):
        if g[j:j+3] == c*3:
            for f in hs:
                if c*5 in f:
                    print(i)
                    keys.append(i)
                    break
            break
    i = i+1
