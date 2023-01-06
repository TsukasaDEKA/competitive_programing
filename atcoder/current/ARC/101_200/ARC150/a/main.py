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
  T = int(input())

  for _ in range(T):
    N, K = map(int, input().split(" "))
    S = list(input())
    one_sum = [0]*(N+1)
    zero_sum = [0]*(N+1)
    for i in range(N):
      one_sum[i+1] = one_sum[i]
      zero_sum[i+1] = zero_sum[i]
      if S[i] == "1": one_sum[i+1] += 1
      if S[i] == "0": zero_sum[i+1] += 1
    
    total_one = one_sum[-1]
    count = 0
    for i in range(K, N+1):
      one_count = one_sum[i] - one_sum[i-K]
      zero_count = zero_sum[i] - zero_sum[i-K]
      if one_count == total_one and zero_count == 0:
        count += 1

    print("Yes" if count == 1 else "No")

resolve()
