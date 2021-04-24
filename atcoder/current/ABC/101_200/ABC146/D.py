import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """3
1 2
2 3"""
        output = """2
1
2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8
1 2
2 3
2 4
2 5
4 7
5 6
6 8"""
        output = """4
1
2
3
4
1
1
2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
1 2
1 3
1 4
1 5
1 6"""
        output = """5
1
2
3
4
5"""
        self.assertIO(input, output)

def resolve():
  # 幅優先探索で解ける。
  # 次のノードを選ぶ際に、辺を塗っていく。
  # ノードにはどの色の辺から来たか記録していく。
  # 次のノードに行く際の辺は来た時に使った色とは別の色を塗る。
  from collections import deque
  N = int(input())

  node_connections = [[] for _ in range(N)]
  K = 0
  for i in range(N-1):
    a, b = [int(x)-1 for x in input().split(" ")]
    node_connections[a].append((i, b))
    node_connections[b].append((i, a))
    K = max(K, len(node_connections[a]), len(node_connections[b]))

  next_node = deque([0])
  first_edge_color = [None]*N
  first_edge_color[0] = 0
  edge_colors = [0]*(N-1)
  while next_node:
    current = next_node.popleft()
    # 次のノードをキューに入れる際に、どの色の辺を使ったか記録
    if current == 0:
      color = 0
    else:
      color = 0 if first_edge_color[current]!=0 else 1

    for edge, node in node_connections[current]:
      if first_edge_color[node] is not None: continue
      next_node.append(node)
      first_edge_color[node] = color
      edge_colors[edge] = color + 1
      color += 1 if first_edge_color[current]!=color+1 else 2

  print(K)
  print(*edge_colors, sep="\n")

resolve()

if __name__ == "__main__":
    unittest.main()
