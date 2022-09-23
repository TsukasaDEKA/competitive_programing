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
  from collections import defaultdict

  # DP で解ける。dp[i] := 0 ~ i 番目の石を使って作れる組み合わせの数。
  # 新しい石を追加した時、
  # - 一個手前の石と同じ色であればパターン数は増えない。
  # - 左側に同じ色がの石がある場合、その石に挟まれた区間を塗り替えるかどうかを行うわけなので、前の石が i まで見た時にあり得る組み合わせの数を足す。
  # - 左側に同じ色の石がない場合、パターン数は増えない。
  mod = 10**9+7
  inf = 10**18+1
  N = int(input())
  C = [int(input()) for _ in range(N)]
  dp = [1]*N
  indexes = defaultdict(list)
  indexes[C[0]].append(0)
  for i in range(1, N):
    c = C[i]
    dp[i] = dp[i-1]
    if len(indexes[c]) != 0 and c != C[i-1]:
      dp[i] += dp[indexes[c][-1]]
    if dp[i] >= mod: dp[i]%=mod

    indexes[c].append(i)

  print(dp[-1])

resolve()