import sys

from numpy import true_divide
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

import sys

def resolve():
  N, X, Y, Z = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]

  # 数学・英語・数学＋英語それぞれの点数が大きい順に並べる。
  # 点数が同じだった場合、受験番号が小さい方が前に来るように、受験番号を負の値にする。
  MATH = sorted([(a, -(i+1)) for i, a in enumerate(A)], reverse=True)
  ENGLISH = sorted([(b, -(i+1)) for i, b in enumerate(B)], reverse=True)
  SUM = sorted([(A[i]+B[i], -(i+1)) for i in range(N)], reverse=True)

  # fixed: 合格した人のインデックスの集合
  fixed = set()

  # 数学の点数が高い方から X 人合格させる。
  for _, i in MATH:
    if len(fixed) == X: break
    fixed.add(i)

  # 英語の点数が高い方から Y 人合格させる。
  # 既に X 人合格しているので、この処理が終わった時点で X + Y 人合格していることになる。
  for _, i in ENGLISH:
    if len(fixed) == X+Y: break
    fixed.add(i)

  # 数学 + 英語の点数が高い方から Z 人合格させる。
  # 既に X + Y 人合格しているので、この処理が終わった時点で X + Y + Z 人合格していることになる。
  for _, i in SUM:
    if len(fixed) == X+Y+Z: break
    fixed.add(i)

  # ソートする時にインデックスを負の値にしたので、
  ans = sorted([-i for i in list(fixed)])

  print(*ans, sep="\n")

resolve()