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
  S = list(input())
  T = list(input())

  # ランレングス圧縮する。aaabbc => [(a, 3), (b, 2), (c, 1)]
  def run_length_compless(S):
    agg_S = [[S[0], 1]]
    for s in S[1:]:
      if agg_S[-1][0] == s: agg_S[-1][1] += 1
      else: agg_S.append([s, 1])
    return agg_S

  agg_S = run_length_compless(S)
  agg_T = run_length_compless(T)

  # 要素の長さが違う場合、S => T の変換はできない。
  if len(agg_S) != len(agg_T):
    print("No")
    return

  N = len(agg_S)
  # 要素毎に比較して、agg_S[i] => agg_T[i] にできるかどうかを判定する。
  for i in range(N):
    s, count_s = agg_S[i]
    t, count_t = agg_T[i]

    # 要素の種類が違う場合、複合できない。
    if s != t:
      print("No")
      return

    # S 側の i 番目の要素の長さが 1 の時、それ以上 S 側を伸ばすことができないので、
    # T 側の i 番目の要素の長さが 1 で無い限り複合ができない。
    if count_s == 1 and count_t != 1:
      print("No")
      return

    # S 側を縮めることはできないので、T 側より S 側が長い時は複合できない。
    if count_s > count_t:
      print("No")
      return

  # すべての要素で複合できないケースが存在しない場合、複合できる判定
  print("Yes")

resolve()