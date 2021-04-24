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
        input = """6
2 3 3 1 3 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """6
5 2 4 2 8 8"""
        output = """0"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """32
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5"""
        output = """22"""
        self.assertIO(input, output)

def resolve():
  # 愚直にやっていくと O(N^2) で間に合わないのでどうにか工夫する。
  # 番号の差の絶対値を 1, 2, 3, 4, 5・・・ N で出していく？
  # N*(1+1/2+1/3・・・1/N) が大体 N*logN になるので、多分間に合う。=> 嘘。そうはならんなぁ
  N = int(input())
  A = [[int(x)+i, i-int(x)] for i, x in enumerate(input().split(" "))]

  # R を足した時点でカウントが何個上がるのかは決まっているので、L をカウントしておく => R が見つかった時点で ans += (Lの個数) する。
  ans = 0
  pairs = {}
  for L, R in A:
    if L not in pairs:
      pairs[L] = 1
    else:
      pairs[L] += 1
    if R in pairs:
      ans += pairs[R]
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()