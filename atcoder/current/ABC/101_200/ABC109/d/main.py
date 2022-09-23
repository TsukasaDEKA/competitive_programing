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
  H, W = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(H)]
  ans = []
  for h in range(H):
    for w in range(W):
      if h == H-1 and w == W-1: continue
      if A[h][w]%2:
        if w < W-1:
          A[h][w]-=1
          A[h][w+1]+=1
          ans.append((h, w, h, w+1))
        else:
          A[h][w]-=1
          A[h+1][w]+=1
          ans.append((h, w, h+1, w))

  print(len(ans))
  for h, w, h_, w_ in ans:
    print(h+1, w+1, h_+1, w_+1)

resolve()