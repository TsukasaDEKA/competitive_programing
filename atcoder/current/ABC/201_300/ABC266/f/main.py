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
  # なもりグラフの閉路に含まれる頂点かどうかを判定して [boolean]*N の配列で返す。
  # 無向グラフのみ対応している。
  # edges[n] := 頂点 n に直接繋がっている頂点の index
  def is_in_cycle_of_namori_graph(N, edges):
    # 次数を求める。
    degrees = [len(x) for x in edges]

    result = [d != 1 for d in degrees]
    que = deque([i for i in range(N) if degrees[i] == 1])
    while que:
      current = que.pop()
      for e in edges[current]:
        if not result[e]: continue
        degrees[e] -= 1
        if degrees[e] == 1:
          result[e] = False
          que.append(e)

    return result

  N = int(input())
  EDGES = [[] for _ in range(N)]
  for _ in range(N):
    u, v =  [int(x)-1 for x in input().split(" ")]
    EDGES[u].append(v)
    EDGES[v].append(u)

  # is_in_cycle[i] : i 番目の頂点がなもりグラフのサイクルに入っているかどうか。
  is_in_cycle = is_in_cycle_of_namori_graph(N, EDGES)

  # 閉路上の全ての点から DFS をする。
  que = deque([i for i in range(N) if is_in_cycle[i]])
  checked = [x for x in is_in_cycle]

  roots = list(range(N))
  while que:
    current = que.pop()
    for e in EDGES[current]:
      if checked[e]: continue
      checked[e] = True
      roots[e] = roots[current]
      que.append(e)

  # クエリ処理
  Q = int(input())
  for _ in range(Q):
    u, v = [int(x)-1 for x in input().split(" ")]

    # 根が同一 => 同じ部分木に属しているのであれば Yes
    print("Yes" if roots[u] == roots[v] else "No")

resolve()