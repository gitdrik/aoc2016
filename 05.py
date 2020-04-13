import hashlib

id = 'abbhdwsy'
code = ''
i = 0
while len(code) < 8:
    s = id+str(i)
    hash = hashlib.md5(s.encode())
    if hash.hexdigest()[:5] == '00000':
        code = code+hash.hexdigest()[5]
        print(code)
    i += 1
