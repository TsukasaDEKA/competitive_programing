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
  # dp っぽいんだよなぁ。
  mod = 998244353
  N, M, K = map(int, input().split(" "))

  DP = [[0]*(N+1) for _ in range(K+1)]
  DP[0][0] = 1
  perM = pow(M, mod-2, mod)
  for i in range(K):
    for n in range(N+1):
      if n == N:
        DP[i+1][N] += DP[i][N]
        continue

      v = (DP[i][n]*perM)%mod
      if v == 0: continue

      for m in range(1, M+1):
        k = 2*N-(n+m) if n+m > N else n+m
        DP[i+1][k] = (DP[i+1][k]+v)%mod

  print(DP[-1][-1]%mod)
resolve()
