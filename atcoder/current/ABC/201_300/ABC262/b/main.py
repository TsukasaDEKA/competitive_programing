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
  EDGES = [set() for _ in range(N)]
  for _ in range(M):
    u, v = [int(x)-1 for x in input().split(" ")]
    EDGES[u].add(v)
    EDGES[v].add(u)
  
  ans = 0
  for a in range(N-2):
    for b in range(a+1, N-1):
      for c in range(b+1, N):
        if b in EDGES[a] and c in EDGES[b] and a in EDGES[c]:
          ans += 1

  print(ans)

resolve()