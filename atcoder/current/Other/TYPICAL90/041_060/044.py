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
        input = """8 5
6 17 2 4 17 19 1 7
2 0 0
1 7 2
1 2 6
1 4 5
3 4 0"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9 6
16 7 10 2 9 18 15 20 5
2 0 0
1 1 4
2 0 0
1 8 5
2 0 0
3 6 0"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11 18
23 92 85 34 21 63 12 9 81 44 96
3 10 0
3 5 0
1 3 4
2 0 0
1 4 11
3 11 0
1 3 5
2 0 0
2 0 0
3 9 0
2 0 0
3 6 0
3 10 0
1 6 11
2 0 0
3 10 0
3 4 0
3 5 0"""
        output = """44
21
34
63
85
63
21
34
96"""
        self.assertIO(input, output)

def resolve():
  # 2 の処理が計算量かかりすぎるので、インデックス処理でどうにかする。
  # deque 使えば普通にいけるかも。
  # 言語毎の配列の実装次第で違うかも？
  inf = 10**18+1
  N, Q = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  shift = 0
  for _ in range(Q):
    T, X, Y = [int(x)-1 for x in input().split(" ")]
    if T == 0:
      A[(X-shift)%N], A[(Y-shift)%N] = A[(Y-shift)%N], A[(X-shift)%N]
    elif T == 1:
      shift+=1
      if shift>=N:shift%=N
    else:
      print(A[(X-shift)%N])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
