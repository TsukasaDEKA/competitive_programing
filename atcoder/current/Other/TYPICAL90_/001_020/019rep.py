from posixpath import sep
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
6 2 3 9 8 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 3 5 5 3 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
1 2 4 8 16 32 64 128"""
        output = """85"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """15
73 8 55 26 97 48 37 47 35 55 5 17 62 2 60 23 99 73 34 75 7 46 82 84 29 41 32 31 52 32"""
        output = """207"""
        self.assertIO(input, output)

def resolve():
  # どれをペアにすると良いかを考える。
  # 二つのペアが交差することはできない。
  # 外側から考えていくのが良さそう。
  # 再帰的に解く？
  # f(l, r): 区間 l, r における最小値
  inf = 10**3
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  cache = [[inf]*(2*N) for _ in range(2*N)]
  def f(l, r):
    if cache[l][r] != inf:
      return cache[l][r]

    if r-l == 1:
      return abs(A[l]-A[r])
    
    val = abs(A[l]-A[r]) + f(l+1, r-1)
    for r_ in range(l+1, r-1, 2):
      l_ = r_+1
      val = min(val, f(l, r_) + f(l_, r))

    cache[l][r] = val
    return cache[l][r]

  ans = f(0, 2*N-1)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()