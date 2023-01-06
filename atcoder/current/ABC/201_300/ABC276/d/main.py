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
  A = [int(x) for x in input().split(" ")]

  count_2 = [0]*N
  count_3 = [0]*N
  temp = [0]*N
  for i in range(N):
    a = A[i]
    while a%2 == 0:
      a//=2
      count_2[i] += 1

    while a%3 == 0:
      a//=3
      count_3[i] += 1

    temp[i] = a

  v = temp[0]
  for t in temp:
    if v != t:
      print(-1)
      return
  min_2 = min(count_2)
  min_3 = min(count_3)

  ans = 0
  for i in range(N):
    ans += count_2[i]-min_2+count_3[i]-min_3
  
  print(ans)

resolve()
