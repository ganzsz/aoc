from pprint import pprint


winners = {'A':'B', 'B':'C', 'C':'A'}
losers = {'A':'C', 'B':'A', 'C':'B'}
scores = {'A':1, 'B':2, 'C':3}
mappings = {'X':'A', 'Y':'B', 'Z':'C'}
score = 0

def getScoreOne(t, m):
    return getScore(t, mappings[m])

def getScore(t, m):
    if(winners[t] == m): return 6 + scores[m]
    return (0 if losers[t] == m else 3) + scores[m]

def getScoreTwo(t, m):
    if  (m == 'X'): return getScore(t, losers[t])
    elif(m == 'Y'): return getScore(t,t)
    elif(m == 'Z'): return getScore(t, winners[t])

with open('/home/ubuntu/projects/advent-of-code/2022/02/realInput') as f:
    lines = [l.strip('\n').split(' ') for l in f.readlines()]
    print(sum(
        getScoreOne(t, m)
        for t, m in lines
    ))
    print(sum(
        getScoreTwo(t, m)
        for t, m in lines
    ))