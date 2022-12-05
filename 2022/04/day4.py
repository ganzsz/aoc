from pprint import pprint

def aOverB(a, b):
    (a1, a2) = a
    (b1, b2) = b
    return a1 <= b1 and a2 >= b2

def hasOverlap(a, b):
    return (aOverB(a,b) or aOverB(b,a))

def inBetween(x, h, l):
    return x<=h and x>=l

def aInbetween(a,b):
    (a1, a2) = a
    (b1, b2) = b
    return inBetween(a1, b2, b1) or inBetween(a2, b2, b1)

def anyOverlap(a, b):
    (a1, a2) = a
    (b1, b2) = b
    return aInbetween(a,b) or aInbetween(b,a)

with open('/home/ubuntu/projects/advent-of-code/2022/04/realinput') as f:
    lines = [[[int(p) for p in i.split('-')] for i in l.strip().split(',')] for l in f.readlines()]
    overlap = [(a,b) for (a,b) in lines if hasOverlap(a,b)]
    anyOverlap = [(a,b) for (a,b) in lines if anyOverlap(a,b)]
    print(len(overlap))
    pprint(len(anyOverlap))