from pprint import pprint


with open('/home/chiron/personal/advent-of-code/2022/01/input') as f:
    file = f.read()
    f.close()

persons = file.split('\n\n')

perPerson = [sum([int(i) for i in p.split('\n')]) for p in persons]

totalTop = 0

for i in range(0, 3):
    totalTop += max(perPerson)
    perPerson.remove(max(perPerson))

print(totalTop)