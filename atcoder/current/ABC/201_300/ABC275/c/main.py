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
  FIELD = [list(input()) for _ in range(9)]
  ans = 0
  for h_s in range(9):
    for w_s in range(9):
      if FIELD[h_s][w_s] == ".": continue
      for h_n in range(9):
        for w_n in range(9):
          if FIELD[h_n][w_n] == ".": continue
          if h_s == h_n and w_s == w_n: continue

          d_h = h_n - h_s
          d_w = w_n - w_s

          if h_n-d_w < 0 or h_n-d_w >= 9: continue
          if w_n+d_h < 0 or w_n+d_h >= 9: continue
          if FIELD[h_n-d_w][w_n+d_h] == ".": continue

          if h_s-d_w < 0 or h_s-d_w >= 9: continue
          if w_s+d_h < 0 or w_s+d_h >= 9: continue
          if FIELD[h_s-d_w][w_s+d_h] == ".": continue
          # print((h_s, w_s), (h_n, w_n), (h_n-d_w, w_n+d_h), (h_s-d_w, w_s+d_h))

          ans += 1

  # print(ans)
  print(ans//4)

resolve()
