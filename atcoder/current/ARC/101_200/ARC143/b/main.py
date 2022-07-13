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
  # 高速な組み合わせ計算
  def comb(N, R, mod):
    if N-R < R: R = N-R

    # 分母を計算
    ans = 1
    for n in range(N-R+1, N+1):
      ans*=n
      if ans > mod: ans%=mod

    # 分子を計算
    den = 1
    for r in range(2, R+1):
      den*=r
      if den > mod: den%=mod

    ans *= pow(den, mod-2, mod)
    return ans%mod

  mod = 998244353
  N = int(input())
  if N == 1:
    print(0)
    return

  # 余事象を求める
  # N**2 個の数字から 2*N-1 個の数字を選ぶ組み合わせ
  comp = comb(N**2, 2*N-1, mod)
  comp = (comp * (N**2))%mod

  # 中央値 X 以外の数字を行と列にそれぞれ配置する組み合わせ。
  # (N-1)! を 2 回かける
  for _ in range(2):
    for n in range(2, N):
      comp *= n
      if comp >= mod: comp %= mod

  # 他の数字を配置する組み合わせ
  for n in range(2, (N-1)**2 + 1):
    comp *= n
    if comp >= mod: comp %= mod
  
  # 全事象は (N**2)!
  all_pattern = 1
  for n in range(2, N**2 + 1):
    all_pattern *= n
    if all_pattern >= mod: all_pattern %= mod

  print((all_pattern - comp)%mod)

resolve()