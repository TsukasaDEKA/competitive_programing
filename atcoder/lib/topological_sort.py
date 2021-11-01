# トポロジカルソート
# DAG (有向閉路が無い有向グラフ) で使える。

def topological_sort(N, in_degrees, outs):
  from collections import deque

  topological_graph = []
  # 入次数 0 のノードから始める。
  nexts = deque(x for x in range(N) if in_degrees[x] == 0)
  while nexts:
    current = nexts.popleft()
    topological_graph.append(current)
    for tar in outs[current]:
      in_degrees[tar]-=1
      # 入次数が 0 だったら追加する。
      if in_degrees[tar]==0: nexts.append(tar)

  return topological_graph

# 辞書順にする場合はこちらを使う。
# def topological_sort(N, in_degrees, outs):
#   from heapq import heappop, heappush
#   topological_graph = []
#   # 入次数 0 のノードから始める。
#   c = [x for x in range(N) if in_degrees[x] == 0]
#   nexts = []
#   for i in c:
#     heappush(nexts, i)

#   while nexts:
#     current = heappop(nexts)
#     topological_graph.append(current)
#     for tar in outs[current]:
#       in_degrees[tar]-=1
#       # 入次数が 0 だったら追加する。
#       if in_degrees[tar]==0:
#         heappush(nexts, tar)

#   return topological_graph

# 以下サンプル
from collections import defaultdict, deque

N, M = map(int, "4 5".split(" "))
sample_input = """1 2
1 3
4 2
2 4
3 4"""
sample_input = sample_input.split("\n")

# 葉から順に遡っていって DP していく。
# そのまま遡っていくと計算順序ずれる (親より子を先に計算する必要がある。)ため、先にトポロジカルソートする。
# in_ = defaultdict(list)
out_ = defaultdict(list)
in_degrees = defaultdict(int)

for i in range(M):
  x, y = [int(x)-1 for x in sample_input[i].split(" ")]
  out_[x].append(y)
  in_degrees[y]+=1

# トポロジカルソートする。
topological_graph = topological_sort(N, in_degrees, out_)

print(topological_graph)