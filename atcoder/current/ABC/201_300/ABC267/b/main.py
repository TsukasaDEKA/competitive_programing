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
  S = list(input())
  count = [0]*7
  for i in range(10):
    if S[i] == "1":
      if i+1 == 7:
        count[0] += 1
      if i+1 == 4:
        count[1] += 1
      if i+1 == 8 or i+1 == 2:
        count[2] += 1
      if i+1 == 5 or i+1 == 1:
        count[3] += 1
      if i+1 == 9 or i+1 == 3:
        count[4] += 1
      if i+1 == 6:
        count[5] += 1
      if i+1 == 10:
        count[6] += 1
  l, r = 0, 0
  for i in range(7):
    if count[i] >= 1:
      l = i
      break
  for i in range(6, -1, -1):
    if count[i] >= 1:
      r = i
      break
  
  if S[0] == "1":
    print("No")
    return

  if r - l <= 1:
    print("No")
    return

  for i in range(l+1, r):
    if count[i] == 0:
      print("Yes")
      return

  print("No")

resolve()