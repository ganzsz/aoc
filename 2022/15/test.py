import time
from typing import List, Tuple


# l = set()
# st = time.time()
# [l.add(x) for x in range(0,4000000)]
# print("adding sec:", time.time() - st)
# st = time.time_ns()
# l.remove(1234)
# print("removing ns", time.time_ns() - st)
# st = time.time_ns()
# 1234 in l
# print("searching ns", time.time_ns() - st)

# l = [x for x in range(0,5)]
# for k, v in enumerate(l):
#     r= l[k]
#     if k == 1:
#         del l[2]
#         r = 7
# print(l)

# a = (1,2)
# b = (4,3)
# c = (1,2)
# print("a=b" if a==b else "a!b")
# print("a=c" if a == c else "a!c")

blocked:List[List[Tuple[int, int]]] = [list() for _ in range(0, 20 + 1)]