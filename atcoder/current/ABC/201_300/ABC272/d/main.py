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
  N, M = map(int, input().split(" "))
  ans = [[inf]*N for _ in range(N)]
  ans[0][0] = 0
  M2 = M**2
  diffs = []
  for i in range(N+1):
    for j in range(N+1):
      if i**2 + j**2 == M:
        # print(i, j, M2)
        diffs.append((i, j))
        diffs.append((-i, j))
        diffs.append((i, -j))
        diffs.append((-i, -j))
  
  nexts = deque()
  nexts.append((0, 0))
  while nexts:
    i, j = nexts.popleft()
    count = ans[i][j]
    for di, dj in diffs:
      i_ = i+di
      j_ = j+dj
      if i_ < 0 or i_ >= N or j_ < 0 or j_ >= N: continue
      if ans[i_][j_] != inf: continue
      ans[i_][j_] = count + 1
      nexts.append((i_, j_))

  for a in ans:
    print(*[n if n != inf else -1 for n in a])

resolve()
