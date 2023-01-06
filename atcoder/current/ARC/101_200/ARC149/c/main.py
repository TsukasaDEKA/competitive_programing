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
  N = int(input())

  if N == 3:
    print(*[5, 9, 1])
    print(*[3, 7, 8])
    print(*[6, 2, 4])
    return

  if N == 4:
    print(*[15, 13, 11,  9])
    print(*[ 7,  5,  3,  1])
    print(*[ 2,  4,  6,  8])
    print(*[10, 12, 14, 16])
    return

  if N == 5:
    print(*[25, 23, 21, 19, 17])
    print(*[15, 13,  9,  1,  3])
    print(*[ 5, 11,  7,  8,  6])
    print(*[10,  4,  2, 12, 14])
    print(*[16, 18, 20, 22, 24])
    return

  # N が偶数の場合
  odds = []
  odds_3 = []
  evens = []
  evens_3 = []
  for i in range(1, (N**2)+1):
    if i%2:
      if i%3: odds.append(i)
      else: odds_3.append(i)
    else:
      if i%3: evens.append(i)
      else: evens_3.append(i)

  ans = [[0]*N for _ in range(N)]

  # 三の倍数を真ん中に並べる。
  h = (N-1)//2
  for w in range(N):
    o, e = odds_3.pop(), evens_3.pop()
    h_ = h if N%2 == 0 or w < (N+1)//2 else h-1
    ans[h_][w], ans[h_+1][w] = o, e

  odds += odds_3
  evens += evens_3
  for h in range(N):
    for w in range(N):
      if ans[h][w] > 0: continue
      if h <= (N-1)//2:
        ans[h][w] = odds.pop()
      else:
        ans[h][w] = evens.pop()

  for a in ans:
    print(*a)
resolve()
