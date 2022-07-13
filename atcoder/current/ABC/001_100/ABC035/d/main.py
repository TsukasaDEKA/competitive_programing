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
  # 目標とする町を決めて、そこまで一直線で向かい、
  # その町に T - (移動時間) 分滞在してから戻ってくるのが最適。
  # 移動時間をどうやって求めるかが問題。
  # 行きは普通に dijkstra なりなんなりすれば良い。
  # 帰りに工夫が必要で、全ての辺を逆向きに付けて dijkstra する。
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

  inf = 10**18+1
  N, M, T = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  EDGES = [set() for _ in range(N)]
  REV_EDGES = [set() for _ in range(N)]
  for _ in range(M):
    a, b, c = [int(x)-1 for x in input().split(" ")]
    c += 1
    EDGES[a].add((c, b))
    REV_EDGES[b].add((c, a))

  to_ = [inf]*N
  from_ = [inf]*N
  dijkstra(0, to_, EDGES)
  dijkstra(0, from_, REV_EDGES)

  ans = max(A[i]*(T-(to_[i]+from_[i])) for i in range(N))

  print(ans)

resolve()