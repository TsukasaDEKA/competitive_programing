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
        input = """4 6"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000000000000 3"""
        output = """Large"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000 1"""
        output = """1000000000000000000"""
        self.assertIO(input, output)

def resolve():
  from math import gcd
  def lcm(x, y):
    return (x * y) // gcd(x, y)

  A, B = map(int, input().split(" "))
  ans = lcm(A, B)
  print(ans if ans <= 10**18 else "Large")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
