from pprint import pprint


with open('/home/ubuntu/projects/advent-of-code/2022/05/realinput') as f:
    stage = "fillStacks"
    stacks = [[] for x in range(9)]
    for readLine in f.readlines():
        if stage == "fillStacks":
            line = readLine[1:]
            if line[0] == '1':
                stage = "stackNumbers"
                continue

            i = 0
            while i*4 < len(line):
                char = line[i*4]
                if char != ' ': stacks[i].insert(0, char)
                i+=1
        elif stage == "stackNumbers":
            stage = "instructions"
            continue
        elif stage == "instructions":
            _, c, _, o, _, t = readLine.strip().split(' ')
            c = int(c)
            o = int(o) - 1
            t = int(t) - 1
            s = stacks[o][-c:]
            # s.reverse()
            del stacks[o][-c:]
            [stacks[t].append(i) for i in s]
    pprint("".join([i[-1] for i in stacks if len(i) > 0]))
