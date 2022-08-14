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

dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]
dh8 = [-1, -1, -1,  0,  0,  1,  1,  1]
dw8 = [-1,  0,  1, -1,  1, -1,  0,  1]

def resolve():
  popcnt = lambda x: bin(x).count("1")

  # N の最大値がとても小さいのでこれを利用する。
  # 男性を軸に見ていって、i 番目の男性にマッチする女性を選ぶ時に何通りあるのか？をやっていけば良さそう
  # 考えられる男性と女性の組み合わせは N! 通りあって、相性の良し悪しでその組み合わせが有効なのか決まる。
  inf = 10**18+1
  mod = 10**9+7
  N = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  # MATCHES[i]: i 番目の男性と相性の良い女性の index
  MATCHES = [[j for j in range(N) if A[i][j] == 1] for i in range(N)]
  dp = [0]*(1<<N)
  dp[0] = 1

  for s in range((1<<N)-1):
    # i: 何番目の男性を見るか？を表すインデックス
    # popcnt(s) は既に相手が決まっている女性の人数。
    # 0-index で考えて popcnt(s) 番目の男性を見るようにする。
    i = popcnt(s)
    for n in MATCHES[i]:
      # n 番目の女性のお相手が既に決まっている場合、遷移できない。
      if s&(1<<n): continue

      # n 番目の女性と i 番目の女性をマッチさせた時、状態は s|(1<<n) になるので、そこに遷移する。
      j = s|(1<<n)
      dp[j] += dp[s]
      if dp[j] >= mod: dp[j]%=mod

  print(dp[-1]%mod)

resolve()