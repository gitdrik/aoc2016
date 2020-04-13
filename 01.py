with open('01.txt') as f:
    moves = f.read().strip().split(',')
    moves = [x.strip() for x in moves]

# moves = ['R5', 'L5', 'R5', 'R3']
# part 2 is not 242

x = 0
y = 0
dir = 0
places = {(0,0)}
done = 0

for m in moves:
#    print(x,y,dir,m)
    if done: break
    if m[0] == 'R':
        dir = (dir+1) % 4
    else:
        dir = (dir-1) % 4

    n = int(m[1:])
    for i in range(n):
        if dir == 0:
            y += 1
        elif dir == 1:
            x += 1
        elif dir == 2:
            y -= 1
        else:
            x -= 1
        if (x,y) in places:
            done = 1
            break
        places.add((x,y))

print(x,y,abs(x)+abs(y))
