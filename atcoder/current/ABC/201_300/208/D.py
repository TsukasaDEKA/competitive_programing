import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """3 2
1 2 3
2 3 2"""
        output = """25"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 20
1 2 6
1 3 10
1 4 4
1 5 1
2 1 5
2 3 9
2 4 8
2 5 6
3 1 5
3 2 1
3 4 7
3 5 9
4 1 4
4 2 6
4 3 4
4 5 8
5 1 2

5 2 5
5 3 6
5 4 5"""
        output = """517"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1

  # N が小さいので全ての k でワーシャルフロイドしてもできそう。
  # 400^3厳しいか
  # 途中で総和を出して、ってのを繰り返すといけるかも。
  N, M = map(int, input().split(" "))
  costs = [[inf]*N for _ in range(N)]
  # A = [[int(x) for x in input().split(" ")] for _ in range(M)]
  for i in range(N):
    costs[i][i] = 0

  for _ in range(M):
    a, b, t = [int(x)-1 for x in input().split(" ")]
    costs[a][b] = t+1

  ans = 0
  ranges = range(N)
  for k in ranges:#経由点
    cost_k = costs[k]
    for i in ranges:#始点
      costs_i_k = costs[i][k]
      costs_i = costs[i]
      for j in ranges:#終点
        if i == j: continue
        costs_i[j] = min(costs_i[j], costs_i_k+cost_k[j])
        if costs_i[j] >= inf: continue
        ans += costs_i[j]

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()