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
        input = """3 2
0 1
1 2
2 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3
0 0
1 1
0 2
2 3
3 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 4
0 3
3 5
2 7
9 0
5 6
4 3
7 8
6 5
9 9
2 1"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3 2
0 0
500000000 500000000
1000000000 1000000000"""
        output = """500000000000000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 二点間の距離の最大値の二乗ということは、X, Y のそれぞれの差の二乗の和。
  # 全ての点の間の距離を求めるのはそこまで計算量がかかる訳じゃない。
  # 15*14/2 だから 105 通りしかない。答えはこの中にあるはず。
  # 辺の数は
  # 全ての組み合わせの距離を出す => 長い順に分割していけるかチェックするって流れでいけるか？
  from collections import defaultdict
  N, K = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]

  distancees = defaultdict(int)
  for i in range(N):
    for j in range(N):
      val = (A[i][0]-A[j][0])**2 + (A[i][1]-A[j][1])**2
      distancees[val] |= 1<<i
      distancees[val] |= 1<<j

  distancees = sorted(distancees.items(), key=lambda x: x[0])
  for key, val in distancees:
    print(key, bin(val))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
