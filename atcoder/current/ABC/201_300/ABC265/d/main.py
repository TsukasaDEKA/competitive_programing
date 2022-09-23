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
  from itertools import accumulate # 累積和作るやつ

  # 累積和ではあるっぽい。
  inf = 10**18+1
  N, P, Q, R = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  accA = [0] + list(accumulate(A))
  exist = set(accA)

  for i in range(N):
    offset = accA[i]
    p = offset + P
    q = p + Q
    r = q + R
    if p in exist and q in exist and r in exist:
      print("Yes")
      return

  print("No")

resolve()