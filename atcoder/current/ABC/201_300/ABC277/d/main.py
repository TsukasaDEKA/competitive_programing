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
  N, M = map(int, input().split(" "))
  A = sorted([int(x)%M for x in input().split(" ")])
  if N == 1:
    print(0)
    return

  if A[0] == 0 and A[-1] == M-1:
    for i in range(N-1):
      if A[i+1] - A[i] > 1:
        A = A[i+1:] + A[:i+1]
        break

  ans = inf
  sum_ = sum(A)
  current = A[0]
  temp = A[0]
  for i in range(1, N):
    if current == A[i] or (current+1)%M == A[i]:
      temp += A[i]
    else:
      temp = A[i]
    current = A[i]
    ans = min(ans, sum_-temp)

  print(ans)

resolve()
