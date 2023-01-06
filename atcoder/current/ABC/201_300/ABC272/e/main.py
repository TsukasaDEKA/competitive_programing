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


# https://github.com/tatyam-prime/SortedSet
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
# multiset
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')

def resolve():
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  max_ = 2*(10**5)

  # メグル式二分探索。
  def binary_search(ok, ng, solve, d, base):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, d, base): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, d, base) else -1
  
  def solve_left(i, d, base):
    val = base + i*d
    return val >= 0

  def solve_right(i, d, base):
    val = base + i*d
    return val <= N

  indexes = [[] for _ in range(M+1)]
  for i in range(N):
    a = A[i]
    if a > max_: continue

    d = i+1
    left_m = binary_search(M+1, 0, solve_left, d, a)
    right_m = binary_search(1, M+1, solve_right, d, a)

    if left_m == -1:
      continue

    # print(left_m, right_m)
    for m in range(left_m, right_m+1):
      indexes[m].append(i)

  for time in range(1, M+1):
    table = set()
    for i in indexes[time]:
      val = A[i] + (i+1)*time
      table.add(val)
    
    for i in range(len(table)+1):
      if i not in table:
        print(i)
        break

resolve()
