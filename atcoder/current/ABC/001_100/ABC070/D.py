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
        input = """5
1 2 1
1 3 1
2 4 1
3 5 1
3 1
2 4
2 3
4 5"""
        output = """3
2
4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
1 2 1
1 3 3
1 4 5
1 5 7
1 6 9
1 7 11
3 2
1 3
4 5
6 7"""
        output = """5
14
22"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
1 2 1000000000
2 3 1000000000
3 4 1000000000
4 5 1000000000
5 6 1000000000
6 7 1000000000
7 8 1000000000
8 9 1000000000
9 10 1000000000
1 1
9 10"""
        output = """17000000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**14+1
  from collections import deque
  # 経由する頂点 K が固定であることに着目する。
  # 頂点 K から各頂点までの最短経路がわかっている場合、a-K 間の最短距離 + b-K 間の最短距離が答えになる。
  # 幅優先探索で点 K からの最短距離を求めることで一つのクエリに対して O(1) で回答できるので、全体では O(N+Q)
  N = int(input())
  connections = [[] for _ in range(N)]
  for _ in range(N-1):
    A, B, C = map(int, input().split(" "))
    A-=1
    B-=1
    connections[A].append((B, C))
    connections[B].append((A, C))

  Q, K = map(int, input().split(" "))
  K-=1
  # 幅優先探索
  next_node = deque([K])
  distance_from_K = [inf]*N
  distance_from_K[K] = 0
  while next_node:
    current = next_node.popleft()
    for node, c in connections[current]:
      if distance_from_K[node] != inf: continue
      distance_from_K[node] = distance_from_K[current] + c
      next_node.append(node)

  for _ in range(Q):
    X, Y = [int(x)-1 for x in input().split(" ")]
    print(distance_from_K[X]+distance_from_K[Y])

resolve()

if __name__ == "__main__":
    unittest.main()
