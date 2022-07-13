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
  mod = 998244353
  N, M = map(int, input().split(" "))
  bit_max = 60
  if N >= 61:
    print(0)
    return
  count_by_digit = [0] + [max(0, min((1<<(i))-1, M) - ((1<<(i-1))-1))%mod for i in range(1, bit_max+1)]
  dp = [[0]*(bit_max+1) for _ in range(N)]
  dp[0] = [c for c in count_by_digit]
  for i in range(1, N):
    for j in range(1, bit_max+1):
      for k in range(1, j):
        dp[i][j] += dp[i-1][k]*count_by_digit[j]
        if dp[i][j] >= mod: dp[i][j]%=mod
  print(sum(dp[-1])%mod)
resolve()