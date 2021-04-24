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
        input = """1
1024"""
        output = """1024
1024"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
3
4
5"""
        output = """12
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
512
512"""
        output = """1024
0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3
4
8
1"""
        output = """13
3"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """10
1
2
3
4
5
6
7
8
9
10"""
        output = """55
0"""
        self.assertIO(input, output)

def resolve():
  # 最大値は全部直線で繋いだ場合だけど、最小値は折り畳んだ時とか考えるので面倒
  # 2 点の場合、最大最小は固定。
  # 3 点の場合、|d0 - d1| ~ (d0 + d1)　の間で任意に決めれる。
  # 4 点の場合、0 - 2 間の距離を |d0 - d1| ~ (d0 + d1)　の間 で任意に決めた後に、d2 を追加する。
  # 辺を追加するごとに最小値最大値を計算していく。
  # 最後に点を追加した時点での最小値最大値が答え

  N = int(input())
  D = [int(input()) for _ in range(N)]
  max_D = D[0]
  min_D = D[0]
  for i in range(1, N):
    if min_D <= D[i] and D[i] <= max_D:
      min_D = 0
    else:
      min_D = min(abs(D[i] - max_D), abs(min_D - D[i]))
    max_D+=D[i]
  print(max_D, min_D, sep="\n")

resolve()


if __name__ == "__main__":
    unittest.main()
