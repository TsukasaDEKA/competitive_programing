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
        input = """0"""
        output = """4
3 3 3 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """3
1 0 3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2"""
        output = """2
2 2"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """3"""
        output = """7
27 0 0 0 0 0 0"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """1234567894848"""
        output = """10
1000 193 256 777 0 1 1192 1234567891011 48 425"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """100"""
        output = """10
1000 193 256 777 0 1 1192 1234567891011 48 425"""
        self.assertIO(input, output)

    def test_Sample_Input_7(self):
        input = """99"""
        output = """10
1000 193 256 777 0 1 1192 1234567891011 48 425"""
        self.assertIO(input, output)

def resolve():
  # N は 50 個以下である必要がある。
  # a_i は 10**16 + 1000 である必要がある。
  # N 個の要素に対して全て一回ずつ操作を行うと、全ての要素が 1 個ずつ減る。
  # 操作回数は N 回になる。
  # N を決め打ちして K を割ってみる？
  # N = 50 と仮定する。
  # 0 <= K <= 50 の場合、50 を K 個並べたあと 0 を N-K 個並べれば良い。
  # 51 <= K <= 100 の場合、K%50 個 51 を並べて他を 51-(K%50+1) にする。
  # 101 <= K <= 150 の場合、K%50 個 52 を並べて他を 52-(K%50+1) にすれば良さそう。
  # 一般化すると、一旦全ての要素を 50 + (K+49)//50-1 にして、そこから N-K%50 個 (K%50 == 0 の時は 0 個) の要素に対して K%50 を引けば良さそう。
  inf = 10**18+1
  K = int(input())
  N = 50
  ans = [N+(K+N-1)//N-1]*N
  if K%N > 0:
    for i in range(N-K%N):
      ans[i] -= K%N+1
  print(N)
  print(*ans, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()