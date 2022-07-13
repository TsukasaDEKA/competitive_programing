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
  # ある頂点を見た時に、高橋くんの方がその頂点に違い場合、その頂点に高橋くんが移動することができる。
  # 高橋くんは可能な限り長く逃げ続けるので、最も遠い点に移動しようとする。
  # 全ての頂点に対して青木くんからの距離と高橋くんからの距離を求めて、
  # 高橋くんの方が近い点の中で最も青木くんから遠い点に高橋くんが移動すると考える。
  # ゲームは必ず葉の一個手前の頂点で終わるということに注意して実装する。

  inf = 10**18+1
  N, U, V = map(int, input().split(" "))
  U, V = U-1, V-1
  EDGES = [[] for _ in range(N)]
  for i in range(N-1):
    A, B = [int(x)-1 for x in input().split(" ")]
    EDGES[A].append(B)
    EDGES[B].append(A)
  
  from_U = [-1]*N
  from_U[U] = 0
  deq = deque([U])
  while deq:
    current = deq.popleft()
    for n in EDGES[current]:
      if from_U[n] >= 0: continue
      from_U[n] = from_U[current]+1
      deq.append(n)

  from_V = [-1]*N
  from_V[V] = 0
  deq = deque([V])
  while deq:
    current = deq.popleft()
    for n in EDGES[current]:
      if from_V[n] >= 0: continue
      from_V[n] = from_V[current]+1
      deq.append(n)
  
  ans = 0
  for i in range(N):
    if from_U[i] < from_V[i]:
      ans = max(ans, from_V[i]-1)

  print(ans)

resolve()