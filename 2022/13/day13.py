import copy
import functools
import json

def compNext(left, right):
  # next step
  if len(left) > 1 and len(right) > 1: return compareItems(left[1:], right[1:])
  # one of both will run out 
  # they deadlocked
  if len(left) == len(right): return None
  else:
    return len(left) < len(right)

def compEntry(left, right):
  left = copy.deepcopy(left)
  right = copy.deepcopy(right)
  if len(left) > 0 and len(right) > 0: return compareItems(left, right)
  else: return  len(left)<len(right)

def compSort(left, right):
  if compEntry(left, right): return -1
  else: return 1

def compareItems(left, right):
  if type(left[0]) == type(right[0]):
    if type(left[0]) == int:
      if left[0] != right[0]: return left[0]<right[0]
      else: return compNext(left, right)
    else:
      if len(left[0]) > 0 and len(right[0]) > 0:
        comp = compareItems(left[0], right[0])
      else:
        comp = compNext(left[0], right[0])
      if comp == None:
        return compNext(left, right)
      else:
        return comp
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
    everything = [[[2]],[[6]]]
    for rawPair in f.read().split('\n\n'):
      left, right = [json.loads(x) for x in rawPair.split('\n')]
      everything.append(left)
      everything.append(right)
      comp = compEntry(left, right)
      if comp: out.append(i)
      i+=1
    print(sum(out))
    sor = sorted(everything, key=functools.cmp_to_key(compSort))
    [print(s) for s in sor]
    indexes = [k+1 for k in range(0, len(sor)) if sor[k] in [[[2]], [[6]]]]
    print(indexes, indexes[0]*indexes[1])