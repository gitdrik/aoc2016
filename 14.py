import hashlib

salt = 'qzyelonm'
hs = []

for i in range(1000):
    s = salt+str(i)
    hs.append(hashlib.md5(s.encode()).hexdigest())

i = 0
keys = []
while len(keys) < 64:
    s = salt+str(i+1000)
    h = hashlib.md5(s.encode()).hexdigest()
    hs.append(h)
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
