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
  # 喜ぶ移動量の頻出値を求める。
  inf = 10**18+1
  N = int(input())
  P = [int(x) for x in input().split(" ")]

  p_to_i = [0]*N
  for i in range(N):
    p_to_i[P[i]] = i
  # print(p_to_i)
  # i 番目の人が喜ぶ移動量 k
  ans = [0]*N
  for n in range(N):
    # n 番目の人が喜ぶ料理は i 番目に置いてある。
    i = p_to_i[n]
    diff = n - p_to_i[n]
    for d in range(-1, 2):
      ans[(diff+d)%N] += 1


  print(max(ans))

resolve()