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

    def test_入力例_1(self):
        input = """2 2 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000 999999999999999999 999999999999999998"""
        output = """2999999999999999994"""
        self.assertIO(input, output)

def resolve():
  from math import gcd
  # A, B, C の最大公約数を求めて、何回カットすれば良いか求める。
  A, B, C = map(int, input().split(" "))
  g = gcd(A, B)
  g = gcd(C, g)
  ans = (A//g)+(B//g)+(C//g)-3
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
