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
  from collections import defaultdict

  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  added_val = defaultdict(int)
  base_val = 0
  for i in range(N):
    added_val[i] = A[i]

  Q = int(input())
  for _ in range(Q):
    query = [int(x) for x in input().split(" ")]
    if query[0] == 1:
      x = query[1]
      added_val = defaultdict(int)
      base_val = x
      continue
    if query[0] == 2:
      i, x = query[1:]
      i -= 1
      added_val[i] += x
      continue
    i = query[1]-1
    print(base_val + added_val[i])

resolve()
