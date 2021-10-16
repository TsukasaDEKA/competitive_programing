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
        input = """3
5 6
2 1
3 4
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
8 8
3 4
2 3
2 1"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  X, Y = map(int, input().split(" "))
  dp = [[inf]*(Y+1) for _ in range(X+1)]
  dp[0][0] = 0
  for i in range(N):
    x, y = map(int, input().split(" "))
    for x_ in reversed(range(X+1)):
      for y_ in reversed(range(Y+1)):
        dp[x_][y_] = min(dp[x_][y_], dp[max(0, x_-x)][max(0, y_-y)]+1)
  print(dp[-1][-1] if dp[-1][-1] < inf else -1)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()