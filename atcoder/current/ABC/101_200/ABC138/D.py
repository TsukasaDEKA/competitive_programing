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
        input = """4 3
1 2
2 3
2 4
2 10
1 100
3 1"""
        output = """100 110 111 110"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10"""
        output = """20 20 20 20 20 20"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 2
1 3
2 3
2 4
3 6
2 5
1 10
1 10"""
        output = """20 20 20 20 20 20"""
        self.assertIO(input, output)

from collections import deque

def resolve():
  N, Q = map(int, input().split(" "))

  connections = [None]*N
  for _ in range(N-1):
    a, b = [int(x)-1 for x in input().split(" ")]
    if connections[a] == None: connections[a] = set()
    connections[a].add(b)
    if connections[b] == None: connections[b] = set()
    connections[b].add(a)

  values = [0]*N
  for _ in range(Q):
    p, x = [int(x) for x in input().split(" ")]
    values[p-1] += x

  # 幅優先探索的なことをしながら 頂点の値を更新していく。
  visited = [False]*N
  visited[0] = True
  next_nodes = deque([0])
  while next_nodes:
    current_node = next_nodes.popleft()
    if connections[current_node] is not None:
      for child in connections[current_node]:
        if visited[child]: continue
        visited[child] = True
        values[child]+=values[current_node]
        next_nodes.append(child)

  print(*values)
resolve()

if __name__ == "__main__":
    unittest.main()
