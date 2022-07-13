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
  # 答えで二分探索？
  # 答えを l とすると、左から順に見ていって l 以上になった時点で切れ目を選択する。
  # 切れ目を K 個以上選択できたら答えを l 以上にできる。
  inf = 10**18+1
  N, L = map(int, input().split(" "))
  K = int(input())
  A = [int(x) for x in input().split(" ")] + [L]
  N += 1

  def binary_search(ok, ng, solve):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok) else -1

  def solve(x):
    count = 0
    l = 0
    for i in range(N):
      if A[i] - l >= x:
        l = A[i]
        count += 1
    return count >= K+1


  print(binary_search(0, inf, solve))

resolve()