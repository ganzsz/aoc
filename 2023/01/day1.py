from pprint import pprint
import re


with open('input.real') as f:
    input = [r.strip() for r in  f.readlines()]

    repl = [
        ('one','1'),
        ('two','2'),
        ('three','3'),
        ('four','4'),
        ('five','5'),
        ('six','6'),
        ('seven','7'),
        ('eight','8'),
        ('nine','9')]
    

def clean(line: str):
    for (i, r) in repl:
        line = line.replace(i, i+r+i)
    return line

stripped = [clean(r) for r in input]

stripped = [re.sub('[a-z]+', '', r) for r in stripped]
print(sum([int(i[0] + i[-1]) for i in stripped]))