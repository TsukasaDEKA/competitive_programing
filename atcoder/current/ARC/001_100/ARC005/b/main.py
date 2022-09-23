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
  S = input().split(" ")
  w, h = [int(x)-1 for x in S[:2]]

  D = S[-1]
  dh = 0
  if "D" in D: dh = 1
  if "U" in D: dh = -1

  dw = 0
  if "L" in D: dw = -1
  if "R" in D: dw = 1

  C = [list(input()) for _ in range(9)]

  ans = C[h][w]
  for _ in range(3):
    h += dh
    w += dw

    if h <= -1 or h >= 9:
      dh *= -1
      if h <= -1: h = 1
      if h >=  9: h = 7

    if w <= -1 or w >= 9:
      dw *= -1
      if w <= -1: w = 1
      if w >=  9: w = 7

    ans += C[h][w]
  print(ans)

resolve()