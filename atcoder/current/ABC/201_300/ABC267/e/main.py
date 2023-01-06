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
  from heapq import heappop, heappush

  # 何回呼ばれるかが変わってくる。
  # 現状のコストが大きいものを愚直に削除していけばよさそう。
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  EDGES = [[] for _ in range(N)]
  current_cost = [0]*N
  for _ in range(M):
    u, v = [int(x)-1 for x in input().split(" ")]
    EDGES[u].append(v)
    EDGES[v].append(u)
    current_cost[u] += A[v]
    current_cost[v] += A[u]

  costs = []
  for i in range(N):
    heappush(costs, (current_cost[i], i))

  ans = 0
  checked = set()
  for _ in range(N):
    while costs[0][1] in checked:
      _ = heappop(costs)
    cost, i = heappop(costs)
    checked.add(i)
    ans = max(ans, cost)
    for e in EDGES[i]:
      if e in checked: continue
      current_cost[e] -= A[i]
      heappush(costs, (current_cost[e], e))
  print(ans)

resolve()