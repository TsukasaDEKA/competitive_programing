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
  # 要素数が奇数の集合の数を求めるのは可能。
  # 要素数が奇数 + 全要素の XOR が 0 でない - 全要素数が奇数かつ全要素の XOR が 0 でない
  # [01, 10, 11] は XOR をとると 0 になるが要素が奇数
  # 集合の種類は pow(2, 2**N) 個ある。
  # そこから要素数が偶数個かつ全要素の XOR が 0 になる集合 T の個数を引く。
  # 空集合が条件を満たす点に注意する。
  mod = 998244353
  N = int(input())
  if N == 1:
    print(2)
    return

  base = pow(2, pow(2, N), mod)
  # print(base, pow(2, pow(2, N-2, mod))
  ans = (base - pow(2, pow(2, N-2), mod) + 1)%mod
  print(ans)

resolve()