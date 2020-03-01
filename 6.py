import collections

msg = ['','','','','','','','']
with open('6.txt') as f:
    for line in f:
        for i, c in enumerate(line.strip()):
            msg[i] += c

m1 = ''.join([collections.Counter(s).most_common(1)[0][0] for s in msg])
m2 = ''.join([collections.Counter(s).most_common()[-1][0] for s in msg])

print('Part 1: ',m1)
print('Part 2: ',m2)
