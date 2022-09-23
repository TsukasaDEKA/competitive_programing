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
  # 上の桁から順に決めていける？
  # 大きい順に K 要素選ぶ。一番大きな要素に揃えることができるのであれば、残った操作を均等に割り振った値が答え。
  # 一番大きな要素に揃えることができない場合を考える。
  # 答えで二分探索系？
  # 
  N, M, K = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")])

  # メグル式二分探索。
  def binary_search(ok, ng, solve):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok) else -1

  def solve(x):
    # x が答え。
    # 全てを x にするのに必要な回数を求める。
    steps = [0]*N
    for i in range(N):
      a = A[i]
      # b: bit の桁
      for b in range(31, -1, -1):
        if x&(1<<b) and a&(1<<b) == 0:
          steps[i] =  (x&((1<<(b+1))-1)) - (a&((1<<(b+1))-1))
          break
    # print(x, steps, file=sys.stderr)
    steps.sort()
    # print( sum(steps[:K]) <= M, file=sys.stderr)
    return sum(steps[:K]) <= M

  print(binary_search(0, pow(2, 31), solve))

resolve()