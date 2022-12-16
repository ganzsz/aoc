import re

def manhattanDistance(a, b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

rowToTest = 2000000


with open('/home/ubuntu/projects/advent-of-code/2022/15/input.real') as f:
    sensors = list()
    onRow10 = set()
    beaconOnRow10 = set()
    lines = f.read().split('\n')
    for key, line in enumerate(lines):
        print("TODO: ", len(lines) - key)
        m = re.match("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line)
        sx, sy, bx, by = [int(m.group(x)) for x in range(1,5)]
        sensor = sx, sy
        beacon = bx, by
        if by == rowToTest and bx not in beaconOnRow10: beaconOnRow10.add(bx)
        distance = manhattanDistance(sensor, beacon)
        if abs(sy - rowToTest) < distance:
            distFrom10 = sy - rowToTest if sy > rowToTest else rowToTest - sy
            [
                onRow10.add(x)
                for x in range(sx - distance + distFrom10, sx + distance - distFrom10 + 1)
                if x not in onRow10
            ]
    [onRow10.remove(x) for x in beaconOnRow10]
    print(len(onRow10))
