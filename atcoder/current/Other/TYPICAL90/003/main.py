import sys
from tabnanny import check
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
  # 木の半径 + 1 が答え
  N = int(input())
  EDGES = [[] for _ in range(N)]
  for _ in range(N-1):
    a, b = [int(x)-1 for x in input().split(" ")]
    EDGES[a].append(b)
    EDGES[b].append(a)
  que = deque([0])
  left = 0
  steps = [-1]*N
  steps[0] = 0
  max_step = 0
  while que:
    current = que.popleft()
    for n in EDGES[current]:
      if steps[n] >= 0: continue
      steps[n] = steps[current]+1
      if max_step < steps[n]:
        left = n
        max_step = steps[n]
      que.append(n)
  
  que.append(left)
  steps = [-1]*N
  steps[left] = 0
  d = 0
  while que:
    current = que.popleft()
    for n in EDGES[current]:
      if steps[n] >= 0: continue
      steps[n] = steps[current]+1
      if d < steps[n]:
        d = steps[n]
      que.append(n)

  print(d+1)

resolve()