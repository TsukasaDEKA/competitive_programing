# ダイクストラ
# 最短経路問題
from heapq import heappop, heappush
def dijkstra(start, dist, path):
  dist[start] = 0
  candidate = [(0, start)]

  while candidate:
    cost, i = heappop(candidate)
    if cost > dist[i]: continue

    for c, j in path[i]:
      if cost+c >= dist[j]: continue
      dist[j] = cost+c
      heappush(candidate, (cost+c, j))