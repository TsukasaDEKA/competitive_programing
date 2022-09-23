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
  # 遷移の時に累積和を作るといい感じにできそう、
  from itertools import accumulate # 累積和作るやつ

  mod = 10**9 + 7
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  # dp[i][k] := i 番目の人に飴を配り終わった時に、今まで配った飴の個数が k 個である配り方の組み合わせ
  # ↑ は二次元だけど、前回の値を利用することで 2 本の一次元 DP テーブルを切り替えることで同じ計算ができるので、
  # そのように実装する。
  dp = [0]*(K+1)
  dp[0] = 1

  for i in range(N):
    # 遷移を高速に行うために累積和をとる
    acc = [0] + list(accumulate(dp))
    dp_ = [0]*(K+1)
    for k in range(K+1):
      dp_[k] = (acc[k+1] - acc[max(0, k-A[i])])%mod
    dp = dp_
  print(dp[-1])

resolve()