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
  N, P = map(int, input().split(" "))
  # dp[i]: HP が i の時の攻撃の回数の期待値
  one_damage = ((100-P)*pow(100, mod-2, mod))%mod
  two_damage = (P*pow(100, mod-2, mod))%mod
  if N == 1:
    print(1)
    return

  dp = [0]*(N+1)
  for i in range(1, N+1):
    dp[i] = ((dp[i-1]+1)*one_damage)%mod + ((dp[i-2]+1)*two_damage)%mod

  print((dp[-1])%mod)

resolve()
