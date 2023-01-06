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
  alpha2num = lambda c: ord(c) - ord('A')

  inf = 10**18+1
  S = list(input())
  N = len(S)
  if N != 8:
    print("No")
    return

  if alpha2num(S[0]) < 0 or alpha2num(S[-1]) < 0:
    print("No")
    return
  
  for i in range(1, N-1):
    if alpha2num(S[i]) >= 0:
      print("No")
      return
  
  val = int("".join(S[1:7]))
  if val < 100000 or val >= 1000000:
    print("No")
    return
  print("Yes")

resolve()
