from pprint import pprint
import re


with open('input.real') as f:
    input = [r.strip() for r in  f.readlines()]


stripped = [re.sub('[a-z]+', '', r) for r in input]
print(sum([int(i[0] + i[-1]) for i in stripped]))