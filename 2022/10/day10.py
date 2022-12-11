instructionSet = {
    'addx': (lambda x,v:x+v, 2),
    'noop': (lambda x,v:x, 1)
}


with open('/home/hans/Projects/aoc/2022/10/input.real') as f:
    regX = 1
    cycle = 0
    out = 0
    for r in f.readlines():
        r = r.strip().split()
        for _ in range(0, instructionSet[r[0]][1]):
            cycle += 1
            if cycle == 20 or (cycle-20) % 40 == 0:
                out += cycle * regX
        regX = instructionSet[r[0]][0](regX, int(r[1]) if len(r)>1 else None )
    print(out)
