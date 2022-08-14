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
  N, X, Y = map(int, input().split(" "))
  # dp[n][c]: レベル N の赤い宝石 1 個からはじめた時に、
  # レベル n の c (c == 0: 赤、c == 1: 青) 色の宝石の最大の個数。
  dp = [[0, 0] for _ in range(N+1)]

  # 初期値。レベル N の赤色の宝石を 1 個持っている状態から始まる。
  dp[N][0] = 1
  for n in range(N, 1, -1):
    # 赤色の宝石に操作を行うときの遷移
    dp[n-1][0] += dp[n][0]
    dp[n][1] += X*dp[n][0]

    # 青色の宝石に操作を行うときの遷移
    dp[n-1][0] += dp[n][1]
    dp[n-1][1] += Y*dp[n][1]

  # 最終的にレベル 1 の青色の宝石を何個作ることができるかを出力する。
  print(dp[1][1])

resolve()