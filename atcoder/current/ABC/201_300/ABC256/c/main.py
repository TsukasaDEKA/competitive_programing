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
  inf = 10**18+1
  HW = [int(x) for x in input().split(" ")]
  H, W = HW[:3], HW[3:]
  # 上 2 段を確定させると 3 行目が確定するので、それの合計が 最終行を満たすか判定
  ans = 0
  for h0w0 in range(1, H[0]-1):
    for h0w1 in range(1, H[0]):
      if h0w0 + h0w1 >= H[0]: break
      h0w2 = H[0] - (h0w0 + h0w1)

      for h1w0 in range(1, H[1]-1):
        if h0w0 + h1w0 >= W[0]: break
        h2w0 = W[0] - (h0w0 + h1w0)
        for h1w1 in range(1, H[1]):
          if h0w1 + h1w1 >= W[1]: break
          h2w1 = W[1] - (h0w1 + h1w1)
          if h1w0 + h1w1 >= H[1]: break
          h1w2 = H[1] - (h1w0 + h1w1)
          
          h2w2 = W[2] - (h0w2 + h1w2)
          if h2w2 <= 0: continue
          if h2w2 == H[2] - (h2w0 + h2w1):
            ans += 1

  print(ans)

resolve()
