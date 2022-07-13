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
        input = """10 3 5"""
        output = """22"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000 314 159"""
        output = """495273003954006262"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000000 1000000000 2"""
        output = """0"""
        self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """1 2 2"""
    #     output = """0"""
    #     self.assertIO(input, output)

def resolve():
  from math import gcd
  from functools import reduce
  def lcm(x, y):
    return (x * y) // gcd(x, y)
  N, A, B = map(int, input().split(" "))
  ans = (N*(N+1))//2

  a, n, d = A, N//A, A
  # print(a, n, d, n*(2*a + (n-1)*d)//2)
  ans -= n*(2*a + (n-1)*d)//2

  a, n, d = B, N//B, B
  # print(a, n, d, n*(2*a + (n-1)*d)//2)
  ans -= n*(2*a + (n-1)*d)//2

  l = lcm(A, B)
  a, n, d = l, N//l, l
  # print(a, n, d, n*(2*a + (n-1)*d)//2)
  ans += n*(2*a + (n-1)*d)//2

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()