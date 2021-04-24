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
        input = """10 10
3 3 3
2 1 1
5 2 3
1 5 6
2 9 3
4 6 12
11 18 5
4 15 25
0 2 3
1 1 7
0 1
0 2
0 10
3 10
0 100
3 8
1 5
2 9
3 4
6 9"""
        output = """8.843002
80.992182
4173.878112
3865.997282
8512.668894
2882.971997
1227.377293
3629.490541
114.081013
1747.545749"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 5
5 10 10
4 100 100
3 1000 1000
2 1000 1000
1 1000 1000
0 3
2 1000
4 314
3 217
5 432"""
        output = """9409079.422279
3139502408.531295
2100737789.465234
1613523459.243475
2532621914.444282"""
        self.assertIO(input, output)


def resolve():
  from math import pi
  # Q は多いけど、N は少ないので、 O(N*Q) だと間に合う。
  # 累計取らなきゃいけないので厳しい。
  N, Q = map(int, input().split(" "))
  CORN = [list(map(int, input().split(" "))) for _ in range(N)]

  for _ in range(Q):
    a, b = map(int, input().split(" "))
    ans = 0.0
    for x, r, h in CORN:
      # 範囲の重複チェック
      if x < b and a < x+h:
        # 重複範囲をチェック
        r1 = r
        a_ = x
        if x < a:
          r1 = r*(x+h-a)/h
          a_ = a

        r2 = 0
        b_ = x+h
        if b < x+h:
          r2 = r*(x+h-b)/h
          b_ = b
        h = b_-a_
        ans += (pow(r1,2)+pow(r2,2)+r1*r2)*h
    print(ans*pi/3.0)

resolve()


if __name__ == "__main__":
    unittest.main()
