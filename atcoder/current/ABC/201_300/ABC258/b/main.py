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

def resolve():
  inf = 10**18+1
  dh8 = [-1, -1, -1,  0,  0,  1,  1,  1]
  dw8 = [-1,  0,  1, -1,  1, -1,  0,  1]
  N = int(input())
  A = [[x for x in list(input())] for _ in range(N)]

  ans = 0
  for h in range(N):
    for w in range(N):
      for j in range(8):
        dh = dh8[j]
        dw = dw8[j]
        temp = ""
        for i in range(N):
          h_ = (h+dh*i)%N
          w_ = (w+dw*i)%N
          temp += A[h_][w_]
        ans = max(ans, int(temp))

  print(ans)

resolve()