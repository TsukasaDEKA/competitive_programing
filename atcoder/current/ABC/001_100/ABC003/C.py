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
        input = """2 2
1000 1500"""
        output = """1000.000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1
1000 1500"""
        output = """750"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 5
2604 2281 3204 2264 2200 2650 2229 2461 2439 2211"""
        output = """2820.031250000"""
        self.assertIO(input, output)

def resolve():
  # レートが高い順に K 個、選び、小さい方から観ていく。
  # (最終レート = (((0+R1)/2) + R2)/2 + R3)/2 ・・・　となるので、できるだけ大きいレートのものを後で観た方が損失が少ない。)
  N, K = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")], reverse=True)

  ans = 0
  for i in reversed(range(K)):
    ans = (ans + A[i])/2

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
