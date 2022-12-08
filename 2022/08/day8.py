from math import prod
from pprint import pprint
from typing import List


with open('/home/chiron/personal/advent-of-code/2022/08/realinput') as f:
  file = [x.strip() for x in f.readlines()]
  rows = []
  cols = [[] for _ in range(0,len(file))]

  for row in file:
    rows.append([int(x) for x in row])
    for i in range(0,len(row)):
      cols[i].append(int(row[i]))

  '''
    day1
  '''
  def top(data:List[int], index:int) -> bool:
    c = data[index]
    slices = [data[0:index], data[index+1:]]
    top =  True in set(map(lambda l: max(l) < c, slices))
    return top

  def highest(lists:List[List[int]], indexes:List[int]) -> bool:
    return True in set(map(lambda l,i:top(l, i),lists,indexes))

  l = len(rows[0])
  ra = range(1,l-1)
  r = sum([sum(list(map(lambda x:highest([rows[x], cols[y]],[y,x]),ra))) for y in ra])
  edges = (l-1)*4
  print(r+edges)

  def firstHit(data:List[int], height:int) -> int:
    for i in range(0,len(data)):
      if height <= data[i]: return i+1
    return len(data)

  def firstHits(data:List[int], index:int) -> int:
    c = data[index]
    l = data[0:index]
    l.reverse()
    r=data[index+1:]
    hits = list(map(lambda i:firstHit(i, c),[l,r]))
    return prod(hits)
  
  def hits(lists:List[List[int]], indexes:List[int]) -> int:
    return prod(list(map(lambda l,i: firstHits(l,i),lists, indexes)))
  
  r = max([max(list(map(lambda x:hits([rows[x], cols[y]],[y,x]),ra))) for y in ra])
  print(r)