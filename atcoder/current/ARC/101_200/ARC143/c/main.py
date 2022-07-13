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
  # 全ての山を X 未満 or Y 未満にすることができるか？という問題。
  # X、Y が小さい方が有利ではある。
  # 相手が操作できない山を操作することで時間稼ぎができる。
  # dp だと手数がかかりすぎて TLE
  # 自分に手番が来たときのことを考えてみる。
  # 相手と同じ山を選べば X+Y 分石を減らすという動作を行うことができる。
  # 全ての山の値を X+Y で割った余りの内、全てが X 未満だった場合、青木くんの勝ち
  # => 青木くんは全ての山の値を X+Y の倍数分減らすことができる。
  inf = 10**18+1
  N, X, Y = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  if all(a%(X+Y) < X for a in A):
    print("Second")
    return

  print("First")
  
resolve()