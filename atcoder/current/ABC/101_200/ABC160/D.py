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
        input = """5 2 4"""
        output = """5
4
1
0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 1 3"""
        output = """3
0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7 3 7"""
        output = """7
8
4
2
0
0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 4 8"""
        output = """10
12
10
8
4
1
0
0
0"""
        self.assertIO(input, output)

from collections import deque

def resolve():
  # dp + 幅優先探索する。O(N**2) で N**2 <= 4*10**6 なので間に合うはず。
  inf = 10**10+1

  N, X, Y = map(int, input().split(" "))
  X, Y = X-1, Y-1
  connects = [[x-1, x+1] for x in range(N)]
  del connects[0][0]
  del connects[-1][1]
  connects[X].append(Y)
  connects[Y].append(X)

  ans = [0] * N
  dp = [[inf]*N for _ in range(N)]

  for start_node in range(N):
    dp[start_node][start_node] = 0

    next_nodes = deque(connects[start_node])
    while next_nodes:
      node = next_nodes.popleft()

      temp_next_nodes = []
      if dp[start_node][node] == inf:
        adjacents_val = [ dp[start_node][x] for x in connects[node] ]

        dp[start_node][node] = min(adjacents_val)+1
        ans[dp[start_node][node]]+=1
        temp_next_nodes.extend(connects[node])

      next_nodes.extend(temp_next_nodes)
  for answer in ans[1:]:
    print(int(answer/2))
  # print(dp)
resolve()

if __name__ == "__main__":
    unittest.main()
