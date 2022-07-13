from locale import currency
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
  from collections import deque
  # S で二分探索
  N = int(input())
  JUMP = [[int(x) for x in input().split(" ")] for _ in range(N)]

  # メグル式二分探索。
  def binary_search(ok, ng, solve):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok
  
  def solve(S):
    EDGE_i = [set() for _ in range(N)]
    for i in range(N):
      x_i, y_i, P = JUMP[i]
      for j in range(N):
        if i == j: continue
        x_j, y_j, _ = JUMP[j]

        if S*P >= abs(x_i-x_j) + abs(y_i-y_j):
          EDGE_i[i].add(j)
    
    for i in range(N):
      checked = [False]*N
      checked[i] = True
      deq = deque([i])
      while deq:
        current = deq.pop()
        for n in EDGE_i[current]:
          if checked[n]: continue
          checked[n] = True
          deq.append(n)
      if all(checked): return True
    return False

  ans = binary_search(2*(10**10)+1, 0, solve)
  print(ans)

resolve()