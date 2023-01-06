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
  N, M = map(int, input().split(" "))
  A = [[int(x)-1 for x in input().split(" ")] for _ in range(M)]
  table = [[0]*N for _ in range(N)]
  for n in range(N):
    table[n][n] = 1

  for i in range(M):
    a = A[i]
    k = a[0]+1
    for j in range(k-1):
      l = a[j+1]

      for k_ in range(j+1, k):
        r = a[k_+1]
        table[l][r] += 1
        table[r][l] += 1

  # print(table)
  for i in range(N):
    for j in range(N):
      if table[i][j] == 0:
        print("No")
        return

  print("Yes")
resolve()
