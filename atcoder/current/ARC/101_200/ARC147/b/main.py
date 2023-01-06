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
  P = [int(x)-1 for x in input().split(" ")]

  ans = []
  for _ in range(N):
    x, y = 0, 0
    for x in range(0, N, 2):
      if P[x]%2: break
    if P[x]%2 == 0: break

    for y in range(1, N, 2):
      if P[y]%2 == 0: break

    x, y = min(x, y), max(x, y)
    while y - x > 1:
      ans.append("B {}".format(x+1))
      P[x], P[x+2] = P[x+2], P[x]
      x += 2
    ans.append("A {}".format(x+1))
    P[x], P[y] = P[y], P[x]
  
  for i in range(N-1, -1, -1):
    j = P.index(i)
    while P[j] != j:
      ans.append("B {}".format(j+1))
      P[j], P[j+2] = P[j+2], P[j]
      j += 2
  print(len(ans))
  print(*ans, sep="\n")

resolve()
