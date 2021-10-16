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
        input = """4
3 4 3 2"""
        output = """6 8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 4 100 3 2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
2 2 2 2 2 2 2 2 2 2"""
        output = """2 3"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5
2 2 5 3 2"""
        output = """6 9"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 逆順から計算して上限下限をそれぞれ計算する。
  # A(i-1) を見た時の上限下限を l(i-1), r(i-1) とすると、
  # A(i) を見た時の下限は l(i-1) <= l(i) <=r(i-1) となり、
  # 上限は l(i-1) <= r(i) <= r(i-1) となる。
  # また、 正の整数を用いて l は Ai*K、 r は Ai*K - 1 で表現できる。
  # 例 1 を見ると、2, 3, 4, 2 なので、
  # [2:3], [3:5], [4:7], [6:8] => min 6, max 8
  K = int(input())
  A = list(reversed([int(x) for x in input().split(" ")]))
  l = 2
  r = 2
  for i in range(K):
    l_ = (l+A[i]-1)//A[i]*A[i]
    r_ = r//A[i]*A[i]+(A[i]-1)
    if l_ > r:
      print(-1)
      return
    l = l_
    r = max(l+A[i]-1, r_)
  print(l, r, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()