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
  mod = 10**9+7
  N = int(input())

  # EDGES[n]: 頂点 n に繋がっている頂点
  EDGES = [[] for _ in range(N)]
  for _ in range(N-1):
    x, y = [int(x)-1 for x in input().split(" ")]
    EDGES[x].append(y)
    EDGES[y].append(x)

  # checked[n]: 頂点 n が既にチェックされているかどうか
  checked = [False]*N
  checked[0] = True

  # parents[n]: 頂点 n の親。根の親は -1 になる。
  parents = [-1]*N

  # dp[n][c] := 頂点 n が c 色のケースのパターン数
  dp = [[1, 1] for _ in range(N)]

  # DFS をやっていく。
  # 帰り道で子の状態から白、黒のそれぞれのパターン数を計算する。
  que = deque([~0, 0])
  while que:
    current = que.pop()
    if current < 0:
      current = ~current
      for n in EDGES[current]:
        # 子だけを見るので、親ノードだった場合はスキップする。
        if n == parents[current]: continue
        dp[current][0] *= sum(dp[n])
        dp[current][1] *= dp[n][0]

        if dp[current][0] >= mod: dp[current][0]%=mod
        if dp[current][1] >= mod: dp[current][1]%=mod
      continue
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      parents[n] = current
      que.append(~n)
      que.append(n)

  print(sum(dp[0])%mod)

resolve()


def resolve():
  mod = 10**9+7
  N = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  # MATCHES[i]: i 番目の男性と相性の良い女性の index
  MATCHES = [[j for j in range(N) if A[i][j] == 1] for i in range(N)]

  # 
  que = deque()

