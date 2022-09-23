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
  # A が正なら全て取るのが良さそう。
  # dp っぽい
  # 左から取っていって、
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  dp = [[-inf]*(M+1) for _ in range(N)]
  for i in range(N):
    dp[i][0] = 0
  dp[0][1] = A[0]

  for i in range(1, N):
    for j in range(1, M+1):
      dp[i][j] = max(dp[i-1][j-1]+j*A[i], dp[i-1][j], dp[i][j])
  # print(*dp)
  print(dp[-1][-1])

resolve()