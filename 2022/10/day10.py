instructionSet = {
    'addx': (lambda x,v:x+v, 2),
    'noop': (lambda x,v:x, 1)
}


def printTerm(term):
    for r in term:
        print(r)


with open('/home/hans/Projects/aoc/2022/10/input.real') as f:
    regX = 1
    cycle = 1
    rowPos = 0
    term = [""]
    row = 0
    for r in f.readlines():
        r = r.strip().split()
        for _ in range(0, instructionSet[r[0]][1]):
            if rowPos in range(regX-1, regX+2):
                term[row] += '#'
            else:
                term[row] += '.'

            if (cycle) % 40 == 0:
                rowPos = -1
                row+=1
                term.append('')
            cycle += 1
            rowPos += 1
        regX = instructionSet[r[0]][0](regX, int(r[1]) if len(r)>1 else None )
    printTerm(term)

