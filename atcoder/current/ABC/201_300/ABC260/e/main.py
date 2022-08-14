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
  from collections import defaultdict
  N, M = map(int, input().split(" "))
  indexes = [[] for _ in range(M)]

  # 尺取法をする時に扱いやすいようにデータを持っておく。
  # indexes[X]: 整数 X を持っている整数の組の番号
  for i in range(N):
    a, b = [int(x)-1 for x in input().split(" ")]
    indexes[a].append(i)
    indexes[b].append(i)

  # imos[k]: 長さ k の
  imos = [0]*(M+1)

  # count[i]: 現在、整数の組の番号 i がもつ数字が区間 [L, R) に何個含まれているか
  count = [0]*M

  # includes: Ai, Bi どちらかが [L, R) に含まれる整数の組の番号を管理するための set
  includes = set()
  r = 0
  for l in range(M):
    # [l, r) が良い数列になるか、r をそれ以上右に動かせなくなるまで r を移動させる
    while r < M and len(includes) < N:
      for i in indexes[r]:
        count[i] += 1
        includes.add(i)
      r += 1

    # f(k) (k: r-l ~ M-l) の結果全てに 1 を足す操作
    # いもす法なので、操作する区間の先頭と末尾に値を差し引きするだけ
    if len(includes) == N:
      imos[r-l] += 1
      if M-l+1 <= M: imos[M-l+1] -= 1

    # 左を動かすタイミングで整数の組の番号 i がもつ数字が区間 [l, r) に何個含まれているか？を減らす
    for i in indexes[l]:
      count[i] -= 1
      # count[i] が 1 => 0 に変化したということは、
      # 整数の組 i が区間 [l, r) に含まれなくなったということなので includes から除く
      if count[i] == 0:
        includes.remove(i)

  # いもす法の全体シミュレートを実行する。
  for i in range(1, M+1):
    imos[i] += imos[i-1]
  print(*(imos[1:]))

resolve()