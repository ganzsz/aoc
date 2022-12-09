from math import sqrt


addTuples = lambda a,b:(a[0]+b[0],a[1]+b[1])
subTuples = lambda a,b:(a[0]-b[0],a[1]-b[1])

moves = [(x, y) for x in range(-1,2) for y in range(-1,2)]

def calcDist(a,b):
    x,y = subTuples(a,b)
    return sqrt(x*x + y*y)


def followH(H, T):
    minDist = 2.0
    minMove = 0,0
    for move in moves:
        tt = addTuples(T, move)
        dist = calcDist(H, tt)
        if(dist == 0.0): return T
        if(dist < minDist):
            minDist = dist
            minMove = move
    return addTuples(T, minMove)


def getDelta(d):
    if   d == 'U': return (0, 1)
    elif d == 'D': return (0, -1)
    elif d == 'L': return (-1, 0)
    elif d == 'R': return (1, 0)


with open('/home/hans/Projects/aoc/2022/09/realinput') as f:
    rope = [(0,0) for _ in range(0,10)]
    visited = dupes = set()
    for line in f.readlines():
        d, a = line.strip().split()
        # print(d,a)
        a = int(a)
        for _ in range(0,a):
            delta = getDelta(d)
            rope[0] = addTuples(rope[0], delta)
            for i in range(1,len(rope)):
                H = rope[i-1]
                T = rope[i]
                T = followH(H, T)
                rope[i] = T
            if T not in visited: visited.add(T)
            # print(rope)
    print(len(visited))
