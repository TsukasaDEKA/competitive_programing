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
  H, M = map(int, input().split(" "))
  minutes = H * 60 + M
  for _ in range(24*60+1):
    h, m = minutes//60, minutes%60

    l_top = h//10
    l_bottom = h%10
    r_top = m//10
    r_bottom = m%10
    h_ = l_top*10 + r_top
    m_ = l_bottom*10 + r_bottom

    if h_ <= 23 and m_ <= 59:
      print(h, m)
      return
    minutes += 1
    if minutes >= 24*60:
      minutes = 0

resolve()
