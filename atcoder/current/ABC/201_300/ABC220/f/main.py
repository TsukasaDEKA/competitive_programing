from re import M
import sys
from tabnanny import check
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
  # i を根とした時の他の頂点の深さの合計が答えになる
  # ただ、それだと計算量が多くなって間に合わない。
  # 計算量を落とす工夫を考えてみる。
  # i = 0 の時の答えが X だとする。
  # i から隣接する頂点 j を見た時、
  # その頂点の答えは X - <辺ij を i => j に移動する回数> + <辺ij を j => i に移動する回数> になる。
  # これは各頂点が持つ子の個数が分かれば計算できる。
  # 辺を挟んで左右に何個ずつ頂点があるかは DFS で帰り道の時に子が持つ子の個数を合計すれば良い。
  N = int(input())
  EDGES = [[] for _ in range(N)]
  for _ in range(N-1):
    A, B = [int(x)-1 for x in input().split(" ")]
    EDGES[A].append(B)
    EDGES[B].append(A)
  child_count = [0]*N
  depth = [-1]*N
  depth[0] = 0
  deq = deque()
  deq.append(~0)
  deq.append(0)
  while deq:
    current = deq.pop()
    if current < 0:
      current = ~current
      child_count[current] = 1
      for n in EDGES[current]:
        child_count[current]+=child_count[n]
      continue

    for n in EDGES[current]:
      if depth[n] >= 0: continue
      depth[n] = depth[current] + 1
      deq.append(~n)
      deq.append(n)

  ans = [0]*N
  ans[0] = sum(depth)
  deq.append(0)
  while deq:
    current = deq.popleft()
    for n in EDGES[current]:
      if ans[n] > 0: continue
      ans[n] = ans[current] - child_count[n] + (N - child_count[n])
      deq.append(n)


  print(*ans, sep="\n")

resolve()