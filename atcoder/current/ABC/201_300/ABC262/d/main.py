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
  mod = 998244353
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  # 一個選ぶ場合は明らかに整数。
  ans = N
  # n 個選ぶ場合の平均について考える。
  for n in range(2, N+1):
    tempA = [a%n for a in A]

    # dp[i][n_][p] := i 番目まで使った時に n_ 個数字を使ってあまりが p になる個数
    dp = [[[0]*n for _ in range(n+1)] for _ in range(N)]
    dp[0][0][0] = 1
    dp[0][1][tempA[0]] = 1
    for i in range(N-1):
      dp_i_1 = dp[i+1]
      dp_i = dp[i]
      dp_i_1[n][0] = dp_i[n][0]
      for n_ in range(n):
        dp_i_n = dp_i[n_]
        dp_i_1_n = dp_i_1[n_]
        for p in range(n):
          dp_i_1_n[p] += dp_i_n[p]
          dp_i_1[n_+1][(p+tempA[i+1])%n] += dp_i_n[p]
          if dp_i_1_n[p] >= mod: dp_i_1_n[p]%=mod
          if dp_i_1[n_+1][(p+tempA[i+1])%n] >= mod: dp_i_1[n_+1][(p+tempA[i+1])%n]%=mod
    ans += dp[-1][n][0]%mod
    if ans >= mod: ans%=mod

  print(ans%mod)

resolve()