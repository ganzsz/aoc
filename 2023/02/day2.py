from typing import List, Tuple
from pprint import pprint

class Game:
    def __init__(self, gameString:str) -> None:
        """Game 8: 3 green, 10 red, 15 blue; 1 green, 9 red; 9 blue, 2 green, 12 red"""
        rawgame, rawpicks = gameString.split(': ')
        self.gameId = int(rawgame.split(' ')[1])
        rawpicks = [g.split(', ') for g in rawpicks.split('; ')]
        self.picks: List[List[Tuple[str, int]]] = [[]]
        for game in rawpicks:
            pcs = []
            for p in game:
                n, c = p.split(' ')
                pcs.append((c, int(n)))
            self.picks.append(pcs)
    
    def maxPerColor(self):
        """Highest number per color,"""
        out = {"red": 0, "green": 0, "blue": 0}
        for p in self.picks:
            for c, n in p:
                if out[c] < n:
                    out[c] = n
        return out
    
    def __repr__(self) -> str:
        return "Game: " + str(self.gameId)
                


with open('input.real') as f:
    input = [Game(i.strip()) for i in f.readlines()]

part1 = 0
"""only 12 red cubes, 13 green cubes, and 14 blue cubes"""
for g in input:
    m = g.maxPerColor()
    if m['red'] > 12 or m['green'] > 13 or m['blue'] > 14: continue

    part1 += g.gameId

print("part1: " + str(part1))

part2 = 0
for g in input:
    m = g.maxPerColor()
    power = m['red'] * m['green'] * m['blue']
    part2 += power

print("part2: "+str(part2))