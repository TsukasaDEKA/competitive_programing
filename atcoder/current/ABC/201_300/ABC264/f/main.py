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
  # 初期状態の 0 と 1 の間には壁が存在していると考えることができる。
  # その壁の片側だけに操作した時、壁が消滅するし、両方に対して操作すれば壁は残ったまま。
  # 壁がないときは反対の挙動になる。
  # 既に同じエリア
  N, W = map(int, input().split(" "))
  R = [int(x) for x in input().split(" ")]
  C = [int(x) for x in input().split(" ")]
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]

  print()

resolve()