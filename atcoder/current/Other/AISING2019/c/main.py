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
  from collections import deque
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]

  inf = 10**18+1
  H, W = map(int, input().split(" "))
  S = [list(input()) + [""] for _ in range(H)] + [[""]*(W+1)]
  G = [[-1]*W for _ in range(H)]

  g = 0
  ans = 0
  que = deque()
  for h in range(H):
    for w in range(W):
      if G[h][w] >= 0: continue
      que.append((h, w))
      G[h][w] = g
      black, white = 0, 0
      while que:
        h_, w_ = que.popleft()
        if S[h_][w_] == "#": black += 1
        else: white += 1

        for i in range(4):
          h__ = h_+dh[i]
          w__ = w_+dw[i]
          if S[h__][w__] == "": continue
          if G[h__][w__] >= 0: continue
          if S[h__][w__] == S[h_][w_]: continue
          G[h__][w__] = g
          que.append((h__, w__))
      g += 1
      ans += black * white
  print(ans)

resolve()
