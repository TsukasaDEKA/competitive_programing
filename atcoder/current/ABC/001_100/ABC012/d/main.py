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
  inf = 10**18+1
  from heapq import heappop, heappush
  def dijkstra(start, dist, path):
    dist[start] = 0
    candidate = [(0, start)]

    while candidate:
      cost, i = heappop(candidate)
      if cost > dist[i]: continue

      for c, j in path[i]:
        if cost+c >= dist[j]: continue
        dist[j] = cost+c
        heappush(candidate, (cost+c, j))

  N, M = map(int, input().split(" "))
  EDGES = [[] for _ in range(N)]
  for _ in range(M):
    a, b, t = [int(x) for x in input().split(" ")]
    a -= 1
    b -= 1
    EDGES[a].append((t, b))
    EDGES[b].append((t, a))

    
  ans = inf
  for i in range(N):
    dist = [inf]*N
    dijkstra(i, dist, EDGES)
    ans = min(ans, max(dist))
  print(ans)

resolve()