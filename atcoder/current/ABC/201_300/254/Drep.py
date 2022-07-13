import sys
from io import StringIO
import unittest

from numpy import square

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
        input = """4"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """254"""
        output = """896"""
        self.assertIO(input, output)

def resolve():
  N = int(input())

  ans = 0
  for n in range(1, N+1):
    # i とペアになる j の内、最小の数字 k を求める。
    k = n
    for d in range(2, int(-(-n**0.5//1))+1):
      d_ = d**2
      while k%d_==0:
        k//=d_
    # <k に平方数をかけたもの> * n は平方数なので、 k * (x**2) <= N になる x の個数を求める。
    for d in range(1, int(-(-N**0.5//1))+1):
      if k*(d**2) > N: break
      ans += 1

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()