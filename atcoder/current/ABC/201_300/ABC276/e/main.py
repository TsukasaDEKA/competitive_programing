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
  from collections import deque
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  FIELD = [list(input())+["#"] for _ in range(H)] + [["#"]*(W+1)]

  que = deque()
  FROM = [[(-1, -1)]*W for _ in range(H)]
  
  start = (-1, -1)
  for h in range(H):
    for w in range(W):
      if FIELD[h][w] == "S":
        start = (h, w)
        FROM[h][w] = (h, w)
        for i in range(4):
          h_ = dh[i] + h
          w_ = dw[i] + w
          if FIELD[h_][w_] == "#": continue
          que.append((h_, w_))
          FROM[h_][w_] = (h_, w_)

  # print(que)  

  while que:
    h, w = que.popleft()

    for i in range(4):
      h_ = dh[i] + h
      w_ = dw[i] + w
      if FIELD[h_][w_] == "#": continue
      if FIELD[h_][w_] == "S": continue
      if FROM[h_][w_] != (-1, -1):
        if FROM[h_][w_] != FROM[h][w]:
          print("Yes")
          return
        continue
      FROM[h_][w_] = FROM[h][w]
      que.append((h_, w_))
  # for f in FROM:
  #   print(*f)
  print("No")

resolve()
