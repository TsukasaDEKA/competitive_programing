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
        input = """1 1 8 2 2 4
1
4 5"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 1 8 2 2 6
1
4 5"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1 1 8 2 2 5
1
4 5"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """7 7 1 1 3 4
3
8 1
1 7
9 9"""
        output = """YES"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  from math import sqrt
  Tsx, Tsy, Tgx, Tgy, T, V = map(int, input().split(" "))
  N = int(input())
  POS = [list(map(int, input().split(" "))) for _ in range(N)]
  # スタート地点 - 全ての女の子の家 - ゴール地点　の距離をそれぞれ計算して、T*V を超えないか確認する。
  # 誤差が怪しい。
  for x, y in POS:
    diff = sqrt((Tsx-x)**2 + (Tsy-y)**2) + sqrt((Tgx-x)**2 + (Tgy-y)**2)
    if diff <= T*V:
      print("YES")
      return
  print("NO")

resolve()

if __name__ == "__main__":
    unittest.main()
