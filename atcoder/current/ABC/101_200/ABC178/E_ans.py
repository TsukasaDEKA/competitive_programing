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
1 1
2 4
3 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1 1
1 1"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # N <= 2*10**5 なので総当たりは間に合わない。
  # 45 度回転してみて解けるかどうか考える。
  inf = 10**15+1
  N = int(input())
  X_Y = [[int(x) for x in input().split(" ")] for _ in range(N)]
  lotated_X_Y = [[x-y, x+y] for x, y in X_Y]

  min_x = inf
  max_x = -inf
  min_y = inf
  max_y = -inf

  for x, y in lotated_X_Y:
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
  print(max(max_x-min_x, max_y-min_y))

resolve()

if __name__ == "__main__":
    unittest.main()
