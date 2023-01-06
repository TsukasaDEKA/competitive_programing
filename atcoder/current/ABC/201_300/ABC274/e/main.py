import imp
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
  popcnt = lambda x: bin(x).count("1")

  from math import sqrt
  inf = 10**18
  N, M = map(int, input().split(" "))
  X_Y = [[0, 0]] + [[int(x) for x in input().split(" ")] for _ in range(N)]
  P_Q = [[int(x) for x in input().split(" ")] for _ in range(M)]

  POINTS = X_Y + P_Q
  DISTANCE = [[0]*(N+M+1) for _ in range(N+M+1)]
  for i in range(N+M):
    x_i, y_i = POINTS[i]
    for j in range(i+1, N+M+1):
      x_j, y_j = POINTS[j]
      v = sqrt((x_i-x_j)**2 + (y_i-y_j)**2)
      DISTANCE[i][j] = v
      DISTANCE[j][i] = v

  dp = [[inf]*(1<<(N+M+1)) for _ in range(N+M+1)]
  dp[0][0] = 0
  for i in range(1, N+M+1):
    dp[i][1<<i] = DISTANCE[0][i]

  speed_filter = ((1<<M)-1)<<(N+1)

  for bit in range(1<<(N+M+1)):
    speed = pow(2, popcnt(bit&speed_filter))
    # 遷移元
    for i in range(N+M+1):
      if bit&(1<<i) == 0: continue 
      for j in range(N+M+1):
        if i == j: continue
        if bit&(1<<j): continue

        current = bit|(1<<j)
        dp[j][current] = min(dp[j][current], dp[i][bit] + DISTANCE[i][j]/speed)

  filter_ = (1<<(N+1))-1

  ans = inf
  for i in range(1<<(N+M+1)):
    if i&filter_ == filter_:
      ans = min(ans, dp[0][i])
  print(ans)


resolve()
