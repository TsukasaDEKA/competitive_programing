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
        input = """1 1 1"""
        output = """28.2743338823"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 1 1"""
        output = """75.3982236862"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """16 2 27"""
        output = """6107.2561185786"""
        self.assertIO(input, output)

def resolve():
  from math import pi
  L1, L2, L3 = map(int, input().split(" "))
  min_ = abs(min(min(L1+L2-L3, L2+L3-L1, L1+L3-L2), 0))
  max_ = L1+L2+L3
  ans = (max_**2 - min_**2)*pi

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
