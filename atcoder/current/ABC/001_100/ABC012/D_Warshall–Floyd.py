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

    def test_入力例1(self):
        input = """3 2
1 2 10
2 3 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 5
1 2 12
2 3 14
3 4 7
4 5 9
5 1 18"""
        output = """26"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 6
1 2 1
2 3 1
3 4 1
4 1 1
1 3 1
4 2 1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**6+1

  N, M = map(int, input().split(" "))
  costs = [[inf]*N for _ in range(N)]
  for i in range(N):
    costs[i][i] = 0

  for _ in range(M):
    a, b, t = [int(x)-1 for x in input().split(" ")]
    costs[a][b] = costs[b][a] = t+1

  ranges = range(N)
  for k in ranges:#経由点
    cost_k = costs[k]
    for i in ranges:#始点
      costs_i_k = costs[i][k]
      costs_i = costs[i]
      for j in range(i+1, N):#終点
        if i == j: continue
        costs_i[j] = costs[j][i] = min(costs_i[j], costs[j][i], costs_i_k+cost_k[j])

  ans = inf
  for cost in costs:
    ans = min(ans, max(cost))
  print(ans)

# resolve()

if __name__ == "__main__":
    unittest.main()
