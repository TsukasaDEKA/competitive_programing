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
  # 数列 Ai について考える。
  # d == 0 の時、Ai を決めた時に美しいペアとなる Ai+1 は 1 個
  # 全ての数列において、そのペアが生み出す美しさは pow(n, m-2)
  # d != 0 の時、
  # Ai が 1+d 以上かつ n-d 以下の場合、美しいペアとなる Ai+1 は 2 個
  # Ai がそれ以外の場合、美しいペアとなる Ai+1 は 1 個
  # つまり、2*max(0, n-2*d) + n - max(0, n-2*d) に pow(n, m-2) を掛けたものが
  # そのペアが生み出す美しさ

  inf = 10**18+1
  N, M, D = map(int, input().split(" "))
  if D == 0:
    print((M-1)/N)
  else:
    ans = ((2*max(0, N-2*D) + N - max(0, N-2*D))*(M-1))/pow(N, 2)
    print(ans)

resolve()