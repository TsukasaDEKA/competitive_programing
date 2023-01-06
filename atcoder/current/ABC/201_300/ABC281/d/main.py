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
  # 三次元 DP 
  N, K, D = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  # dp[k][d]
  dp = [[-1]*D for _ in range(K+1)]
  dp[0][0] = 0

  for n in range(N):
    temp_dp = [[-1]*D for _ in range(K+1)]
    for k in range(K+1):
      for d in range(D):
        temp_dp[k][d] = dp[k][d]

    a = A[n]
    for k in range(K):
      for d in range(D):
        if dp[k][d] <= -1: continue
        # 取る場合
        value = dp[k][d] + (d+a)//D
        dist = (d+a)%D
        temp_dp[k+1][dist] = max(temp_dp[k+1][dist], value, dp[k+1][dist])

    dp = temp_dp

  if dp[K][0] < 0:
    print(-1)
  else:
    print(dp[K][0]*D)

resolve()
