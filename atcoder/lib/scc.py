# 強連結成分分解
def scc(n, edge, directed=False, connection='strong'):
  # n は頂点数、edge は [[i, j],[k, l]] のような形式の配列
  from collections import Counter
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


def sample():
  from collections import Counter

  N = 4
  M = 7
  sample = [[0, 1], [1, 0], [1, 2], [3, 2], [3, 0], [0, 3], [1, 2]]
  _, labels = scc(N, sample, directed=True)

  groups = Counter(labels)
  ans = 0
  for val in groups.values():
    if val < 2: continue
    ans += val*(val-1)//2
  return ans

print(sample())