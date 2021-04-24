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
        input = """3.2 3.8 1.1"""
        output = """3"""
        self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """0 0 2"""
    #     output = """13"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """42782.4720 31949.0192 99999.99"""
    #     output = """31415920098"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """0.5 0.5 0.4"""
    #     output = """0"""
    #     self.assertIO(input, output)



def resolve():
  # R <= 10**5 なので、R**2 の点全てを求めようとすると厳しそう。
  # 縦に輪切りする。
  # X-R ~ X+R の範囲で探索する。 縦の格子店の個数を求める。
  # (x-a)**2 +(y-b)**2 = R**2
  from math import floor, ceil, sqrt
  from decimal import Decimal
  import decimal

  X, Y, R = [Decimal(x) for x in input().split(" ")]
  # 対称性があるため。
  X = X if X >= 0 else -X
  Y = Y if Y >= 0 else -Y
  count = 0
  P = Decimal("0.5")
  # X > 0 としたことで、X+R > 0 が成立し、結果、めんどくさい丸め処理が必要なくなった。
  for x in range(int(X-R), int(X+R)+1):
    # int(X-R) って雑な処理をしてるので、 R*R - (x-X)*(x-X) < 0 が発生しうるため事前処理する。
    if R*R - (x-X)*(x-X) < 0: continue
    P = Decimal(R*R - (x-X)*(x-X)).sqrt()
    top = floor(Y+P)
    bottom = ceil(Y-P)
    # print(x, up, down)
    count+= top - bottom + 1
  print(count)

# resolve()

if __name__ == "__main__":
    unittest.main()
