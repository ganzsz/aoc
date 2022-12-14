from typing import Dict


def pointsOnLine(s,e):
    x0,y0 = s
    x1,y1 = e
    if x0 == x1:
        return [(x0,i) for i in range(min(y0,y1),max(y1,y0)+1)]
    if y0 == y1:
        return [(i,y0) for i in range(min(x0,x1),max(x0,x1)+1)]

def printPoints(points, limx, limy):
    for y in range(limy[0], limy[1]+1):
        screen[y] = {}
        for x in range(limx[0], limx[1]+1):
            screen[y][x] = '#' if (x,y) in points else ' '
        print(''.join(screen[y].values()))

with open('/home/ubuntu/projects/advent-of-code/2022/14/input.real') as f:
    points = set()
    xlim = 500,500
    ylim = 0,0
    for line in f.readlines():
        line = line.split(' -> ')
        for i in range(1, len(line)):
            x0,y0 = [int(x) for x in line[i-1].split(',')]
            x1,y1 = [int(x) for x in line[i].split(',')]
            mx = min(x0,x1)
            if mx < xlim[0]: xlim = mx, xlim[1]
            mx = max(x0,x1)
            my = max(y0,y1)
            if mx > xlim[1]: xlim = xlim[0], mx
            if my > ylim[1]: ylim = ylim[0], my
            [points.add(p) for p in pointsOnLine((x0,y0),(x1,y1))]
    screen: Dict[int, Dict[int,str]] = {}
    printPoints(points, xlim, ylim)
    number = 0
    while True:
        x = 500
        y = 0
        while True:
            if y > ylim[1]: break
            if (x,y+1) not in points:
                y+=1
                continue
            if (x-1,y+1) not in points:
                x-=1
                y+=1
                continue
            if (x+1,y+1) not in points:
                x+=1
                y+=1
                continue
            break
        if y > ylim[1]: break
        points.add((x,y))
        number += 1
        printPoints(points, xlim, ylim)
    print(number)


