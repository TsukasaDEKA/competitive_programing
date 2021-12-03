
from heapq import heappop, heappush
def dijkstra(start, dist, path):
  candidate = [(0, start)]

  while candidate:
    cost, i = heappop(candidate)
    if cost > dist[i]: continue
    dist[i] = cost

    for c, j in path[i]:
      if cost+c > dist[j]: continue
      heappush(candidate, (cost+c, j))