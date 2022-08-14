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
  from collections import deque
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  P = deque([int(x) for x in input().split(" ")])
  if K == 0:
    print(*P)
    return

  deleted = set()
  max_ = N
  for _ in range(K):
    while P[-1] in deleted:
      _ = P.pop()

    if P[0] > P[-1]:
      v = P.pop()
      P.appendleft(v)
    else:
      deleted.add(max_)
      max_-=1
  ans = [p for p in P if p not in deleted]
  print(*ans)

resolve()