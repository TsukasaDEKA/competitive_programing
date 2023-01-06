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
  H, W, N, dh, dw = map(int, input().split(" "))
  A = [[int(x)-1 for x in input().split(" ")] for _ in range(H)]
  table = [[[0]*(W+1) for _ in range(H+1)] for _ in range(N)]

  for i in range(N):
    t = table[i]
    for h in range(1, H+1):
      for w in range(1, W+1):
        t[h][w] = t[h-1][w] + t[h][w-1] - t[h-1][w-1]
        if i == A[h-1][w-1]:
          t[h][w] += 1

  ans = [[0]*(W-dw+1) for _ in range(H-dh+1)]
  for i in range(N):
    t = table[i]
    total = table[i][H][W]

    for h in range(H-dh+1):
      for w in range(W-dw+1):
        h_, w_ = h+dh, w+dw
        v = t[h_][w_] - t[h][w_] - t[h_][w] + t[h][w]
        if v < total:
          ans[h][w] += 1

  for a in ans:
    print(*a)

resolve()
