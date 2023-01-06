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
  N, M, K = map(int, input().split(" "))
  EDGES = [set() for _ in range(2*N+10)]
  for _ in range(M):
    u, v, a = [int(x) for x in input().split(" ")]

    u, v = u-1, v-1
    if a == 0:
      u, v = u+N, v+N

    EDGES[u].add(v)
    EDGES[v].add(u)

  if K > 0:
    S = [int(x)-1 for x in input().split(" ")]
    for s in S:
      EDGES[s].add(s+N)
      EDGES[s+N].add(s)

  steps = [inf]*(2*N+10)
  steps[0] = 0
  deq = deque()
  deq.append(0)
  while deq:
    current = deq.popleft()
    if current == N-1 or current == 2*N-1: break
    for n in EDGES[current]:
      if steps[n] != inf: continue

      steps[n] = steps[current]
      if abs(n - current) != N:
        steps[n] += 1
        deq.append(n)
      else:
        deq.appendleft(n)


  ans = min(steps[N-1], steps[2*N-1])
  print(ans if ans != inf else -1)

resolve()
