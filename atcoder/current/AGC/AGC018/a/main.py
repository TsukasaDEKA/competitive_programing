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
  N, K = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")])

  if max(A) < K:
    print("IMPOSSIBLE")
    return

  if K in A or 1 in A:
    print("POSSIBLE")
    return

  if N == 1:
    print("IMPOSSIBLE")
    return

  temp = A[0]
  for i in range(1, N):
    temp = gcd(temp, A[i])
    if temp == 1 or temp == K:
      print("POSSIBLE")
      return

  print("IMPOSSIBLE")

resolve()