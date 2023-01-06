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
  N, M = map(int, input().split(" "))
  A = [int(x)-1 for x in input().split(" ")]
  B = [x for x in range(N)]
  # 一通りやってから逆順に操作
  B_index = [x for x in range(N)]
  changed_to = [-1]*M
  for i in range(M):
    a = A[i]
    b0, b1 = B[a], B[a+1]
    B[a], B[a+1] = B[a+1], B[a]
    B_index[b0], B_index[b1] = a+1, a
    if b0 == 0 or b1 == 0:
      changed_to[i] = max(b0, b1)
  #   print(B_index, b0, b1)
  # print(B_index)
  # print(changed_to)
  ans = [0]*M
  for i in range(M):
    if changed_to[i] == -1:
      ans[i] = B_index[0]+1
    else:
      ans[i] = B_index[changed_to[i]]+1


  print(*ans, sep="\n")

resolve()
