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
        input = """3 5
4 2 1
2 3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 8
4 2 1
2 3 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """11 14
3 1 4 1 5 9 2 6 5 3 5
8 9 7 9 3 2 3 8 4 6 2"""
        output = """12"""
        self.assertIO(input, output)

def resolve():
  # 単純に A を小さい順に F を大きい順に並び替えてそれぞれマッチさせれば良い。
  # 修行の処理について、答えが X である時、Ai - X//Fi が行わなければいけない修行の回数になる。
  # これを全部足し合わせた数が K を超えなければ X を達成できる。
  # X は射撃王的に二分探索で求めれば良さそう。
  # O(NlogN) で解ける。
  N, K = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")])
  F = sorted([int(x) for x in input().split(" ")], reverse=True)

  def binary_search(ok, ng, solve):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid): ok = mid
      else: ng = mid
    return ok
  
  def solve(X):
    k = 0
    for i in range(N):
      k += max(0, A[i] - X//F[i])
    return k <= K

  ok = 10**18
  ng = -1
  print(binary_search(ok, ng, solve))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()