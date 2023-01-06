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
  # 埋めれる
  # 端っこの処理が困りそう。

  inf = 10**18+1
  N, M = map(int, input().split(" "))
  X_Y = [[int(x) for x in input().split(" ")] for _ in range(M)]
  if M == 0:
    print("Takahashi" if N%2 else "Aoki")
    return

  odd = 0
  for i in range(M-1):
    x_l, y_l = X_Y[i]
    x_r, y_r = X_Y[i]
    if y_l == y_r: odd += 1

  count = 0
  x, y = X_Y[0]
  if x == 2: odd += 1
  if x > 2: count += 1

  x, y = X_Y[-1]
  if x == N-1: odd += 1
  if x < N-1: count += 1

  if count == 1:
    print("Takahashi")
    return

  if count == 2:
    print("Aoki")
    return

  odd %= 2

  print("Takahashi" if odd else "Aoki")

resolve()
