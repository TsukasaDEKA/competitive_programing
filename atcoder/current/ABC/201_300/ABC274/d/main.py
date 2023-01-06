import sys
sys.setrecursionlimit(500*500)

from math import gcd
from functools import reduce
# product('ABCD', repeat=2) => AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
from itertools import product
# permutations('ABCD', 2) => AB AC AD BA BC BD CA CB CD DA DB DC
from itertools import permutations
# combinations('ABCD', 2) => AB AC AD BC BD CD
from itertools import combinations
from itertools import accumulate # 累積和作るやつ
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush
from bisect import bisect_left
# 0埋めされた二進数表現
f'{9:05b}'

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)
popcnt = lambda x: bin(x).count("1")

dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]
dh8 = [-1, -1, -1,  0,  0,  1,  1,  1]
dw8 = [-1,  0,  1, -1,  1, -1,  0,  1]

def resolve():
  # DP パターンはそんなにない。
  inf = 10**18+1
  N, x, y = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  # x だけ判定
  next_ = set()
  next_.add(A[0])
  for i in range(2, N, 2):
    a = A[i]
    current = set()
    for x_ in next_:
      current.add(x_ + a)
      current.add(x_ - a)
    next_ = current

  if x not in next_:
    print("No")
    return

  next_ = set()
  next_.add(0)
  for i in range(1, N, 2):
    a = A[i]
    current = set()
    for x_ in next_:
      current.add(x_ + a)
      current.add(x_ - a)
    next_ = current

  if y not in next_:
    # print("No", next_)
    print("No")
    return

  print("Yes")

resolve()
