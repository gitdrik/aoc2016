n, s = 0, [1]
with open('18.txt') as f:
    for c in f.read().strip():
        if c == '.':
            s.append(1)
            n += 1
        else:
            s.append(0)
s.append(1)

for i in range(400000-1):
    ss = [1]
    for j in range(1,len(s)-1):
        if (s[j-1],s[j],s[j+1]) in [(0,0,1),(1,0,0),(0,1,1),(1,1,0)]:
            ss.append(0)
        else:
            ss.append(1)
            n += 1
    s = ss + [1]
print(n)
