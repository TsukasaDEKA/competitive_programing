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
  def scc(n, edge, directed=False, connection='strong'):
    # n は頂点数、edge は [[i, j],[k, l]] のような形式の配列
    import numpy as np
    from scipy.sparse.csgraph import connected_components
    from scipy.sparse import csr_matrix

    m = len(edge)
    edge_t = np.array(edge, dtype = np.int64).T
    tmp = np.ones(m, dtype = np.int64).T
    graph = csr_matrix((tmp, edge_t[:]), (n, n))

    # directed = True で有効グラフ
    # connection = 'strong' で強連結 (相互移動可能)
    return connected_components(graph, directed=directed, connection=connection)
  inf = 10**18
  N = int(input())
  X = [int(x)-1 for x in input().split(" ")]
  C = [int(x) for x in input().split(" ")]
  EDGES = []
  for i in range(N):
    EDGES.append((i, X[i]))

  g, labels = scc(N, EDGES, directed=True)
  groups = [[] for _ in range(g)]
  for i in range(N):
    groups[labels[i]].append(i)

  ans = [inf]*g
  for i in range(N):
    ans[labels[i]] = min(ans[labels[i]], C[i])

  print(sum([ans[i] for i in range(g) if len(groups[i]) > 1]))

resolve()
