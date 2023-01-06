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
dh6 = [-1, -1,  0,  0,  1, 1]
dw6 = [-1,  0, -1,  1,  0, 1]

def resolve():
  dh6 = [-1, -1,  0,  0,  1, 1]
  dw6 = [-1,  0, -1,  1,  0, 1]
  from collections import deque

  inf = 10**18+1
  N = int(input())
  A = [[int(x) for x in input().split()] for _ in range(N)]
  cell = set()
  for x, y in A:
    cell.add((x, y))
  checked = set()
  deq = deque()

  ans = 0
  for i in range(N):
    x, y = A[i]
    if (x, y) in checked: continue
    ans += 1
    deq.append((x, y))
    checked.add((x, y))

    while deq:
      x, y = deq.popleft()
      for dx, dy in zip(dh6, dw6):
        x_, y_ = x+dx, y+dy

        if (x_, y_) not in cell: continue
        if (x_, y_) in checked: continue
        checked.add((x_, y_))

        deq.append((x_, y_))
  print(ans)

resolve()
