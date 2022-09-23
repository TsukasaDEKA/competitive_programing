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

dh8 = [-1, -1, -1,  0,  0,  1,  1,  1]
dw8 = [-1,  0,  1, -1,  1, -1,  0,  1]

def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]
  H, W = map(int, input().split(" "))
  G = [list(input())+["-"] for _ in range(H)] + [["-"]*(W+1)]

  checked = set()
  h, w = 0, 0
  while True:
    if (h, w) in checked:
      print(-1)
      return
    
    checked.add((h, w))

    if G[h][w] == "U":
      h_ = dh[0]
      w_ = dw[0]

    if G[h][w] == "L":
      h_ = dh[1]
      w_ = dw[1]

    if G[h][w] == "D":
      h_ = dh[2]
      w_ = dw[2]

    if G[h][w] == "R":
      h_ = dh[3]
      w_ = dw[3]
    
    if G[h+h_][w+w_] == "-":
      print(h+1, w+1)
      return
    h += h_
    w += w_

resolve()