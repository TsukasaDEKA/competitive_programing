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
  # N が少ない。
  # 差の最小値以上には分割できないはず => 分割後も差を 1 以上維持しておく必要があるので
  inf = 10**18+1
  N = int(input())
  _ = list(input())
  A = [int(x) for x in input().split(" ")]

  min_diff = min(abs(A[i]-A[i+1]) for i in range(N))
  B = [[a//min_diff for a in A] for _ in range(min_diff)]
  for i in range(N+1):
    for j in range(A[i]%min_diff):
      B[j][i] += 1

  print(min_diff)
  [print(*b) for b in B]

H, W = 10, 5
A = [list(range(W)) for _ in range(H)]
[print(*a) for a in A]
resolve()