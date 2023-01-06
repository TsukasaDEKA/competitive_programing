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
  N = int(input())
  S = list(input())
  l = -1
  for i in range(N):
    if S[i] == "p":
      l = i
      break

  if l == -1:
    print("".join(S))
    return

  ans = [s for s in S]

  front = [s for s in S[:l]]
  rev = []

  for i in range(l, N):
    rev.append("d" if S[i] == "p" else "p")
    temp = front + rev[::-1] + S[i+1:]
    if temp < ans: ans = [s for s in temp]

  print("".join(ans))

resolve()