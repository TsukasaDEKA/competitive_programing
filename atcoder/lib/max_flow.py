# 最大流 を見つける。
# https://evolite.hatenablog.com/entry/20201203/1606935517
# Ford-Fulkerson法
# フローネットワーク
# 蟻本 p190
# TODO: graph の代わりに 2次元配列で渡すバージョンを実装する。

def maximum_flow(graph, start, goal):
  INF = 1 << 30
  n = len(graph)
  max_flow = 0
  while True:
    # パスを見つける。n のサイズ次第では実行時間長めになるかもしれない。
    visited = [0] * n
    stack = [start]
    last = [None] * n
    while stack:
      x = stack.pop()
      visited[x] = 1
      if x == goal:
        break
      for y in graph[x].keys():
        if visited[y] or graph[x][y] == 0:
          continue
        stack.append(y)
        last[y] = x
    # パスが見つからなかったら終了
    if x != goal:
      break

    # 経路上の最小容量を出す。
    # last に記録してある経路を逆に辿っていっている。
    y = goal
    min_capacity = INF
    while last[y] is not None:
      x = last[y]
      min_capacity = min(min_capacity, graph[x][y])
      y = x

    # last に記録してある経路を逆に辿りながら、逆辺と順辺を入れ替えている。
    y = goal
    while last[y] is not None:
      x = last[y]
      graph[x][y] -= min_capacity
      graph[y][x] += min_capacity
      y = x
    max_flow += min_capacity
  return max_flow

def sample():
  # N が点のセットの個数
  # R が赤い点群の座標
  # B が青い点群の座標
  # 問題 -> https://atcoder.jp/contests/arc092/tasks/arc092_a
  N = 5
  R = [(0, 0), (1, 1), (5, 5), (6, 6), (7, 7)]
  B = [(2, 2), (3, 3), (4, 4), (8, 8), (9, 9)]

  # 経路。0~N-1: 赤い点, N~2N-1: 青い点、2N: source, 2N+1: sink
  graph = [{} for _ in range(2*(N+1))]
  # source と赤い点、sink と青い点を結合
  for i in range(N):
    graph[2*N][i] = 1
    graph[i][2*N] = 0
    graph[N+i][2*N+1] = 1
    graph[2*N+1][N+i] = 0

  for r in range(N):
    for b in range(N):
      if R[r][0] < B[b][0] and R[r][1] < B[b][1]:
        graph[r][b+N] = 1
        graph[b+N][r] = 0
  print(maximum_flow(graph, 2*N, 2*N+1)) # =4

sample()