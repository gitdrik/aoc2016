data = [1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1]
#part 1: size = 272
size = 35651584
while len(data) < size:
    data += [0] + [int(not x) for x in data[::-1]]

data = data[:size]
while not len(data) % 2:
    data = [int(a == b) for a,b in zip(data[::2],data[1::2])]

print(''.join([str(x) for x in data]))
