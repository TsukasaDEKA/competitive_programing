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
  # N が 1 の時、A は B に対して 1 パターンしかない。
  # M が 1 の時、B は A に対して 1 パターンしかない。
  # それ以外の時、A に含まれる値の最大値でが B に含まれる値の最小値
  # 境界となる値を X とすると、A のパターン数は pow(X, N)、B のパターン数は、pow(K-x+1, M) - pow(K-x, M) (少なくとも 1 つは X である必要があるため)
  N, M, K = map(int, input().split(" "))
  if N == 1 and M == 1:
    print(K)
    return
  if N == 1:
    print(pow(K, M, mod))
    return
  if M == 1:
    print(pow(K, N, mod))
    return
  
  ans = 0
  for x in range(1, K+1):
    A_pattern = pow(x, N, mod)
    B_pattern = pow(K-x+1, M, mod) - pow(K-x, M, mod)
    ans += (A_pattern*B_pattern)%mod
    if ans >= mod: ans %= mod

  print(ans)

resolve()