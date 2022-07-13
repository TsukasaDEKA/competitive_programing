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
  import sys
  inf = sys.maxsize
  N, X = map(int, input().split(" "))
  STAGES = [[int(x) for x in input().split(" ")] for _ in range(N)]

  ans = inf
  current_time = 0
  clear_cout = 0
  for i in range(N):
    a, b = STAGES[i]
    clear_cout += 1
    current_time += (a+b)

    # print(i, a, b, current_time, clear_cout, current_time + (X - clear_cout)*b)
    ans = min(ans, current_time + (X - clear_cout)*b)
    if (X - clear_cout) <= 0: break

  print(ans)

resolve()