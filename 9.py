def unpack(s):
    out = ''
    while len(s):
        if s[0] != '(':
            out += s[0]
            s = s[1:]
        else:
            i = s.find(')')
            a,b = [int(x) for x in s[1:i].split('x')]
            out += s[i+1:i+a+1]*b
            s = s[i+1+a:]
    return out

def length(s):
    l = 0
    while len(s):
        if s[0] != '(':
            l += 1
            s = s[1:]
        else:
            i = s.find(')')
            a,b = [int(x) for x in s[1:i].split('x')]
            l += length(s[i+1:i+a+1])*b
            s = s[i+1+a:]
    return l

with open('9.txt') as f:
    for line in f:
        print('Part 1: ', len(unpack(line.strip().replace(' ',''))))
        print('Part 2: ', length(line.strip().replace(' ','')))
