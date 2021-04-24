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
  from math import sqrt
  p = 10**4
  x0, y0, r = [int(float(x)*p) for x in input().split(" ")]

  x0 %= p
  y0 %= p
  rr = r**2

  count = 0

  for y in range(-((r-y0)//p)*p, y0+r+1, p):
      k = int(sqrt(rr-(y-y0)**2))
      if rr < k**2+(y-y0)**2:
          k -= 1

      a, b = -((k-x0)//p), (x0+k)//p
      count += b-a+1

  print(count)

resolve()

if __name__ == "__main__":
    unittest.main()
