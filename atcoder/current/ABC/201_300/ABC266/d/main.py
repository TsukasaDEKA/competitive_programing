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
  # DP 
  N = int(input())
  limit = 10**5
  TABLE = {}
  for i in range(N):
    T, X, A = [int(x) for x in input().split(" ")]
    TABLE[T] = (X, A)
  dp = [[0]*5 for _ in range(limit+1)]
  dp[0] = [0, -inf, -inf, -inf, -inf]
  for t in range(1, limit+1):
    for i in range(5):
      dp[t][i] = max(dp[t-1][max(0, i-1)], dp[t-1][i], dp[t-1][min(4, i+1)])
    
    if t not in TABLE: continue
    x, a = TABLE[t]
    dp[t][x] += a
  print(max(dp[-1]))

resolve()