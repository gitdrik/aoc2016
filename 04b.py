from operator import itemgetter
idsum = 0
with open('04.txt') as f:
    for line in f:
        l = line.split('[')
        chk = l[1][:-2]
        n = int(l[0].split('-')[-1])
        cs = sorted(''.join(l[0].split('-')[:-1]))
        csn = []
        while cs:
            c = cs.pop(0)
            cn = 1
            while cs and cs[0] == c:
                cn += 1
                cs.pop(0)
            csn.append((c,cn))
        csn.sort(key=itemgetter(1),reverse=True)
        nchk = ''.join([c[0] for c in csn[0:5]])
        if nchk == chk:
            name = ''
            for c in l[0]:
                if c =='-':
                    name += ' '
                    continue
                name += chr(97 + (ord(c)-97+n)%26 )
            if 'north' in name:
                print(name[:-4], n)
