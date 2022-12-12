import multiprocessing
from pprint import pprint
import sys
from typing import Dict
from dijkstra import Link, dijkstra, multiplicationFactor, Node

def heightDiff(a,b):
    az = 'abcdefghijklmnopqrstuvwxyz'
    a = az.find(a)
    b = az.find(b)
    return b-a

def idFromPos(pos):
    y,x = pos
    return multiplicationFactor * y + x

def ignoreSpecial(c):
    if(c == 'S'): return 'a'
    if(c == 'E'): return 'z'
    return c

with open('/home/ubuntu/projects/advent-of-code/2022/12/input.real') as f:
    world = [l.strip() for l in f.readlines()]
    nodes :Dict[int, Node] = {}
    start = (0,0)
    end = (0,0)
    alist = []
    for y, row in enumerate(world):
        for x, char in enumerate(row):
            if char == 'S':
                start = (y,x)
                char = 'a'
            elif char == "E":
                end = (y,x)
                char = 'z'

            id = y*multiplicationFactor + x
            nodes[id] = Node(id)

            if char == 'a':
                alist.append(id)

            if y != 0:
                other = ignoreSpecial(world[y-1][x])
                diff = heightDiff(char, other) + 1
                if diff < 3:
                    nodes[id].links.append(Link(nodes[id - multiplicationFactor], 1))
                diff = heightDiff(other, char) + 1
                if diff < 3:
                    nodes[id - multiplicationFactor].links.append(Link(nodes[id], 1))
            if x != 0:
                other = ignoreSpecial(world[y][x-1])
                diff = heightDiff(char, other) + 1
                if diff < 3:
                    nodes[id].links.append(Link(nodes[id - 1], 1))
                diff = heightDiff(other, char) + 1
                if diff < 3:
                    nodes[id - 1].links.append(Link(nodes[id], 1))
    outputs = []
    def lookupSquare(a):
        global outputs
        d = dijkstra(nodes, nodes[a], nodes[idFromPos(end)])
        return d
    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(processes=4)
    alen = len(alist)
    for i, r in enumerate(pool.imap_unordered(lookupSquare, alist), 1):
        sys.stderr.write('\rdone {0:%}'.format(i/alen))
        outputs.append(r)
    print()
    print(min(outputs))