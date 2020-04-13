def abba(s):
    for i in range(len(s)-3):
        a,b,c,d = s[i:i+4]
        if a != b and a == d and b == c:
            return True
    return False

def ababab(l):
    for w in l[::2]:
        for i in range(len(w)-2):
            a,b,c = w[i:i+3]
            if a != b and a == c:
                for v in l[1::2]:
                    for j in range(len(v)-2):
                        d,e,f = v[j:j+3]
                        if d == b and f == b and e == a:
                            return True
    return False

tls = 0
ssl = 0
with open('07.txt') as f:
    for line in f:
        l = line.strip().replace('[',']').split(']')
        if any([abba(x) for x in l[::2]]) and not any([abba(x) for x in l[1::2]]):
            tls += 1
        if ababab(l):
            ssl += 1
print('TLS: ',tls)
print('SSL: ',ssl)
