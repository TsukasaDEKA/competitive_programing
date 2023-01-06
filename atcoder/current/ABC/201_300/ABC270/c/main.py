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
  from collections import deque

  inf = 10**18+1
  N, X, Y = map(int, input().split(" "))
  X, Y = X-1, Y-1
  EDGES = [[] for _ in range(N)]

  for _ in range(N-1):
    U, V = [int(x)-1 for x in input().split(" ")]
    EDGES[U].append(V)
    EDGES[V].append(U)

  parents = [-1]*N
  deq = deque()
  deq.append(Y)
  checked = [False]*N
  checked[Y] = True

  while deq:
    current = deq.pop()

    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      parents[n] = current
      deq.append(n)

  ans = [str(X+1)]
  node = X
  while node != Y:
    node = parents[node]
    ans.append(str(node+1))

  print(" ".join(ans))

resolve()
