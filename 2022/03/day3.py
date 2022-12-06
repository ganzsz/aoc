'''
 I WROTE THIS ON MY PHONE
'''

from pprint import pprint

scores = "#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index

def findSingles(b):
    seen = set()
    seen_once = set()
    for x in b:
        if x in seen:
            seen_once.discard(x)
        else:
            seen.add(x)
            seen_once.add(x)
    return list(seen)

def findDupes(a,b):
    sa = findSingles(a)
    sb = findSingles(b)
    return [x for x in sa if x in sb]


with open('realinput') as f:
    lines = []
    full = []
    for line in f.readlines():
        l=line.strip()
        mid = int(len(l)/2)
        lines.append((
            l[0:mid],
            l[mid:]
        ))
        full.append(l)
    dupes = []
    for (a,b) in lines:
        dupes.append(
            [x for x in b if x in a][0]
        )
    print(sum([scores(d) for d in dupes]))
    i=0
    out=0
    while i < len(full):
        out = out + scores(findDupes(findDupes(full[i], full[i+1]), full[i+2])[0])
        i = i+3
    print(out)