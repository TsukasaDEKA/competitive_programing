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
        input = """2 3
2 2 3
3 2 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3
99 99 99
99 0 99
0 99 99"""
        output = """792"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 2
4 4
4 4
4 4"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
  inf = 10**9
  H, W = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(H)]
  min_val = inf
  for h in range(H):
    min_val = min(min_val, min(A[h]))
  ans = 0
  for h in range(H):
    for w in range(W):
      ans+=A[h][w]-min_val
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
