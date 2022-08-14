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
  popcnt = lambda x: bin(x).count("1")
  # 全探索だと間に合わなさそうだけど意外といけるっぽい。
  H_1, W_1 = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(H_1)]
  H_2, W_2 = map(int, input().split(" "))
  B = [[int(x) for x in input().split(" ")] for _ in range(H_2)]

  h_candidates = []
  w_candidates = []
  for bit in range(1, 1<<H_1):
    if popcnt(bit) == H_2:
      h_candidates.append(bit)

  for bit in range(1, 1<<W_1):
    if popcnt(bit) == W_2:
      w_candidates.append(bit)

  A_ = [[0]*W_2 for _ in range(H_2)]
  for bit_h in h_candidates:
    for bit_w in w_candidates:
      rows = [i for i in range(H_1) if bit_h&(1<<i)]
      columns = [i for i in range(W_1) if bit_w&(1<<i)]
      for h in range(H_2):
        for w in range(W_2):
          A_[h][w] = A[rows[h]][columns[w]]

      if B == A_:
        print("Yes")
        return

  print("No")
resolve()