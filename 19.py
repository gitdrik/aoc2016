import collections

n = 3018458
start = 1
step = 1
while start <= n:
    w = start
    if (1+(n-start)//step) % 2:
        start = start + step*2
    step = step*2
print('Part1: ',w)

p = 0
es = collections.deque([x for x in range(1,n+1)])
es.rotate(-(n//2-1))
while len(es) > 1:
    if len(es)%2 == 0:
        es.rotate(-1)
    es.popleft()
print('Part 2: ', es[0])
