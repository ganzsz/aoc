from pprint import pprint
import re
import time
from typing import List, Set, Tuple

def manhattanDistance(a, b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

def inBetween(x, h, l):
    return x<=h + 1 and x>=l - 1

def aInbetween(a,b):
    (a1, a2) = a
    (b1, b2) = b
    return inBetween(a1, b2, b1) or inBetween(a2, b2, b1)

def anyOverlap(a, b):
    (a1, a2) = a
    (b1, b2) = b
    return aInbetween(a,b) or aInbetween(b,a)

# maxRow = 20
maxRow = 4000000

def calcMissing(row:List[Tuple[int,int]]):
    x = max(row[0][0], row[1][0])
    return x-1


with open('/home/ubuntu/projects/advent-of-code/2022/15/input.real') as f:
    st = time.time()
    openRows:Set[int] = set([x for x in range(0, maxRow + 1)])
    blocked:List[List[Tuple[int, int]]] = [list() for _ in range(0, maxRow + 1)]

    lines = f.read().split('\n')
    for key, line in enumerate(lines):
        stline= time.time()
        m = re.match("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line)
        sx, sy, bx, by = [int(m.group(x)) for x in range(1,5)]
        sensor = sx, sy
        beacon = bx, by
        distance = manhattanDistance(sensor, beacon)
        for rowToTest in range(max(0, sy-distance), min(maxRow+1 ,sy+distance+1)):
            if rowToTest not in openRows: continue
            row = blocked[rowToTest]
            distFrom10 = sy - rowToTest if sy > rowToTest else rowToTest - sy
            row.append((max(0, sx - distance + distFrom10), min(maxRow, sx + distance - distFrom10)))
            if by == rowToTest and bx >= 0 and bx <= maxRow : row.append((bx, bx))
            i = 0
            while i < len(row):
                range1 = row[i]
                for k, range2 in enumerate(row):
                    if(k==i): continue
                    if(anyOverlap(range1, range2)):
                        row[min(i,k)] = (min(range1[0], range2[0]), max([range1[1], range2[1]]))
                        del row[max(i,k)]
                        i = -1
                        break
                i+=1
            if (0, maxRow) in row:
                openRows.remove(rowToTest)
        now = time.time()
        fullTime = now - st
        minutes = int(fullTime/60)
        minutes = str(minutes) if minutes > 10 else "0"+str(minutes)
        prettyTime = f"{minutes}:{fullTime % 60:2.5}"
        print(f"line {key+1 if key+1 > 9 else '0' + str(key+1)} took {now - stline:5.5} sec, total: {prettyTime}, dist:{distance}, lines left: {len(openRows)}")
        stline = now

    # I'm leaving this in so you can feel my pain as well
    # print("openrows", len(openRows))
    # singles = list()
    # mults = list()
    # [singles.append(x) if len(x) == 1 else mults.append(x) for x in blocked]
    # print([x for k,x in enumerate(blocked) if k in openRows ])
    # print("singles", len(singles))
    # foults = [x for x in singles if x[0][0]<=0 and x[0][1] >= maxRow]
    # print("foults", len(foults))
    # print (openRows)
    theRow = openRows.pop()
    x = calcMissing(blocked[theRow])
    y = theRow
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"result: {4000000*x+y}")

    print("Elapsed seconds:", time.time() - st)
