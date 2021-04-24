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

    def test_入力例1(self):
        input = """26"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """41"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """100000"""
        output = """37"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # N <= 100,000 なので、一辺の長さを 1 => N で全探索しても間に合う。
  N = int(input())
  ans = inf
  for rows in range(1, N+1):
    columns = N//rows
    ans = min(ans, abs(rows - columns) + N%rows)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
