from functools import reduce
from math import gcd
from typing import List, Tuple



class Monkey():
    def __init__(self, lines:str):
        lines = [l.strip().split() for l in lines.splitlines()]
        self.number = int(lines[0][1][0:-1])
        self.holding = [int(i.strip(',')) for i in lines[1][2:]]
        self.operation = ' '.join(lines[2][1:])
        self.doOperation = lambda old: eval(' '.join(lines[2][3:]))
        self.divider = int(lines[3][3])
        self.true = int(lines[4][5])
        self.false = int(lines[5][5])
        self.inspections = 0
    
    def __repr__(self) -> str:
        return f'''
Monkey {self.number}:
  Starting items: {', '.join([str(i) for i in self.holding])}
  Operation: {self.operation}
  Test: divisible by {self.divider}
    If true: throw to monkey {self.true}
    If false: throw to monkey {self.false}'''

    def inspectItem(self, old:int, lc) -> Tuple[int, int]:
        new = self.doOperation(old) % lc + lc
        self.inspections += 1

        if new % self.divider == 0:
            return (self.true, new)
        else:
            return (self.false, new)

    def inspectItems(self, lc) -> List[Tuple[int, int]]:
        ret = list(map(lambda i:self.inspectItem(i, lc), self.holding))
        self.holding = []
        return ret

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

with open('/home/hans/Projects/aoc/2022/11/input.real') as f:
    monkeys = [Monkey(i) for i in f.read().split('\n\n')]
    lc = lcm([m.divider for m in monkeys])
    print(monkeys)
    for r in range(0, 10000):
        if r%100 == 0:
            print(str(r/100)+"%")
        # print('round',r+1)
        for throwing in monkeys:
            updates = throwing.inspectItems(lc)
            # print(throwing.number,updates)
            [monkeys[id].holding.append(item) for id, item in updates]
        # print([(m.number,m.inspections) for m in monkeys], '\n')
        if r%1000 == 0:
            print([m.inspections for m in monkeys])
    inspections = [m.inspections for m in  monkeys]
    inspections.sort()
    print(inspections[-1]*inspections[-2])