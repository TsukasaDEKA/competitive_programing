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
  mod = 10**9+7
  N = [int(x) for x in list(input())]
  D = int(input())

  # dp[i][f][d] := i 桁目まで見た時に、N 以下であることが確定した状態で、かつ各桁の和が d である組み合わせの数
  dp = [[[0]*D for _ in range(2)] for _ in range(len(N))]

  # 初期化。1 桁目だけ遷移なしで入れる。
  for i in range(N[0]+1):
    dp[0][int(i<N[0])][i%D] += 1

  for i in range(len(N)-1):
    for d in range(D):
 
      # N 以下であることが確定していないセルの遷移
      # 遷移先の桁が 0 ~ N[i] に変化する。
      for n in range(N[i+1]+1):
        dp[i+1][int(n < N[i+1])][(d+n)%D] += dp[i][int(False)][d]
        if dp[i+1][int(n < N[i+1])][(d+n)%D] >= mod:
          dp[i+1][int(n < N[i+1])][(d+n)%D]%=mod
    
      # N 以下であることが確定しているセルの遷移
      # 遷移先の桁が 0 ~ 9 に変化する。
      for n in range(10):
        dp[i+1][int(True)][(d+n)%D] += dp[i][int(True)][d]
        if dp[i+1][int(True)][(d+n)%D] >= mod:
          dp[i+1][int(True)][(d+n)%D]%=mod
  # [print(*d) for d in dp]
  # 上記の計算を行うと、0 が答えに含まれてしまう。
  # しかし、問題の条件を満たすのは 1 ~ N なので、 カウントされた 0 を除外する意味で -1 する。
  print((dp[-1][0][0] + dp[-1][1][0] - 1)%mod)
 
resolve()