import json

def compNext(left, right):
  # next step
  if len(left) > 1 and len(right) > 1: return compareItems(left[1:], right[1:])
  # one of both will run out 
  # they deadlocked
  if len(left) == len(right) == 1: return None
  else:
    return len(left) < len(right)

def compEntry(left, right):
  if len(left) > 0 and len(right) > 0: return compareItems(left, right)
  else: return len(right) > len(left)


def compareItems(left, right):
  if type(left[0]) == type(right[0]):
    if type(left[0]) == int:
      if left[0] != right[0]: return left[0]<right[0]
      else: return compNext(left, right)
    else:
      if len(left[0]) > 0 and len(right[0]) > 0:
        comp = compareItems(left[0], right[0])
        if comp == None:
          return compNext(left, right)
        else:
          return comp
      else:
        return compNext(left[0], right[0])
  #one is int
  else:
    if type(left[0]) == int:
      left[0]=[left[0]]
    else:
      right[0]=[right[0]]
    return compareItems(left, right)



with open('/home/ubuntu/projects/advent-of-code/2022/13/input.real') as f:
    out = []
    i = 1
    for rawPair in f.read().split('\n\n'):
      left, right = [json.loads(x) for x in rawPair.split('\n')]
      comp = compEntry(left, right)
      if comp: out.append(i)
      i+=1
    print(sum(out))