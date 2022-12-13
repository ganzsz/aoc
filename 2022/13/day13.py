import json
from typing import List

def compareItems(left, right):
  # print(left, right)
  if len(left) == 0 and len(right) > 0: return True
  l = left[0]
  r = right[0]
  if type(l) == type(r):
    if type(l) == int:
      if l != r: return left < right
      else: return compareItems(left[1:], right[1:])
    else: return compareItems(left[1], right[1])
  
  if type(left) == List:
    right[0] = [r]
  else:
    left[0] = [l]
  return compareItems(left,right)


  



with open('/home/chiron/personal/advent-of-code/2022/13/input.test') as f:
    for rawPair in f.read().split('\n\n'):
      left, right = [json.loads(x) for x in rawPair.split('\n')]
      print(left, right)
      print(compareItems(left,right))