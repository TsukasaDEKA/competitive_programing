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
  # 末尾から逆算？

  from collections import defaultdict

  inf = 10**18+1
  N = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  ans = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
  ans[0][0][A[0][0]] = 1

  for i in range(N):
    ans_i = ans[i]
    ans_i_1 = ans[i-1]
    for j in range(N):
      
      if i > 0:
        for k in ans[i-1][j].keys():
          ans_i[j][k^A[i][j]] += ans_i_1[j][k]

      if j > 0:
        for k in ans_i[j-1].keys():
          ans_i[j][k^A[i][j]] += ans_i[j-1][k]

  # print(ans)
  print(ans[N-1][N-1][0])

resolve()
