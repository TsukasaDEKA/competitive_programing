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
        input = """0.2 0.8 1.1"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """0 0 2"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """42782.4720 31949.0192 99999.99"""
        output = """31415920098"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """0.5 0.5 0.4"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
  # R <= 10**5 なので、R**2 の点全てを求めようとすると厳しそう。
  # 縦に輪切りする。
  # X-R ~ X+R の範囲で探索する。 縦の格子点の個数を求める。
  # (x-a)**2 +(y-b)**2 = R**2
  from math import floor, ceil, isqrt
 
  base = 10**4
  # X, Y, R = map(lambda a: int(a.replace('.', '')) * 10**(5-(len(a)-(a.find('.') % len(a)))), input().split(" "))
  X, Y, R = [int(float(x)*base) for x in input().split(" ")]
  # 対称性があるので
  X = X if X >= 0 else -X
  Y = Y if Y >= 0 else -Y
  # 整数分の移動は答えに影響を与えないので
  X %= base
  Y %= base
  R_2 = R**2

  left  = ((X-R+base-1)//base)*base
  right = X+R

  # print(X, Y, R)
  count = 0
  for x in range(left, right+1, base):
    P = isqrt(R_2 - (x-X)**2)
    if R_2 < P**2 + (x-X)**2: P -= 1
    top = (P+Y)//base
    bottom = (Y-P+base-1)//base
    # print(x//base, ":", P, Y, P+Y, top, Y-P, bottom)
    count += top - bottom + 1
  print(count)

resolve()

if __name__ == "__main__":
    unittest.main()
