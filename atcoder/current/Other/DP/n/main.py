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
  from itertools import accumulate # 累積和作るやつ
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  # accA : A の累積和
  # 考察に書いてある sum(A[l:r]) を毎回行うのは無駄なので、累積和を取って O(1) で区間和を出せるようにしておく。
  accA = [0] + [x for x in accumulate(A)]

  # memo[l][r] := 区間 l, r のコストの最小値
  # メモ化再帰をするために使う。（みなさんが変数名をどうしているか気になるのでコメントで教えていただけるとありがたいです。）
  memo = [[None]*(N+1) for _ in range(N)]
  def cost(l, r):
    # r-l == 1 というのは区間の長さが 1、つまりスライムが一匹だけしかいないので合体できない => コスト 0 を返す
    if r-l == 1:
      return 0
    # 再帰で区間 l, r のコストを求める。
    if memo[l][r] is None:
      memo[l][r] = min(cost(l, n) + cost(n, r) for n in range(l+1, r)) + accA[r] - accA[l]
    return memo[l][r]

  print(cost(0, N))

resolve()