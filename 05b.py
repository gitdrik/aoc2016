import hashlib

id = 'abbhdwsy'
code = '________'
i = 0
digs = 0

while digs < 8:
    s = id+str(i)
    hash = hashlib.md5(s.encode())
    if hash.hexdigest()[:5] == '00000':
        pos = hash.hexdigest()[5]
        if pos in '01234567':
            p = int(pos)
            if code[p]=='_':
                code = code[:p] + hash.hexdigest()[6] + code[(p+1):]
                digs += 1
                print(code)
    i += 1
